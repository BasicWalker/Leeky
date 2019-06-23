# Create virtual environment using venv
```
cd Leeky/
python3 -m venv ./venv
```

# Get into virtual environment (venv)
```
cd Leeky/
*linux*
source ./venv/bin/activate
*windows*
venv\Scripts\activate
```
*should return*
>`(venv) pi@raspberrypi:~/git/Leeky $ `


**check python interpreter and pip location**

*linux*: `which pip3` should return 
>`/Leeky/venv/bin/pip3`

*windows*: `where pip` should return 
>`\Leeky\venv\Scripts\pip.exe `

*linux*: `which python` should return 
>`/Leeky/venv/bin/python`

*windows*: `where python` should return 
>`\Leeky\venv\Scripts\python.exe`


# Install dependencies
make sure loaction is set in the `Leeky/` folder and the (venv) is active.

run `pip install -r requirements.txt`

**check if dependencies are installed correctly**

`pip list` should return a list of 3rd-party dependencies required for this project

# Using spellgen.py module
## for standalone 
use enter the command:
`python spellgen.py`
then input spell level
>`Input highest spell level available: 3 `
>
this should return something like this

>————-Spell————- 
>
>Spell Name: Hellish Rebuke 
>
>Spell Level: 1     
>
>Spell Duration: Instantaneous 
>
>Spell Range: 60 feet   
>
>Spell Description: You point your finger, and the creature that damaged you is momentarily surrounded by hellish flames. The creature >must make a Dexterity saving throw. It takes 2d10 fire damage on a failed save, or half as much damage on a successful one.  
>
>———-Wild-Magic———-         
>
>you rolled 0 for wild magic:    
>
>extreme! You gain the service of an arcane sword that does not require concentration until your next short or long rest.

## as a module 
import using
`import spellgen` 

`spellgen.spell(level)` returns a list of
>`[[wild], spell_name, spell_level, spell_duration, spell_range, spell_desc]`

**wild list** contains wild magic information as :
>`[wild_roll, str(severity: effect)]`

if needed `spellgen.wildmagic(spell_level)` can also be called seperately to return the **wild list**.

## discord bot
the discord bot take the command `!spell [level]` and outputs a formatted spellgen.spell(level) post to the channel where the command was sent

