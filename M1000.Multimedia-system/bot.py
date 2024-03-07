from twitchio.ext import commands 
import os
from googleapiclient.discovery import build
from discord.ext import commands
import discord


# Define your intents
intents = discord.Intents.default()
intents = discord.Intents.all()

# Create an instance of your bot with the intents
bot = commands.Bot(command_prefix='$', intents=intents)

# bot = commands.bot(
#     #set twitch bot prefix
#     irc_token=os.environ['TMI_TOKEN'],
#     client_id=os.environ['CLIENT_ID'],
#     nick=os.environ['BOT_NICK'],
#     prefix=os.environ['BOT_PREFIX'],
#     initial_channel=[os.environ['CHANNEL']]
# )

#twitch bot system
# @twitch_bot.event
# async def event_message(message):
#     print(message.content)

# @twitch_bot.event
# async def event_raw_(data):
#     print(data)


#youtbe api
YOUTUBE_API_KEY = 'AIzaSyAqLhThhvb-yvbLafIRO97vndeIpAt4JdI'

def youtube_search(query):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    request = youtube.search().list(
        part='snippet',
        q=query,
        maxResults=1
    )
    response = request.execute()
    video_id = response['items'][0]['id']['videoId']
    return f'https://www.youtube.com/watch?v={video_id}'

@bot.command()
async def youtube(ctx, *, query):
    result = youtube_search(query)
    await ctx.send(result)
    
                    

#token
TOKEN = "MTE3NjE2Nzk4NzE0MTY4MTE4Mw.G5KoMQ._51UVQSo4B8rUD97MNe8GLoiwgJl-Pp0JhU_tc"

#bot run
bot.run(TOKEN)