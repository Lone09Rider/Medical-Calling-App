import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_PHONE_NUMBER")
to_number = os.getenv("TO_PHONE_NUMBER")

# Replace this with your ngrok URL after running ngrok
NGROK_URL = "https://XXXXXXXX.ngrok-free.dev"

client = Client(account_sid, auth_token)

call = client.calls.create(
    to=to_number,
    from_=from_number,
    url=f"{NGROK_URL}/answer"
)

print(f"Call started! Call SID: {call.sid}")
print(f"Calling {to_number} from {from_number}")
