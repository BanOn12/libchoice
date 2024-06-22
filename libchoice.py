import discord
from discord.ext import commands,tasks
import os
import nacl.utils
import youtube_dl
from youtube_dl import YoutubeDL
from time import *
import ffmpeg

named = str

TOKEN = ""
prefix = "%"
instens = discord.Intents().all()
client = discord.Client(intents=instens)
bot = commands.Bot(command_prefix=prefix, intents=instens)

@bot.command()
async def hello(ctx):
    embed = discord.Embed(color=0xff9900, title='Hello')  
    embed.add_field(name='hello', value='bot say you hi!', inline=False)  
    await ctx.send(embed=embed)



class StoryDrop(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Страшная История 1", description= "Страшно шо пиздос"),
            discord.SelectOption(label="Страшная История 2", description= "Шед где дизайн"),
            discord.SelectOption(label="Страшная История 3", description= "Тенькью Пабло")
            ]
        super().__init__(placeholder="Выбери Историю", options=options, min_values=1, max_values=1)
    
    async def callback(self, interaction: discord.Interaction) :
        global named
        named = self.values[0]
        await interaction.response.send_message(f"Вы выбрали историю: {self.values[0]}")
        #print(named)
        #await ctx.message.add_reaction('✔️')
        #voice_channel = ctx.author.voice.channel
        #voice_client = await voice_channel.connect() 
        #audio_source = discord.FFmpegPCMAudio(f'audio\\{named}.mp3')
        #voice_client.play(audio_source)
        return named


class StoryView (discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(StoryDrop())
@bot.command()
async def playtest(ctx: commands.Context):
    await ctx.send("Выбери", view=StoryView())
    #def check():
    #await ctx.message.add_reaction('✔️') 



    voice_channel = ctx.author.voice.channel
    voice_client = await voice_channel.connect() 
    #bot.wait_for("reaction_add",check=check)
    print(named)
    #audio_source = discord.FFmpegPCMAudio(f'audio\\{file}.mp3')
    #voice_client.play(audio_source)
    
@bot.command()
async def play(ctx: commands.Context):
    voice = discord.utils.get(bot.voice_clients)
    audio_source = discord.FFmpegPCMAudio(f'audio\\{named}\\story_1.mp3')
    print (named)
    voice.play(audio_source)
    embed = discord.Embed(color=0xff9900, title='Играет история')  
    embed.add_field(name='', value=f'Играет история: {named}', inline=False)  
    #await ctx.send(embed=embed)
    message = await ctx.send(embed=embed)
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
    await message.add_reaction('❌')

@bot.command()
async def calledback(ctx):
    print(named)
    
    await ctx.send("Отработка")
    
@bot.command()
async def storyes(ctx: commands.Context):
    await ctx.send("Выбери", view=StoryView())
    
@bot.command()
async def quick(ctx: commands.Context):
    voice = discord.utils.get(bot.voice_clients)
    await voice.disconnect()

bot.run(TOKEN)