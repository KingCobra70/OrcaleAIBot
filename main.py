import discord
from discord.ext import commands
import openai
import configparser
from PIL import Image as PIL_Image
from io import BytesIO

config = configparser.ConfigParser()
config.read("config.ini")
description = '''CHATGPT BOT'''

openai.api_key = config.get("global", "API_KEY")
bot_token = config.get("global", "BOT_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix="!", description=description, intents=intents)
api_delay = int(config['discord_bot']['api_delay'])

@client.event
async def on_connect():
    guild_ids = [int(guild_id) for guild_id in config.get("global", "guild_id").split(',')]
    for guild in client.guilds:
        if guild.id not in guild_ids:
            await guild.leave()
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('______________________')
    print('Powered By OpenAI API')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#Chat Command
    if message.content.startswith("!chat"):
        channel = message.channel
        query = []
        async for msg in channel.history(limit=1):
            query.append(msg)
        query.reverse()
        query_string = "\n".join(f"User: {msg.content}" for msg in query)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=[{"role": "assistant", "content": query_string}],
            max_tokens=2000
        )
        await message.channel.send(response.choices[0].message.content)


# Image Command
    if message.content.startswith('!img'):
        channel = message.channel
        query = []
        async for msg in channel.history(limit=1):
            query.append(msg)
        query.reverse()
        query_string = "\n".join(f"User: {msg.content}" for msg in query)
        image_url = create_image(query_string)
        if image_url.startswith("Sorry"):
            await message.channel.send(image_url)
        else:
            await message.channel.send(image_url)


def create_image(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
        )
        return response["data"][0]["url"]
    except openai.error.InvalidRequestError:
        return "Your thinking is impressive, but I'm afraid I lack the skill to put it into a visual form."


@client.command(pass_context=True)
async def chat(ctx):
    await ctx.send("testing")


client.run(bot_token)