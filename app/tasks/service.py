import requests

from app.settings import settings



def send_doc_and_msg_to_tg_bot(caption, chat_id: int, file_path) -> dict:
    files = {
        'document': open(file_path, 'rb')
    }

    return requests.post(
        f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendDocument',
        data={'chat_id': chat_id, 'caption': caption},
        files=files
    ).json()
