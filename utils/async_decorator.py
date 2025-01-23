import asyncio
from threading import current_thread
from ctypes import c_ulong, pythonapi, py_object
from typing import Any, Awaitable, Callable

# Based on run_in_executor
def async_decorator(func: Callable) -> Awaitable:
    """Decorate a sync function to be used as async. Supports task cancelling.
    This version is based on loop.run_in_executor()
    """
    async def run_cancellable(*args, **kwargs) -> Any:
        def worker() -> Any:
            context["thread"] = current_thread().ident
            return func(*args, **kwargs)
        context: dict = {"thread": None}
        loop: asyncio.AbstractEventLoop = asyncio.get_running_loop()
        future: asyncio.Future = asyncio.ensure_future(loop.run_in_executor(None, worker))
        while not future.done():
            try:
                await asyncio.wait([future])
            except asyncio.CancelledError:
                thread_id: c_ulong = c_ulong(context["thread"])
                exception: py_object = py_object(asyncio.CancelledError)
                ret: int = pythonapi.PyThreadState_SetAsyncExc(thread_id, exception)
                if ret > 1:  # This should NEVER happen, but shit happens
                    pythonapi.PyThreadState_SetAsyncExc(thread_id, None)
        return future.result()
    return run_cancellable