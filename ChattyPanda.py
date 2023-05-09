import os
import discord
from discord_slash import SlashCommand, SlashContext

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

@slash.slash(name="hello", description="Says hello to the user")
async def hello(ctx: SlashContext):
    await ctx.send(f"Hello, {ctx.author.mention}!")

client.run(os.environ["DISCORD_TOKEN"])



