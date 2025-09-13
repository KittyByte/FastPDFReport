import requests

from app.settings import settings



def send_msg_to_tg_bot(msg, chat_id: int) -> dict:
    return requests.post(
        f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage',
        data={'chat_id': chat_id, 'text': msg}
    ).json()
