---
layout: default
title: Combat
parent: Telling The Story
nav_order: 2
has_children: true
---

## Combat
Combat in Aspirant is more structured than standard narrative time, since it is also more high stakes. Combat is broken up into [Combat Rounds](Terminology#Combat%20Round). During which, you will get a [Combat Turn](Terminology#Combat%20Turn) to do things.

### Initiative Value
Initiative value is your [Initiative](Stats#Initiative)+ 1d6. Your initiative value determines what order people will perform their [Combat Turn](Terminology#Combat%20Turn) during the [Combat Round](Terminology#Combat%20Round). So even though all characters are acting simultaneously in combat, as an abstraction, people still go in a specific order.

---

### Hit Locations
Hit locations are usually simplified to head, body, arms, legs.

To randomly determine a hit location, you should roll a d12 and consult the following chart.

| D12  | Location |
| ---- | -------- |
| 1-4  | Chest    |
| 5-8  | Arms     | 
| 9-11 | Legs     |
| 12   | Head     |

### Armour and Penetration
When someone is being attacked, to determine what effect the attack has, you check if the incoming damage type is either a weakness or resistance of the armour:

| Attack is: | Armour Integrity Damage |
| ---------- | ----------------------- |
| Weakness   | 4                       |
| Normal     | 2                       |
| Resistance | 1                       | 

#### Compromised Armour
Once your armour integrity goes to 0, your armour is considered compromised. It no longer provides any protection, and any attacks you take [Deal Damage](#Dealing%20Damage).

#### Partially Compromised
Any time you would remove armour integrity, your armour isn't compromised, but you don't have the full required amount, your armour's integrity is reduced to 0, but your opponent's attack is a [Glancing Blow](#Glancing%20Blow).

> A character with two armour integrity taking a normal attack reduces their armour integrity to 0 but is otherwise unharmed.

> A character with 2 armour integrity taking a weakness attack (4 integrity damage) reduces their armour integrity to 0 and takes an injury. The opponent rolls and determines the injury is a [Severe Injury](Injury#Severe%20Injury), but since the characters armour was only [Partially Compromised](#Partially%20Compromised) they take a [Minimal Injury](Injury#Minimal%20Injury) instead. Their armour is now [Compromised](#Compromised%20Armour).

#### Resistance
As an additional benefit, if you are resistant to an attack it always counts as a [Glancing Blow](#Glancing%20Blow).

### Dealing Damage
When you or something else is attempting to injure someone you will in most cases roll 1d6 + damage modifier. Damage modifier is a combination of the weapons inherent lethality, size, any bonuses from your character and usually, your [Strength](Strength). 

This number is usually compared to the universal damage chart to determine the injury caused:

| Roll  | Injury   |
| ----- | -------- |
| 1-5   | Minimal  |
| 6-10  | Severe   |
| 11-15 | Critical |
| 16+   | Lethal   |

> So, for example, a long sword (3 size artisan weapon) wielded by a character with 3 [Strength](Strength) would have a damage bonus of 7 (1 artisan + 3 size + 3 [Strength](Strength)). That means on a 1-3 it causes a severe injury, on a 4-6 it causes a critical injury. 

#### Glancing Blow
Sometimes your attacks will be partially mitigated by abilities or other circumstances. When this happens you reduce the severity of your injury by one.

> So a [Critical Injury](Injury#Critical%20Injury) glancing blow becomes a [Severe Injury](Injury#Severe%20Injury).

### Types of Damage
Generally, there are two large categories of damage – Physical and Otherworldly, each of these then further has three categories of damage.

Physical injuries can consist of:
#### Rending
tearing and cutting flesh.
#### Piercing
Stabbing and piercing flesh.
#### Impact
Slamming into and breaking flesh .

---

Otherworldly injuries can consist of:
#### Life
Poison, acid, and rot ravage the body, destroying life itself.
#### Heat
Heat, power, holy energy ravage the body 
#### Cold
Ice, chill, vampiric energy ravage the body

---

### Area Of Effect
In general, most things will only target a single person, however if something (such as a spell) refers to a square or cone of damage. A 9m square means a square with a side length of 9m. You would choose where you want it and if you miss your attack it scatters in a random direction equal to the number you failed by in meters. Determine what direction it scatters at random.

### Being in Melee Combat
If you perform a melee attack (whether it’s successful) on an enemy or they perform an attack on you (whether it’s successful) then you are both considered in melee. Anyone who performs a melee attack on anyone in a melee joins the melee. During a melee, narratively your characters are moving around and connecting weapons, though mechanically your character is rooted in place. Any time you attempt to move, back out, or cautious step you are no longer in the melee, but this may cause people to hurt you as you stop defending to escape. While in a melee, if the enemies are outnumbered you get a +1 on all combat rolls related to the melee and if they are outnumbered more than 2 to 1 you get a +2.

While in melee, you are at a negative to use ranged weapons equal to the largest enemy threat. 

### Being in Cover
If there is an object of some kind between yourself and an opponent, you count as “in cover”. This provides you with protection from incoming attacks.

If you are behind cover and not attacking or otherwise doing something it is assumed, you are fully covered. Anyone shooting at you gets a -2 as you are not visible, and your entire body is protected by the cover.

If you are shooting from behind cover unless you have some special abilities you require your dominant arm chest and head exposed. When you are shot when you determine hit location if any of those locations are targeted you are hit normally otherwise your cover protects you. You may opt to blind fire while in cover which is a ranged attack at -4 but only requires your dominant arm to be outside cover.

You do not gain the benefits of cover if you are in melee.

If you are protected by cover, any attack against you must first penetrate the cover to be able to harm you (this stacks with your armour). Most pieces of cover only have 1 armour integrity and will be unable to protect you after the first shot.