# 🏥 Medical Calling App

An AI-powered automated voice calling agent for hospitals and healthcare centers — built with **Twilio** and **Python**. Automatically calls patients with appointment reminders and handles their responses in real-time.

---

## 📞 How It Works

1. The agent **calls the patient** automatically
2. Plays a professional **appointment reminder message**
3. Patient responds by pressing:
   - **1** → Confirm appointment *(loops back to menu)*
   - **2** → Cancel appointment
   - **3** → Hear the message again
4. The agent responds accordingly and ends or loops the call

---

## 🚀 Features

- Outbound automated voice calls via Twilio
- Interactive keypress responses (IVR)
- Loop on confirmation — keeps the conversation going
- Fully customizable hospital name, time, and message
- Lightweight Flask webhook server
- Easy to deploy with ngrok for local testing

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Twilio | Voice call API |
| Flask | Webhook server |
| ngrok | Expose local server to Twilio |
| python-dotenv | Manage environment variables |

---

## ⚙️ Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/Lone09Rider/Medical-Calling-App.git
cd Medical-Calling-App
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
```bash
cp .env.example .env
```
Fill in your credentials in `.env`:
```env
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_number
TO_PHONE_NUMBER=patient_phone_number
```

### 4. Start the Flask server
```bash
python server.py
```

### 5. Expose with ngrok (in a new terminal)
```bash
ngrok http 5000
```
Copy the `https://XXXX.ngrok-free.dev` URL and paste it in `agent.py`:
```python
NGROK_URL = "https://XXXX.ngrok-free.dev"
```

### 6. Trigger the call
```bash
python agent.py
```

---

## 📁 Project Structure

```
Medical-Calling-App/
├── agent.py          # Triggers the outbound call
├── server.py         # Flask webhook — handles call flow
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variable template
├── .gitignore        # Ignores .env and sensitive files
└── README.md         # You are here
```

---

## 📋 Requirements

- Python 3.7+
- [Twilio Account](https://twilio.com) (free trial available)
- [ngrok Account](https://ngrok.com) (free tier available)

---

## ⚠️ Twilio Trial Note

On a Twilio trial account, every outbound call begins with:
> *"You have a trial account. Press any key to execute your code."*

Simply press any key to proceed to your custom message. Upgrade your Twilio account to remove this prompt.

---

## 🔒 Security

- Never commit your `.env` file — it's listed in `.gitignore`
- Use `.env.example` as a template for others
- Regenerate your Twilio Auth Token if accidentally exposed

---

## 🙌 Contributing

Pull requests are welcome! Feel free to open an issue for feature requests or bugs.

---

## 📄 License

MIT License — free to use and modify.
