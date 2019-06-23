import discord
import asyncio
from discord.ext import commands
import spellgen

f = open('token.txt', 'r')
Token = f.read()
client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.upper().startswith("!STOP"):
        await client.logout()
    if message.content.upper().startswith("!PING"):
        await client.send_message(message.channel, 'Pong!')
    if message.content.upper().startswith("!SPELL"):
        try:
            say_args = message.content.split(" ")
            level = say_args[-1]
            return_list = spellgen.spell(level)
            msg = ''
            no_spell = ''
            spell_info = ''
            try:
                spell_header = '\n————-Spell————-'
                spell_info = ('\nSpell Name: {spell_name}\nSpell Level: {spell_level}\nSpell Duration: {spell_duration}'
                              '\nSpell Range: {spell_range}\nSpell Description: {spell_desc}'.format(
                                spell_name=return_list[1], spell_level=return_list[2], spell_duration=return_list[3],
                                spell_range=return_list[4], spell_desc=return_list[5]))
            except IndexError:
                no_spell = '\nNo spell selected'
                pass
            finally:
                wild_header = '\n\n———-Wild-Magic———-'
                wild_info = ('\nyou rolled {wild_roll} for wild magic:\n{effect}'.format(wild_roll=return_list[0][0],
                                                                                effect=return_list[0][1]))
                msg = (spell_header + spell_info + no_spell + wild_header + wild_info)
                await client.send_message(message.channel, msg)
        except:
            await client.send_message(message.channel, 'Did you input the command in the following format:'
                                                       '\n !spell [level]')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(Token)

# msg = 'Hello {0.author.mention}'.format(message)
# # await client.send_message(message.channel, msg)