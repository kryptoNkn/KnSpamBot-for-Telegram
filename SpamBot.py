import requests

TOKEN = "" # Enter your bot token

def send_message(chat_ids, message, num_messages=1):
    if not isinstance(chat_ids, list):
        chat_ids = [chat_ids]

    for chat_id in chat_ids:
        for _ in range(num_messages):
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            response = requests.get(url)
            print(response.json())

chat_ids = [""]  # Enter the ID of the user you want to send a message to
message = "" # Enter the text you want to send
num_messages = 5  # number of messages sent
send_message(chat_ids, message, num_messages)

single_chat_id = "" # Enter the ID of the user you want to send a message to
send_message(single_chat_id, message, num_messages)