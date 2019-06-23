# Create virtual environment using venv
```
cd Leeky/
python3 -m venv ./venv
```

# Get into virtual environment (venv)
```
cd Leeky/
source ./venv/bin/activate
```
*should return*
>`(venv) pi@raspberrypi:~/git/Leeky $ `


**check python interpreter and pip location**

`which pip3` should return 
>`/Leeky/venv/bin/pip3`

`which python` should return 
>`/Leeky/venv/bin/python`

# Using spellgen.py module
for standalone use enter the command:
`python spellgen.py`
then input spell level
>`Input highest spell level available: 3 `
>
this should return something like this
>
>`————-Spell————- 
>Spell Name: Hellish Rebuke 
>Spell Level: 1      
>Spell Duration: Instantaneous                                                                                           
>Spell Range: 60 feet                                                                                                    
>Spell Description: You point your finger, and the creature that damaged you is momentarily surrounded by hellish flames. The creature >must make a Dexterity saving throw. It takes 2d10 fire damage on a failed save, or half as much damage on a successful one.             
>———-Wild-Magic———-                                                                                                      
>you rolled 0 for wild magic:                                                                    
>extreme! You gain the service of an arcane sword that does not require concentration until your next short or long rest.
`
