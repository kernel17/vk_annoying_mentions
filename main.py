from vkbottle import user
from vkbottle.user import Message
import schedule
import time
from datetime import datetime

API_TOKEN = ""
FROM_ID : int
CHAT_ID : int = 1


client = user.User(token=API_TOKEN)
count : int = 0
timestamp : float = 0.0
def get_readable_from_timestamp():
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


@client.on.chat_message()
async def message_handler(message: Message):
    if ("@all" in message.text or "@все" in message.text) and (True if FROM_ID == 0 else FROM_ID in message.text):
        count += 1
        if timestamp != 0.0:
            await message.reply(message=f'Опять ты со своим @all достаешь всех. Дата отправки последнего @all: {get_readable_from_timestamp()}')
        else:
            await message.reply(message=f'Опять ты со своим @all достаешь всех.')

        timestamp = time.time()


async def send_message():
    if count == 0:
        await client.api.messages.send(chat_id=1, text="Вот это да! За сегодня Корнеев не отправил ни одного @all!")
    else:
        await client.api.messages.send(chat_id=1, text=f'Внимание! Количество @all отправленных Корнеевым за сегодня: {count}, дата отправки последнего: {get_readable_from_timestamp()}')
    count = 0
    timestamp = 0.0


if __name__ == "__main__":
    schedule.every().day.at("00:00").do(send_message)
    client.run_forever()