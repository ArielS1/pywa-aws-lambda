from pywa import WhatsApp

wa = None

def init_wa_client(server = None, callback_url: str = None) -> WhatsApp:
    global wa
    from os import environ
    
    wa = WhatsApp(
        server=server,
        callback_url=callback_url, # when None, the challange http request won't be invoked
        webhook_endpoint='/whatsapp',
        phone_id=environ.get('WHATSAPP_PHONE_ID'),
        token=environ.get('WHATSAPP_TOKEN'),
        business_account_id=environ.get('WHATSAPP_BUSINESS_ACCOUNT_ID'),
        verify_token=environ.get('WHATSAPP_VERIFY_TOKEN'),
        app_id=environ.get('WHATSAPP_APP_ID'),
        app_secret=environ.get('WHATSAPP_APP_SECRET'),
        webhook_challenge_delay=1
    )
    
    from wa.handlers import text #init inbound messages handlers file
    return wa
    
def get_wa_client(server = None, callback_url: str = None) -> WhatsApp:
    global wa
    return init_wa_client(server, callback_url) if wa is None or callback_url is not None else wa