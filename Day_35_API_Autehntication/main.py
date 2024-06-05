import vonage

client = vonage.Client(key="611f9916", secret="B4ZIKC9dqZVGEktw")
sms = vonage.Sms(client)

responseData = sms.send_message(
    {
        "from": "918910284642",
        "to": "916290213235",
        "text": "Maya HOTDOG",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")