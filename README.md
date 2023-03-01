# vk_annoying_mentions

do you get annoyed of hundreds and hundreds '@all', '@online', '@everyone' mentions? well, this bot will help remind the sender of such mentions that he is doing bad things

## Usage

Open main.py file with any text editor, and change values of these variables:

```
API_TOKEN = "<your_api_token>"

FROM_ID : int = <id of the user from whom messages will be processed, 0 if from everyone>

PEER_ID : int = <id of the chat from which messages will be processed >
```

this bot has a dependency on VKBottle, so you need install it before all:

```
pip install vkbottle
```

and simply run bot:

```
python3 main.py
```
