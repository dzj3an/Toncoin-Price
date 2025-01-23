# Toncoin Price Bot

Este bot de Telegram publica el precio de **Toncoin** en un canal específico cada minuto. Es útil para quienes deseen seguir de cerca la cotización de Toncoin.

Apoya al creador uniéndote a su canal de desarrollo en Telegram: [J3an | Dev](https://t.me/iJ3AN)
## Funcionalidades

- Obtiene el precio de Toncoin desde una API oficial.
- Envía actualizaciones al canal de Telegram configurado.
- Puedes apagar el proceso o prenderlo cuando gustes.


Puedes ver las funcionalidades del Bot uniéndote al siguiente canal:  
[https://t.me/iTonPrice](https://t.me/iTonPrice)

---

## Requisitos

Asegúrate de tener las siguientes dependencias instaladas:

- [**kurigram**](https://pypi.org/project/kurigram/)
- [**pyromod**](https://pypi.org/project/pyromod/)
- [**TgCrypto**](https://pypi.org/project/TgCrypto/)
- [**pytonapi**](https://pypi.org/project/pytonapi/)

Puedes instalarlas ejecutando:

```bash
pip install -r requirements.txt
```

---

## Configuración

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/dzj3an/Toncoin-Price.git
   cd Toncoin-Price
   ```

2. **Obtén tus credenciales:**

   - **BOT_TOKEN**: Genera un token para tu bot desde [@BotFather](https://t.me/BotFather) en Telegram.
   - **API_HASH** y **API_ID**: Crea una aplicación en el sitio de [Telegram](https://my.telegram.org/auth) para obtener estas credenciales.
   - **TON_TOKEN**: Regístrate en [Ton Console](https://tonconsole.com/) para obtener un token de acceso.

3. **Configura las credenciales en `config.py`:**

   ```python
   BOT_TOKEN = "TU_BOT_TOKEN"
   API_HASH = "TU_API_HASH"
   API_ID = TU_API_ID  # Ejemplo: 12345678
   TON_TOKEN = "TU_TON_TOKEN"
   OWNERS_ID = [123456789]  # IDs de los administradores del bot
   CHANNEL_TON = -1001234567890  # ID del canal donde se enviarán los precios
   ```

---

## Ejecución

Ejecuta el bot con el siguiente comando:

```bash
python main.py
```

Al iniciar, dirígete al Bot y presiona /menu luego prende el proceso y listo.

---

## Créditos

Este bot fue creado por [J3an](https://github.com/dzj3an).


Ayudarías muchísimo si sigues la página de la librería que utilizamos en este bot para conectar con Telegram. Dicha librería es **kurigram**, un fork de **pyrogram**.  

Encuentra información en su canal oficial:  
[Kurigram](https://t.me/kurigram_news)

Deja tu estrella en este repositorio y compártelo con tus amigos. 😊
