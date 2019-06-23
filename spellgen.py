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
with open('wild_magic.csv', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        extreme.append(line[0].replace('\xa0', ' '))
        moderate.append(line[1].replace('\xa0', ' '))
        nuisance.append(line[2].replace('\xa0', ' '))


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


def spell(level):
    """
    take input level, then if if spell level > 0 return random spell info and wild magic outcome,
    else return wild magic outcome
    :param level:
    :return [[wild], spell_name, spell_level, spell_duration, spell_range, spell_desc]:
    """

    if int(level) > 0:
        # collects specified spell levels from spell_list and adds them to level_list
        level_list = dict()
        level_list['spell'] = []
        spell_level_list = list(range(1, int(level)+1))
        for spell in spell_list['spell']:
            if spell['level'] in str(spell_level_list):
                level_list['spell'].append(spell)
        # finds total amount of spells in level_list
        total_len = len(level_list['spell'])
        # generates random int from 0 to total_len and stores spell dict
        random_spell = level_list['spell'][random.randrange(total_len)]
        spell_name = (random_spell['name'])
        spell_level = (random_spell['level'])
        spell_duration = (random_spell['duration'])
        spell_range = (random_spell['range'])
        spell_desc = (random_spell['description'])
        wild = wildmagic(spell_level)
        return [wild, spell_name, spell_level, spell_duration, spell_range, spell_desc]
    else:
        return [wildmagic(0)]


if __name__ == '__main__':
    level = input('Input highest spell level available: ')
    return_list = spell(level)
    try:
        print('\n————-Spell————-')
        print('Spell Name: {spell_name}\nSpell Level: {spell_level}\nSpell Duration: {spell_duration}\n' 
              'Spell Range: {spell_range}\nSpell Description: {spell_desc}\n'.format(
                spell_name=return_list[1], spell_level=return_list[2], spell_duration=return_list[3],
                spell_range=return_list[4], spell_desc=return_list[5]))
    except IndexError:
        print('No spell selected')
        pass
    finally:
        print('———-Wild-Magic———-')
        print('you rolled {wild_roll} for wild magic:\n{effect}'.format(wild_roll=return_list[0][0],
                                                                       effect=return_list[0][1]))








