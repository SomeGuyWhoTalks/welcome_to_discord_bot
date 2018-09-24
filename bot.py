import discord
from discord.ext import commands
import asyncio


client = discord.Client()



newUserMessage = """

welcome to this server!

"""

@client.event
async def on_ready():
	print('logged in')
	print(client.user.name)
	print(client.user.id)
	print('-------------')

@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    await client.send_message(client.get_channel("CLient_ID"), newUserMessage)
    print("Sent message to " + member.name)

    role = discord.utils.get(member.server.roles, name="ROLE")
    await client.add_roles(member, role)

@client.event
async def on_message(message):
	if message.content.startswith('!hello'):
		await client.send_message(message.channel, 'hello')
		msg = await client.wait_for_message(author=message.author, content='Hello.')
		await client.send_message(message.channel, 'Hello.')

client.run('TOKEN')
