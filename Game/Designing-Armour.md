---
layout: default
title: Designing Armour
parent: Armour
grand_parent: Equipment
nav_order: 2
---
# Designing [Armour](Core/Armour)
Through play and when creating a character, you may desire to protect yourself with armour. You can use one of the [Example-Armour](Example-Armour) or design your own. Perhaps your village or character has a unique type of armour, or you encounter a blacksmith who has an idea for a unique piece of armour. 

To build a piece of armour:
- Choose the [Quality](#Quality)
- Choose [Materials](#Materials)
- Calculate the [Base Armour Value](#Base%20Armour%20Value)
- Spend your [Crafting Points](#Crafting%20Points)

## Quality
Armour comes in various qualities based on the skill required to craft.
### Basic
Basic armour is improvised, hastily constructed, or primitive in nature, but may save your life when no other options are available. 
* Use a single material of at least [Artisan](Materials#Artisan) quality.
* Has the stats of [Basic-Armour](Game/Gear/Basic-Armour)


### Artisan

Artisan armour is expressly built for the hardships of battle. When compared to basic armour, artisan armour is more complex and more meticulously constructed, often with specific functions in mind.
* Use 2 materials, at least 1 of which is [Artisan](Materials#Artisan).
* Have 1 [Crafting Points](#Crafting%20Points).
* May take 1 [Tradeoffs](#Tradeoffs)

### Exotic

Exotic armours incorporate additional complexity of both materials and design allowing for further specialization of enhanced functionality thanks to the use of rare and advanced materials and expert craftsmanship.
* Use 2 materials, at least 1 of which is [Exotic](Materials#Exotic).
* Have 2 [Crafting Points](#Crafting%20Points).
* May take 1 [Tradeoffs](#Tradeoffs)

### Master Work

Master worked armour is an artisan or exotic armour of exceptional craftsmanship and design. 
* A piece of masterwork armour gains 1 additional [Crafting Points](#Crafting%20Points)
* May take 2 [Tradeoffs](#Tradeoffs). 
* Must include at least one additional [Exotic](Materials#Exotic) material in its construction.

### Relic
Armours that go beyond what could be possible with enchanting or standard craftsmanship can be considered relics. They may still be crafted, but would require more narrative investment then a simple skill roll.


## Materials
Armour is made of [Materials](Materials), which determine its characteristics, see [Materials](Core/Armour#Materials) for more details. Artisan or Exotic [Quality](Core/Armour#Quality) armour will require a small amount of secondary material to reinforce, pad, or affix the primary material to. 

### Material Table
This is a list of the base values an armour with each material might have.

| Material                  | Skill Penalty | Integrity | Weakness                              |
| ------------------------- | ------------- | --------- | ------------------------------------- |
| [Textiles](Game/Textiles) | (+1)          | 2         | [Rending](Game/Core/Injury#Rending)   |
| [Hide](Game/Hide)         | (+1)          | 2         | [Impact](Game/Core/Injury#Impact)     |
| [Bits](Game/Bits)         | (0)           | 3         | [Piercing](Game/Core/Injury#Piercing) |
| [Liquid](Game/Liquid)     | (-1)          | 4         | [Life](Game/Core/Injury#Life)         |
| [Metal](Game/Metal)       | (-1)          | 4         | [Cold](Game/Core/Injury#Cold)         |
| [Resonant](Game/Resonant) | (0)           | 2         | -                                     |
| [Flora](Game/Flora)       | (0)           | 3         | [Heat](Game/Core/Injury#Heat)         |

> Some armour concepts are obvious, such as metal, textiles and hide. Consider liquid to be things like epoxy, oil quenching, chemical treatments. Bits to be, bone, quills, feathers, living rock. Resonant to be crystals, powders and gemstones. Flora to be vines, woods and roots. 


### Base Armour Value
 The base attributes for a suit of armour is as follows;

| Attribute         | Calculation         |
| ----------------- | ------------------- |
| Skill Penalty     | Primary + Secondary |
| Integrity         | Primary + Secondary |
| Weakness          | Primary Weakness    |
| Critical Weakness | Secondary Weakness  |
| Resistance        | -                   |

> So an armour with a primary material of metal and a secondary of textiles would result in having a skill penalty of 0, an integrity of 6, and a weakness to rending damage.

### Tradeoffs
Some armour sacrifces in one way to gain power in another. For each tradeoff you do you gain an additional [Crafting Points](#Crafting%20Points). Tradeoffs are (can be selected more than once):
- Gain 2 [Critical Weakness](Game/Core/Armour#Critical%20Weakness)
- Make a [Critical Weakness](Game/Core/Armour#Critical%20Weakness) into a [Weakness](Game/Core/Armour#Weakness%20and%20Resistance)
- Reduce [Armour Integrity](Game/Core/Armour#Armour%20Integrity) by 2
- Increase [Skill Penalty](Game/Core/Armour#Skill%20Penalty) by 1.


### Crafting Points
 Can be spent to further modify armour. Per crafting point you can (each selectable more than once):
 * Add an [Armour-Traits](Game/Core/Armour-Traits) that can be justified based on the armour.
 * Add 2 [Armour Integrity](Game/Core/Armour#Armour%20Integrity).
 * Reduce [Skill Penalty](Game/Core/Armour#Skill%20Penalty) by 1.
 * Remove 2 [Critical Weakness](Game/Core/Armour#Critical%20Weakness)
 * Make a [Weakness](Game/Core/Armour#Weakness%20and%20Resistance) into a [Critical Weakness](Game/Core/Armour#Critical%20Weakness)
 * Gain a [Resistance](Game/Core/Armour#Weakness%20and%20Resistance) and a [Critical Weakness](Game/Core/Armour#Critical%20Weakness)



 
## Crafting
A character looking to craft a specific armour requires relevant training as a [Craftsman](Craftsman), requires 2 size worth of the primary material, and 1 size worth of secondary material where applicable. Other bits, unless narratively relevant, are a negligible portion of the cost. Then, the character, as [Production Work](Activities#Production%20Work), may spend a day crafting. If they succeed on the [Application](Core/Intelligence#Application) test, the item is created successfully. If not, they must try again in the future; however, materials are not lost, just time. 

The difficulty of the test is modified as follows:

* Exotic Materials -1
* Traits -1 per each
* Poor facilities -1
* Excellent facilities +1