import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Your Account SID and Auth Token from console.twilio.com
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="whatsapp:+votre numéro",
    from_="whatsapp:+14155238886",
    body="Hello Python!",
)

print(message.sid)