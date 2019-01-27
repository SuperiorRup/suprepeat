# Work with Python 3.6

import asyncio
import discord
from discord.ext.commands import Bot

Mike = Bot('+')

@Mike.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    return await Mike.say(mesg)

Mike.run('NTM3NTgyMzAxMzEyMzE5NDkw.Dy68_A.ZbHplVBXgdVKXa2Kgfo_h4Y30tI')



