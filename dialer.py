import os
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
BASE_URL = os.environ.get("BASE_URL")  # e.g. https://your-service.onrender.com

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def call_parent(row):
    """
    row is a dict-like object with:
    - parent_phone
    - patient_name
    - parent_name (optional)
    - visit_label
    - insurance_type
    """
    params = {
        "patient_name": row.get("patient_name", ""),
        "visit_label": row.get("visit_label", ""),
        "insurance_type": row.get("insurance_type", "")
    }

    url = f"{BASE_URL}/voice?{urlencode(params)}"

    call = client.calls.create(
        to=row["parent_phone"],
        from_=TWILIO_NUMBER,
        url=url,
        method="POST"
    )
    print(f"Placed call SID={call.sid} to {row['parent_phone']}")