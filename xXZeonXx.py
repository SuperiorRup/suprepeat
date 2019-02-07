import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import json
import aiohttp
from discord.utils import get
from random import choice, shuffle

commandprefix = "+"
client = commands.Bot(command_prefix=commandprefix)
client.remove_command('help')

async def status_task():
    while True:
       await client.change_presence(game=discord.Game(name="Watch Dogs X"))
       await asyncio.sleep(5)
       await client.change_presence(game=discord.Game(name="Epic Games"))
       await asyncio.sleep(5)
       await client.change_presence(game=discord.Game(name="Fortnite"))
       await asyncio.sleep(5)
       await client.change_presence(game=discord.Game(name="Superior's Videos"))
       await asyncio.sleep(5)
       await client.change_presence(game=discord.Game(name="By +Help"))
       await asyncio.sleep(5)
       await client.change_presence(game=discord.Game(name="Nothing"))
       await asyncio.sleep(5)
       await client.change_presence(game=discord.Game(name='with '+str(len(set(client.get_all_members())))+' members'))
       await asyncio.sleep(3)
       await client.change_presence(game=discord.Game(name='in '+str(len(client.servers))+' servers'))
       await asyncio.sleep(3)

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Our BOT')
    print('Created by Superior Rup')
    client.loop.create_task(status_task())


@client.command(pass_context=True)
async def Zeon(ctx):
    await client.say("Yes!")
    print ("reply Posted")
@client.command(pass_context = True)
async def ping(ctx):
        embed=discord.Embed(title="**PONG!**", description="Command Accepted!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    return await client.say(mesg)
@client.command(pass_context = True)
async def invite(ctx):
        embed=discord.Embed(title="**Our Server Link**", description="https://discord.gg/CrMKHMb".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context=True)
async def totalmembers(ctx):
        embed=discord.Embed(title="**TOTAL MEMBERS OF {0.name}**", description="MEMBERS- {0.member_count}".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def zeonyt(ctx):
        embed=discord.Embed(title="**HERE IS THE LINK OF SUPERIOR RUP CHANNEL**", description="https://www.youtube.com/channel/UCguNIP794svRhgGTAWE7JDg?view_as=subscriber".format(ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def zeonlink(ctx):
        embed=discord.Embed(title="**HERE IS THE LINK OF ZEON**", description="https://discordapp.com/oauth2/authorize?client_id=542649204141457409&scope=bot&permissions=2146958591".format(ctx.message.author), color=0xff00f6)
        await client.say(embed=embed) 
@client.command(pass_context = True)
async def Help(ctx):
        embed=discord.Embed(title="**New**", description="**join**\n**zeonlink**\n**adminhelp**\n**say**\n**botinfo**\n**ping**\n**invite**\n**join\n**zeonyt**\n** - coming soon...**\n****".format(ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def botinfo(ctx):
        embed=discord.Embed(title="**INFORMATIONS OF Zeon**", description="**Name-ZEON**\n**Creator- Superior Rup**\n**Official Server- ZEON**\n**Bot Type- Public**\n**Discord.py**".format(member, ctx.message.author), color=0x7289da)
        await client.say(embed=embed)
        print ("helped")        
@client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        await client.kick(userName)
        embed=discord.Embed(title="**User Kicked Successfully!**", description="**The User was successfully Kicked!**".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="**User unmuted!**", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def purge(ctx, number):
 if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
    mgs = [] 
    number = int(number) 
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="**User muted!**", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def clearwarn(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="**Warning Cleared!!**", description="Warning of **{0}** was cleared by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)   
@client.command(pass_context = True)
async def warn(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="**User Warned!**", description="**{0}** was warned **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def ban(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        await client.ban(userName)
        embed=discord.Embed(title="**User Banned Successfully!**", description="**The User was successfully Banned!**".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def unban(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        await client.unban(userName)
        embed=discord.Embed(title="**User Banned Successfully!**", description="**The User was successfully Banned!**".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context=True)
async def hack(ctx,user: discord.Member=None,*,hack=None):
    nome = ctx.message.author
    if not hack:
        hack = 'discord'
    else:
        hack = hack.replace(' ','_')
    channel = ctx.message.channel
    x = await client.send_message(channel, '``[▓▓▓                    ] / {}-Starting Hacking Tool.``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓                ] - {}-Starting Hacking Tool..``'.format(hack))
    await asyncio.sleep(0.3)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {}-Hacking Tool Started...``'.format(hack))
    await asyncio.sleep(1.2)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {}-Starting to hack.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {}-Searching fb password..``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {}-Searching discord password.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {}-Almost Done...``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``Showing Results {}- Discord Hacker``'.format(hack))
    await asyncio.sleep(2)
    x = await client.edit_message(x,'``Downloading File  |``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Downloading File..  /``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Downloading File... -``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Downloading File....\``')
    await client.delete_message(x)
    await client.delete_message(ctx.message)
        
    if user:
        await client.say('`I Found This:-\n FB password-887755hug \n Discord password- 9785661adhs \n '.format(hack,user.name))
        await client.send_message(user,'**Alert!**\n``You may have been hacked.``'.format(hack))
    else:
        await client.say('**{}** has hacked himself ¯\_(ツ)_/¯.'.format(name.name))
        await client.send_message(name,'**Alert!**\n``You may have been hacked..``'.format(hack))

client.run('NTQyNjQ5MjA0MTQxNDU3NDA5.Dz1cCQ._4DCD2erG2KY0-cdUQ6U8C1WhsI')


