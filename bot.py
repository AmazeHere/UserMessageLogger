import discord

TOKEN = "add your token here"
USERID = "add user id here"

class DMLogger(discord.Client):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id

    async def on_ready(self):
        print('Logged in as {0.user}'.format(self))

    async def on_message(self, message):
        if message.author.id == self.user_id:
            print('{0.author}: {0.content}'.format(message))

if __name__ == '__main__':
    user_id = USERID
    client = DMLogger(user_id)
    client.run(TOKEN)