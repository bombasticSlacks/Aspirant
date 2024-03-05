---
layout: default
title: Designing Weapons
parent: Weapons
grand_parent: Equipment
nav_order: 2
---
# Designing [Weapons](Core/Weapons)
Through play and when creating a character, you may be asked to select a weapon. You can use one of the [Example-Weapons](Example-Weapons) or design your own. Perhaps your character hales from a distant land which uses a unique weapon, or a blacksmith has an idea for a specialized weapon for your character's fighting style.

To build a weapon:
- Choose the [Quality](#Quality).
- Choose a [Size](#Size).
- Select a [Damage Type](#Damage%20Type).
- Spend any [Crafting Points](#Crafting%20Points).
- Do [Calculating Damage Bonus](#Calculating%20Damage%20Bonus).

## Quality
Weapons come in a variety of qualities based on the skill required to craft.
### Basic
Basic weapons are simple tools, improvised items, rudimentary weapons or other implements not built intentionally for harm.
* -1 [Damage Bonus](Game/Core/Weapons#Damage%20Bonus)
* 0 [Crafting Points](#Crafting%20Points)

### Artisan
Artisan weapons are properly built tools of war. They require some training to use properly and have unique advantages over using a basic weapon.
* +1 [Damage Bonus](Core/Weapons#Damage%20Bonus)
* 1 [Crafting Points](#Crafting%20Points)

### Exotic
Exotic weapons have additional complexity over basic artisan weapons. Their mechanisms are more complex or their chance of self injury is higher. They require additional training on top of the training required for artisan weapons to be used successfully. To wield an exotic weapon, you need [Exotic Expert](Combat-Training#Exotic%20Expert).
* +1 [Damage Bonus](Core/Weapons#Damage%20Bonus)
* 2 [Crafting Points](#Crafting%20Points)

### Master Work
A masterful blacksmith can do a lot to imbue an item with additional power and versatility. 
* A masterwork weapon has +1 [Crafting Points](#Crafting%20Points).
* It must be made of materials of similar quality to an [Exotic](#Exotic) weapon.

## Size
Weapons, like all items, come in various sizes. However, in the case of weapons, an item's size has more effect than just the required storage space. 
- A weapon's $size \times 2$ is added to its [Damage Bonus](Weapons#Damage%20Bonus)
- Weapons of size 1-2 have the [One-Handed](Game/Core/Blocks/One-Handed) trait.
- Weapons of size 3-4 have the [Two-Handed](Game/Core/Blocks/Two-Handed) trait.
- Weapons of size 5 have the [Impossibly-Large](Game/Core/Blocks/Impossibly-Large) trait.

> Examples of weapon sizes are as follows:
Size 1 - Dagger, hammer, knife
Size 2 - Arming Sword, Mace, Truncheon
Size 3 - Long sword, Warhammer, Spear
Size 4 - Lance, Great Sword
Size 5 - Giant Weapons

> So, for example, a long sword is a size 3 weapon. This means it is two-handed, gets +6 damage bonus.


## Damage Type
## Material
Generally, weapons material isn’t particularly important. Cheap materials will not be usable for artisan weapons, simple but quality materials will not be usable for exotic/master worked weapons. [Costs Of Materials](Services#Costs%20Of%20Materials) has details on the crafting capacity and cost of different materials.

One benefit to exotic materials, however, is their potential for harming monsters. A sword made of silver might be known to harm werewolves, a spear made from elven wood is effective against wraiths, etc. In some exceptional cases, a material may provide a trait for free, increase damage bonus, or provide some skill bonus. 

## Default Traits
By default, all weapons have:
* [Mass](Game/Core/Blocks/Mass)
* [Size-Matters](Game/Blocks/Size-Matters)

## Crafting Points
Can be spent to add either [Weapon-Traits](Game/Core/Weapon-Traits) or [Weapon-Templates](Game/Weapon-Templates) to your weapons. Traits must be negotiated with the [Game Master](Game/Core/Terminology#Game%20Master) but [Weapon-Templates](Game/Weapon-Templates) are designed to be added to weapons directly.

## Calculating Damage Bonus
A weapons damage bonus is equal to:
$traits + quality$

> A [Size](Core/Weapons#Size) 3 [Artisan](#Artisan) weapon, with the [Lethal](Core/Weapon-Traits#Lethal) [Weapon Trait](Core/Weapon-Traits) would have a damage bonus of 8, 6 from [Size Matters](Core/Weapon-Traits#Size%20Matters), 1 from [Artisan](#Artisan), 1 from [Lethal](Core/Weapon-Traits#Lethal).

## Crafting
A character looking to craft a specific weapon first requires the size + 1 worth of materials and [Craftsman](Craftsman) training saying they are able to make what they want. 

> So, a silver sword of size 3 would require 4 size worth of pure silver, or 40 silver coins. 

Other bits, unless narratively relevant, are a negligible portion of the cost. Then, the character, as [Production Work](Activities#Production%20Work), may spend a day crafting. If they succeed on the [Application](Core/Intelligence#Application) test, the item is created successfully. If not, they must try again in the future, however materials are not lost, just time. 