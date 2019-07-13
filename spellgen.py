import json
import random
import csv
# -----

# collects specified spell class spells from spells.json and adds them to spell_list
spell_list = dict()
spell_list['spell'] = []
with open('spells.json') as json_file:
    full_spell_list = json.load(json_file)
    for spell in full_spell_list:
        for tag in spell['tags']:
            if tag == 'wizard' or tag == 'sorcerer' or tag == "warlock":
                spell_list['spell'].append(spell)

extreme = []
moderate = []
nuisance = []
# collects extreme, moderate, and nuisance effects from wild-magic csv and assign respective lists
with open('wild_magic.csv', 'r', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        extreme.append(line[0].replace('\xa0', ' '))
        moderate.append(line[1].replace('\xa0', ' '))
        nuisance.append(line[2].replace('\xa0', ' '))

confusion = {
    1: "The creature uses all its Movement to move in a random direction. To determine the direction, roll a d8 and assign a direction to each die face. The creature doesn't take an action this turn.",
    2: "The creature doesn't move or take Actions this turn.",
    3: "The creature doesn't move or take Actions this turn.",
    4: "The creature doesn't move or take Actions this turn.",
    5: "The creature doesn't move or take Actions this turn.",
    6: "The creature doesn't move or take Actions this turn.",
    7: "The creature uses its action to make a melee Attack against a randomly determined creature within its reach. If there is no creature within its reach, the creature does nothing this turn.",
    8: "The creature uses its action to make a melee Attack against a randomly determined creature within its reach. If there is no creature within its reach, the creature does nothing this turn.",
    9: "The creature can act and move normally.",
    10: "The creature can act and move normally."
}


def wildmagic(spell_level):
    """
    determines wild magic outcome based on input spell level
    :param spell_level:
    :return [wild_roll, str(severity! effect)]:
    """
    # checks if roll meets wild-magic thresh (d20 - spell_level <= 5)
    spell_level_num = int(spell_level)
    d20 = random.randrange(1, 20)
    wild_roll = (d20 - spell_level_num)
    if wild_roll <= 5:
        # random 1-20: 1-3/extreme 4-9/moderate, 10-20/nuisance
        severity = random.randrange(1, 20)
        effect_roll = random.randrange(100)
        if severity <= 3:
            effect = 'extreme! ' + extreme[effect_roll]
            return [wild_roll, effect]
        elif 9 >= severity > 3:
            effect = 'moderate! ' + moderate[effect_roll]
            return [wild_roll, effect]
        else:
            effect = 'nuisance! ' + nuisance[effect_roll]
            return [wild_roll, effect]
    else:
        return [wild_roll, "no wild magic effect"]


def spell(level, combat_flag):
    """
    take input level, then if if spell level > 0 return random spell info and wild magic outcome,
    else return wild magic outcome
    :param level, combat_flag:
    :return [[wild], spell_name, spell_level, spell_duration, spell_range, spell_desc]:
    """

    combat_schools = ["transmutation", "necromancy", "evocation", "enchantment", "abjuration", "conjuration" ]
    noncombat_schools = ["transmutation", "necromancy", "illusion", "enchantment", "divination", "conjuration"]
    if str(combat_flag) == "c":
        # collects specified spell levels from spell_list and adds them to spell_choices
        spell_choices = dict()
        spell_choices['spell'] = []
        spell_level_list = list(range(1, int(level)+1))
        for spell in spell_list['spell']:
            if spell['level'] in str(spell_level_list) and spell["school"] in str(combat_schools):
                spell_choices['spell'].append(spell)
        # finds total amount of spells in spell_choices
        total_len = len(spell_choices['spell'])
        # generates random int from 0 to total_len and stores spell dict
        random_spell = spell_choices['spell'][random.randrange(total_len)]
        spell_name = (random_spell['name'])
        spell_level = (random_spell['level'])
        spell_school = (random_spell['school'])
        spell_duration = (random_spell['duration'])
        spell_range = (random_spell['range'])
        spell_desc = (random_spell['description'])
        wild = wildmagic(spell_level)
        return [wild, spell_name, spell_level, spell_duration, spell_range, spell_desc, spell_school]
    elif str(combat_flag) == "nc":
        # collects specified spell levels from spell_list and adds them to spell_choices
        spell_choices = dict()
        spell_choices['spell'] = []
        spell_level_list = list(range(1, int(level)+1))
        for spell in spell_list['spell']:
            if spell['level'] in str(spell_level_list) and spell["school"] in str(noncombat_schools):
                spell_choices['spell'].append(spell)
        # finds total amount of spells in spell_choices
        total_len = len(spell_choices['spell'])
        # generates random int from 0 to total_len and stores spell dict
        random_spell = spell_choices['spell'][random.randrange(total_len)]
        spell_name = (random_spell['name'])
        spell_level = (random_spell['level'])
        spell_school = (random_spell['school'])
        spell_duration = (random_spell['duration'])
        spell_range = (random_spell['range'])
        spell_desc = (random_spell['description'])
        wild = wildmagic(spell_level)
        return [wild, spell_name, spell_level, spell_duration, spell_range, spell_desc, spell_school]
    else:
        # collects specified spell levels from spell_list and adds them to spell_choices
        spell_choices = dict()
        spell_choices['spell'] = []
        spell_level_list = list(range(1, int(level)+1))
        for spell in spell_list['spell']:
            if spell['level'] in str(spell_level_list):
                spell_choices['spell'].append(spell)
        # finds total amount of spells in spell_choices
        total_len = len(spell_choices['spell'])
        # generates random int from 0 to total_len and stores spell dict
        random_spell = spell_choices['spell'][random.randrange(total_len)]
        spell_name = (random_spell['name'])
        spell_level = (random_spell['level'])
        spell_school = (random_spell['school'])
        spell_duration = (random_spell['duration'])
        spell_range = (random_spell['range'])
        spell_desc = (random_spell['description'])
        wild = wildmagic(spell_level)
        return [wild, spell_name, spell_level, spell_duration, spell_range, spell_desc, spell_school]


def known(level):
    """
    take known spell input level, then runs wild magic outcome and confusion outcome,
    :param level:
    :return [[wild], level, d20_known, d10_known, confusion_effect]:
    """
    wild = wildmagic(level)
    d20_known = random.randrange(1,20)
    d10_known = random.randrange(1,10)
    if int(d20_known) == 1 or int(d20_known) == 2:
        d10_known = random.randrange(1,10)
        confusion_effect = confusion[int(d10_known)]
        return [wild, level, d20_known, d10_known, confusion_effect]
    else:
        confusion_effect = "No confusion!"
        return [wild, level, d20_known, d10_known, confusion_effect]
    

if __name__ == '__main__':
    level = input('Input highest spell level available: ')
    return_list = spell(level)
    try:
        print('\n————-Spell————-')
        print('Spell Name: {spell_name}\nSpell Level: {spell_level}\nSpell School: {spell_school}\n'
        'Spell Duration: {spell_duration}\nSpell Range: {spell_range}\n'
        'Spell Description: {spell_desc}\n'.format(
                spell_name=return_list[1], spell_level=return_list[2], spell_duration=return_list[3],
                spell_range=return_list[4], spell_desc=return_list[5], spell_school=return_list[6]))
    except IndexError:
        print('No spell selected')
        pass
    finally:
        print('———-Wild-Magic———-')
        print('you rolled {wild_roll} for wild magic:\n{effect}'.format(wild_roll=return_list[0][0],
                                                                       effect=return_list[0][1]))








