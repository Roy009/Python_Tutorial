import telepot
from telepot.loop import MessageLoop
import datetime
# Replace 'YOUR_BOT_TOKEN' with the token you obtained from BotFather
bot = telepot.Bot('6468351030:AAEKbWGfwnwWb9lghSU0tBIpkUpF8zROiNM')

def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        command = msg['text']
        if command == '/start':
            bot.sendMessage(chat_id, 'Hello! I am your bot.')
        elif command == '/time':
            current_time = datetime.datetime.now().strftime('%H:%M:%S')
            bot.sendMessage(chat_id, f'The current time is {current_time}.')

        else:
            # Echo back the received text
            bot.sendMessage(chat_id, f'You said: {command}')

if __name__ == '__main__':
    MessageLoop(bot, handle_message).run_as_thread()
    print('Bot is listening...')

    # Keep the program running
    while True:
        pass
