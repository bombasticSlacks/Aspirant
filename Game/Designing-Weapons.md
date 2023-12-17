---
layout: default
title: Designing Weapons
parent: Weapons
grand_parent: Equipment
nav_order: 2
---
# Designing [Weapons](Core/Weapons.md)
Through play and when creating a character, you may be asked to select a weapon. You can use one of the [Example-Weapons](Example-Weapons) or design your own. Perhaps your character hales from a distant land which uses a unique weapon, or a blacksmith has an idea for a specialized weapon for your character's fighting style. 

To build a weapon:
- Choose the [Quality](#Quality).
- Choose a [Size](Core/Weapons.md#Size).
- Select a [Damage Type](Core/Weapons.md#Damage%20Type).
- Include the [[]]
- Select a number of [Weapon Traits](Core/Weapon-Traits.md) for the weapon equal to the amount available based on [Quality](#Quality).

## Quality
Weapons come in a variety of qualities based on the skill required to craft.
### Basic
Basic weapons are simple tools, improvised items, rudimentary weapons or other implements not built intentionally for harm.
* -1 [Damage Bonus](Core/Weapons.md#Damage%20Bonus)
* 0 [Weapon Traits](Core/Weapon-Traits.md)

### Artisan
Artisan weapons are properly built tools of war. They require some training to use properly and have unique advantages over using a basic weapon.
* +1 [Damage Bonus](Core/Weapons.md#Damage%20Bonus)
* 1 [Weapon Traits](Core/Weapon-Traits.md)

### Exotic
Exotic weapons have additional complexity over basic artisan weapons. Their mechanisms are more complex or their chance of self injury is higher. They require additional training on top of the training required for artisan weapons to be used successfully. To wield an exotic weapon, you need [Exotic Expert](Combat-Training#Exotic%20Expert).
* +1 [Damage Bonus](Core/Weapons.md#Damage%20Bonus)
* 2 [Weapon Traits](Core/Weapon-Traits.md)

### Master Work
A masterful blacksmith can do a lot to imbue an item with additional power and versatility. 
* A masterwork weapon has +1 [Weapon Traits](Core/Weapon-Traits.md). 
* It must be made of materials of similar quality to an exotic weapon.

## Material
Generally, weapons material isn’t particularly important. Cheap materials will not be usable for artisan weapons, simple but quality materials will not be usable for exotic/master worked weapons. [Costs Of Materials](Services#Costs%20Of%20Materials) has details on the crafting capacity and cost of different materials.

One benefit to exotic materials, however, is their potential for harming monsters. A sword made of silver might be known to harm werewolves, a spear made from elven wood is effective against wraiths, etc. In some exceptional cases, a material may provide a trait for free, increase damage bonus, or provide some skill bonus. 

## Default Traits
By default, all weapons have:
* [Strength](Core/Weapon-Traits.md#Strength).
* [Size Matters](Core/Weapon-Traits.md#Size%20Matters).

## Calculating Damage Bonus
A weapons damage bonus is equal to:
$traits + quality$

> A [Size](Core/Weapons.md#Size) 3 [Artisan](#Artisan) weapon, with the [Lethal](Core/Weapon-Traits.md#Lethal) [Weapon Trait](Core/Weapon-Traits.md) would have a damage bonus of 8, 6 from [Size Matters](Core/Weapon-Traits.md#Size%20Matters), 1 from [Artisan](#Artisan), 1 from [Lethal](Core/Weapon-Traits.md#Lethal).

## Crafting
A character looking to craft a specific weapon first requires 2x the size worth of materials and [Craftsman](Craftsman) training saying they are able to make what they want. 

> So, a silver sword of size 3 would require 6 size worth of pure silver, or 60 silver coins. 

Other bits, unless narratively relevant, are a negligible portion of the cost. Then, the character, as [Production Work](Activities#Production%20Work), may spend a day crafting. If they succeed on the [Application](Core/Intelligence.md#Application) test, the item is created successfully. If not, they must try again in the future, however materials are not lost, just time. 

The difficulty of the test is modified as follows:
* Traits -1 per each
* Exotic Materials -1
* Poor facilities -1