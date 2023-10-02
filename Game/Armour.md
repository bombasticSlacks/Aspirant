---
layout: default
title: Armour
parent: Equipment
nav_order: 2
has_children: true
---
## Armour
Armour [Equipment](Equipment) is your character's safety net. It is designed to protect against only a small amount of high-powered attacks. However, advanced armour can be almost impervious to simpler weapons. Armour will protect certain locations on your body. A suit of armour together has shared integrity, but separate details for each location it protects on your body. Some armours will stack, such as shields and energy fields. If you have multiple valid armour sources, you can choose to use whichever you want (though only 1 per attack).

### Locations
Armour is separated into 4 distinct sections. Head, Torso, Arms, Legs.

### Materials
Armour is made of specific [materials](materials) which have 4 distinct attributes: Weakness, Resistance, Structure, Max Skill. To function as protection, a piece of armour must be made of at least [Artisan](Materials#Artisan) quality materials even if it is of a Basic design. Materials also influences which [Armour-Traits](Armour-Traits) are available for Artisan and Exotic armours.

#### Max Skill
affects different locations separately and is the maximum bonus you can have on related skill tests before negatives are applied. 

| Location | Skills effected                                |
| -------- | ---------------------------------------------- |
| Head     | [Insight](Intelligence#Insight), and [Connection](Communication#Connection)    |
| Arms     | [Strike](Strength#Strike), [Accuracy](Agility#Accuracy), and [Will](Spirit#Will)|
| Torso    | *No Penalties*                                 |
| Legs     | [reflexes](Agility#Reflexes), [Grace](Agility#Grace)                                               |

#### Weakness and Resistance
Changes how certain [types of damage](Combat#Types%20of%20Damage) effect you. If a piece of armour would gain a resistance or weakness complementary to an existing Resistance or Weakness on the armour through [Armour-Traits](Armour-Traits), the two cancel out resulting in no effect. If a piece of armour would gain a resistance or weakness it already has through [Armour-Traits](Armour-Traits), there is no effect. See [Armour and Penetration](Combat#Armour%20and%20Penetration) for details. 

#### Structure
Contributes to your overall armours integrity. Allowing it to take more hits before becoming non-functional.

### Quality
Armour can come in a variety of qualities. Higher quality armours gain access to [Armour-Traits](Armour-Traits) as well as the ability to incorporate additional [materials](materials) into their design. [Designing Armour](Designing-Armour) has more details on the specifics.

### Armour Integrity
Your overall suit of armour will have an armour integrity, which is how well it all comes together to protect you. In other words, your armour suit has a shared amount of health over all locations. To calculate your suit of armour's integrity, add the structure values of all your armour pieces together. 

Armour Integrity is calculated as $Structure \over 8$ rounded. You can also consult the table below.

| Total Structure | Armour Integrity |
| --------------- | ---------------- |
| 1-4             | 2                |
| 5-12            | 3                |
| 13-20           | 4                |
| 21-28           | 5                |
| 29+             | 6                |

> For example, a character with 4 pieces of leather gives 8 structure, that's one additional integrity, for integrity of 3 total.

> A character with 1 pieces of leather (2 structure) and 3 pieces of plate mail (6 each) has 20 total structure, that's 2 bonus integrity for an overall armour integrity of 4.

### Style
Characters shouldn’t be punished for dressing their characters in a specific way that doesn’t describe perfect protection. The most obvious, however dated, example is a chain mail bikini. Though silly and perhaps not something players would be comfortable with, if it is in your game, it counts as fully functional armour with similar weaknesses to any other armour of similar material. Players and, in most cases, NPC characters should not have their narrative armour exploited.  

This extends to hats and helmets as well. Many players love the idea of a hero with their hair flowing in the wind and a perfect smile as they rush into battle. This vision doesn’t need to conflict with having a protected head. Characters could have headbands, thinly framed helmets, or even a high coif / scarf. These give the impression of head armour without giving up the vision of a hero.

### Acquiring Armour
* [Purchased](Example-Armour)
* [Found through play](Equipment#Looting)
* [Crafted](Designing-Armour)
* Commissioned [Costs Of Services](Services#Costs%20Of%20Services)
