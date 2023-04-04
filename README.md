# OrcaleAIBot


This code is a Python program that runs a chatbot and image generator using OpenAI's GPT-3 API. It listens for messages in a Discord server and responds to them if they match certain conditions. It uses the discord and discord.ext libraries for interacting with the Discord API, as well as the openai library for interacting with the GPT-3 API. The program reads configuration settings from a config.ini file, which includes the OpenAI API key, the Discord bot token, and a list of guild IDs to monitor.

When a user sends a message starting with "!chat", the program sends the message to the GPT-3 API and returns a response. When a user sends a message starting with "!img", the program sends the message to the GPT-3 API to generate an image based on the text, which is then returned to the user as a URL. The program also includes an on_connect event handler to log in to Discord and monitor the configured guilds.

The code uses Python's asyncio library to handle asynchronous operations and improve the responsiveness of the bot. It also includes exception handling to handle errors that may occur when interacting with the APIs. Overall, this code provides a basic example of how to use OpenAI's GPT-3 API and the Discord API to create a chatbot and image generator.
