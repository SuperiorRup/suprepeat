# Work with Python 3.6

import asyncio
import discord
from discord.ext.commands import Bot

Mike = Bot('+')

@Mike.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    return await Mike.say(mesg)

Mike.run('NTQyNjQ5MjA0MTQxNDU3NDA5.DzxFYA.U6-42w6Yftv6COYALUuWLmye2SA')



