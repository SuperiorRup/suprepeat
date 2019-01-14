# Work with Python 3.6

import asyncio
import discord
from discord.ext.commands import Bot

Mike = Bot('+')

@Mike.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    return await Mike.say(mesg)

Mike.run('NTI4NTA0MzMyMjYyMzA5ODg4.DwoIKQ.P9HY47BQ3wD5BtZz3JH6kUzOtwA')



