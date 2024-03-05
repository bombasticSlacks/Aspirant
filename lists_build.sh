#! /bin/bash
# builds all lists
python3 ./Game/Core/Scripts/lists.py Game/Core/Weapon-Traits.md Weapon-Traits Game/Core/Blocks
python3 ./Game/Core/Scripts/lists.py Game/Core/Weapon-Traits.md Weapon-Traits Game/Blocks
python3 ./Game/Core/Scripts/lists.py Game/Core/Armour-Traits.md Armour-Traits Game/Core/Blocks
python3 ./Game/Core/Scripts/lists.py Game/Weapon-Templates.md Weapon-Templates Game/Core/Blocks