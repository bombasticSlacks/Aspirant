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
- Select a number of [Armour Traits](Core/Armour-Traits) for the armour equal to the amount available based on [Quality](#Quality) and [Materials](#Materials)

## Quality
Armour comes in a variety of qualities based on the skill required to craft.
### Basic
Basic armour is improvised, hastily constructed, or primitive in nature, but may save your life when no other options are available. 
* Use a single material of at least [Artisan](Materials#Artisan) quality.
* Have 0 [Armour-Traits](Core/Armour-Traits).


### Artisan

Artisan armour is expressly built for the hardships of battle. When compared to basic armour, artisan armour is more complex and more meticulously constructed, often with specific functions in mind.
* Use 2 materials, at least 1 of which is [Artisan](Materials#Artisan).
* Have 1 [Armour-Traits](Core/Armour-Traits).

### Exotic

Exotic armours incorporate additional complexity of both materials and design allowing for further specialization of enhanced functionality thanks to the use of rare and advanced materials and expert craftsmanship.
* Use 2 materials, at least 1 of which is [Exotic](Materials#Exotic).
* Have 2 [Armour-Traits](Core/Armour-Traits).

### Masterwork

Master worked armour is an artisan or exotic armour of exceptional craftsmanship and design. 
* A piece of masterwork armour gains 1 additional trait point.
* May take a single [Armour-Trait](Core/Armour-Traits) it does not meet the material requirement for. 
* Must include at least one [Exotic](Materials#Exotic) material in its construction.


## Materials
Armour is made of [Materials](Materials), which determine its characteristics, see [Materials](Core/Armour#Materials) for more details. Artisan or Exotic [Quality](Core/Armour#Quality) armour will require a small amount of secondary material to reinforce, pad, or affix the primary material to. Materials, whether they be the primary or secondary material, will also provide access to material specific [Armour-Traits](Core/Armour-Traits) for Artisan and Exotic armours.

### Material Table
This is a list of the base values an armour with each primary material will have.
#TODO update machinery

| Material  | Skill Penalty | Integrity | Weakness | Resistance |
| --------- | ------------- | --------- | -------- | ---------- |
| Textile   | 0             | 1         | Heat     | -          |
| Leather   | 0             | 1         | Life     | -          |
| Wood      | (-1)          | 2         | Heat     | -          |
| Metal     | (-1)          | 2         | Cold     | -          |
| Machinery | (-1)          | 1         | Impact   | -          |

If a piece of armour would gain a resistance or weakness complementary to an existing Resistance or Weakness on the armour through [Armour-Traits](Armour-Traits), the two cancel out, resulting in no effect. If a piece of armour would gain a resistance or weakness it already has through [Armour-Traits](Armour-Traits), there is no effect. 

### Multiple Materials
 When multiple materials are used, one is treated as the primary material and the other as the secondary material. The armour's base attributes (Weakness, Resistance, Structure, and Max Skill) are determined by the primary material, while the secondary material represents the increase in complexity and robustness of higher quality gear.
 
## Crafting
A character looking to craft a specific armour requires relevant training as a [Craftsman](Craftsman), requires 3 size worth of the primary material, and 1 size worth of secondary material where applicable. Other bits, unless narratively relevant, are a negligible portion of the cost. Then, the character, as [Production Work](Activities#Production%20Work), may spend a day crafting. If they succeed on the [Application](Core/Intelligence#Application) test, the item is created successfully. If not, they must try again in the future; however, materials are not lost, just time. 

The difficulty of the test is modified as follows:

* Exotic Materials -1
* Traits -1 per each
* Poor facilities -1
* Excellent facilities +1