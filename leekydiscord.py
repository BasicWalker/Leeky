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
    if message.content.upper().startswith("!HELP"):
        await client.send_message(message.channel, 'type ![command] [parameter 1] [parameter 2],...\n\n'
        'commands are:\n\n!stop : Stops bot\n\n!ping : bot response test\n\n'
        '!random [combat flag] [level] :returns a random spell up to level parameter of the combat'
        ' flag parameter type, with wild magic outcome\n combat flag can be "combat" or "c", "noncombat" or "nc", all)\n level can be an integer up to the highest spell available'
        '\n\n!known [level] '
        ':returns wild magic outcome and confusion outcome ')
    if message.content.upper().startswith("!RANDOM"):
        try:
            say_args = message.content.split(" ")
            level = say_args[-1]
            combat_flag = say_args[-2].upper()
            if combat_flag == "COMBAT" or combat_flag == "C":
                return_list = spellgen.spell(level,"c")
                try:
                    spell_header = '\n————-Spell————-'
                    spell_info = ('\nSpell Name: {spell_name}\nSpell Level: {spell_level}\nSpell School: {spell_school}\n'
                    'Spell Duration: {spell_duration}\nSpell Range: {spell_range}\n'
                    'Spell Description: {spell_desc}'.format(
                    spell_name=return_list[1], spell_level=return_list[2], spell_duration=return_list[3],
                    spell_range=return_list[4], spell_desc=return_list[5], spell_school=return_list[6]))
                    wild_header = '\n\n———-Wild-Magic———-'
                    wild_info = ('\nyou rolled {wild_roll} for wild magic:\n{effect}'.format(wild_roll=return_list[0][0],
                                                                                    effect=return_list[0][1]))
                    msg = (spell_header + spell_info)
                    msg2 = (wild_header + wild_info)
                except IndexError:
                    msg = '\nNo spell selected'
                    msg2 = ''
                    pass
                except:
                    msg = "\nSomething Wonky happened with the spells"
                    msg2 = ''
                finally:
                    if len(msg) > 1700:
                        msg_split_1 = msg[:1700]
                        msg_split_2 = msg[1700:]
                        await client.send_message(message.channel, msg_split_1)
                        await client.send_message(message.channel, msg_split_2)
                        await client.send_message(message.channel, msg2)
                    else:
                        await client.send_message(message.channel, msg)
                        await client.send_message(message.channel, msg2)

            elif combat_flag == "NONCOMBAT" or combat_flag == "NC":
                return_list = spellgen.spell(level,"nc")
                try:
                    spell_header = '\n————-Spell————-'
                    spell_info = ('\nSpell Name: {spell_name}\nSpell Level: {spell_level}\nSpell School: {spell_school}\n'
                    'Spell Duration: {spell_duration}\nSpell Range: {spell_range}\n'
                    'Spell Description: {spell_desc}'.format(
                    spell_name=return_list[1], spell_level=return_list[2], spell_duration=return_list[3],
                    spell_range=return_list[4], spell_desc=return_list[5], spell_school=return_list[6]))
                    wild_header = '\n\n———-Wild-Magic———-'
                    wild_info = ('\nyou rolled {wild_roll} for wild magic:\n{effect}'.format(wild_roll=return_list[0][0],
                                                                                    effect=return_list[0][1]))
                    msg = (spell_header + spell_info + wild_header + wild_info)
                except IndexError:
                    msg = '\nNo spell selected'
                    pass
                except:
                    msg = "\nSomething Wonky happened with the spells"
                finally:
                    await client.send_message(message.channel, msg)
            else:
                return_list = spellgen.spell(level,"all")
                try:
                    spell_header = '\n————-Spell————-'
                    spell_info = ('\nSpell Name: {spell_name}\nSpell Level: {spell_level}\nSpell School: {spell_school}\n'
                    'Spell Duration: {spell_duration}\nSpell Range: {spell_range}\n'
                    'Spell Description: {spell_desc}'.format(
                    spell_name=return_list[1], spell_level=return_list[2], spell_duration=return_list[3],
                    spell_range=return_list[4], spell_desc=return_list[5], spell_school=return_list[6]))
                    wild_header = '\n\n———-Wild-Magic———-'
                    wild_info = ('\nyou rolled {wild_roll} for wild magic:\n{effect}'.format(wild_roll=return_list[0][0],
                                                                                    effect=return_list[0][1]))
                    msg = (spell_header + spell_info + wild_header + wild_info)
                except IndexError:
                    msg = '\nNo spell selected'
                    pass
                except:
                    msg = "\nSomething Wonky happened with the spells"
                finally:
                    await client.send_message(message.channel, msg)
        except:
            await client.send_message(message.channel, 'Did you input the command in the following format:'
                                                       '\n !spell [combat flag] [level]')
    if message.content.upper().startswith("!KNOWN"):
        say_args = message.content.split(" ")
        try:
            level = say_args[-1]
            msg = ''
            return_list = spellgen.known(level)
            wild_header = '\n\n———-Wild-Magic———-'
            wild_info = ('\nyou rolled {wild_roll} for wild magic:\n{effect}'.format(wild_roll=return_list[0][0],
                                                                                    effect=return_list[0][1]))
            confusion_header = "\n————-confusion————-"
            confusion_info = ('\nyou rolled {d20_known} for confusion:\n{confusion_effect}'.format(d20_known=return_list[2],
                                                                                        confusion_effect=return_list[4]))
            msg = (confusion_header + confusion_info + wild_header + wild_info)
        except:
            msg = "something went wrong"
        finally:
            await client.send_message(message.channel, msg)




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(Token)
