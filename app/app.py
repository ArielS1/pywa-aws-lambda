import uvicorn
from fastapi import FastAPI, Request
from mangum import Mangum
from wa.client import get_wa_client

app = FastAPI()
handler = Mangum(app)

@app.patch('/RegisterWebhook')
async def register_webhook(request: Request):
    get_wa_client(server=app, callback_url=f'https://{request.url.hostname}')
    # the challange request is sent after 1 second, so we need to wait for it to be processed
    # if we won't wait, the transaction will end before the http request will be made
    from time import sleep
    sleep(2)
    return { "message": "Webhook registered" }

get_wa_client(app) # initialize client at cold start without registering webhook

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8080)
