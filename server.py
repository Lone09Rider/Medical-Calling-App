from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

@app.route("/answer", methods=["POST"])
def answer():
    response = VoiceResponse()
    gather = Gather(num_digits=1, action="/handle-response", timeout=10)
    gather.say(
        "Hello, this is a reminder call from X Y Z Hospital, a trusted healthcare center "
        "known for providing excellent medical care and patient support. "
        "You have an appointment scheduled with your doctor at 10:00 AM tomorrow morning at X Y Z Hospital. "
        "To confirm your appointment, please press 1. "
        "If you wish to cancel your appointment, please press 2. "
        "To hear this message again, please press 3. "
        "Thank you for choosing X Y Z Hospital. We look forward to serving you and ensuring your health and well-being.",
        voice="alice"
    )
    response.append(gather)
    response.say("We did not receive your input. Goodbye!", voice="alice")
    return str(response)


@app.route("/handle-response", methods=["POST"])
def handle_response():
    digit = request.form.get("Digits", "")
    response = VoiceResponse()

    if digit == "1":
        response.say(
            "Thank you! Your appointment has been confirmed. "
            "We look forward to seeing you tomorrow at 10 AM.",
            voice="alice"
        )
        response.redirect("/answer")
    elif digit == "2":
        response.say(
            "Your appointment has been cancelled. "
            "Please call us back to reschedule. Goodbye!",
            voice="alice"
        )
    elif digit == "3":
        response.redirect("/answer")
    else:
        response.say("Invalid option. Goodbye!", voice="alice")

    return str(response)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
