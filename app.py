from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return "OK", 200

@app.route("/voice", methods=["GET", "POST"])
def voice():
    patient_name = request.values.get("patient_name", "your child")
    visit_label = request.values.get("visit_label", "their upcoming visit")
    insurance_type = request.values.get("insurance_type", "your insurance")

    resp = VoiceResponse()

    with resp.gather(
        input="dtmf",
        num_digits=1,
        timeout=5,
        action="/handle-key",
        method="POST"
    ) as gather:
        gather.say(
            f"Hello, this is MedTest calling about {patient_name}. "
            f"They are scheduled for {visit_label}. "
            f"We have {insurance_type} on file. "
            "Press 1 to confirm this appointment, "
            "press 2 to reschedule, "
            "or press 3 to speak to our staff.",
            voice="alice",
            language="en-US"
        )

    resp.say("We did not receive any input. Goodbye.", voice="alice")
    return Response(str(resp), mimetype="text/xml")

@app.route("/handle-key", methods=["POST"])
def handle_key():
    digit = request.values.get("Digits", "")
    resp = VoiceResponse()

    if digit == "1":
        resp.say("Thank you. Your appointment is confirmed. Goodbye.", voice="alice")
    elif digit == "2":
        resp.say("A staff member will contact you to reschedule. Goodbye.", voice="alice")
    elif digit == "3":
        resp.say("Please hold while we connect you.", voice="alice")
        # Replace with your real office number:
        resp.dial("+1YOUR_OFFICE_NUMBER")
    else:
        resp.say("We did not understand your selection. Goodbye.", voice="alice")

    return Response(str(resp), mimetype="text/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)