---
layout: default
title: Attacks
parent: Combat
nav_order: 2
grand_parent: Telling The Story
---

## Attacking
Usually, in combat, you will be trying to harm your opponents with the goal of killing or disabling them. Attacks will typically be:
* Thrown attacks using [Athletics](Strength#Athletics)
* Ranged attacks using [Accuracy](Agility#Accuracy)
* Melee attacks using [Strike](Strength#Strike) 
* Magic attacks using [Will](Spirit#Will)

### Attack Range
When you attack something, your range is how far you can engage them from. 
* If a weapon doesn't specify a range it is assumed you need to be within [Reach](Movement#Reach).
* If you aren't within a weapons range you can either [Move](Combat-Turn#Move), or suffer a [Distance Penalty](Attack-Bonuses#Distance%20Penalty), or perhaps, both.
* Magic generally has a range of [Close](Movement#Close).
* Items can be thrown [Close](Movement#Close).
* Ranged attacks will be defined in the weapons [traits](Weapons#[Weapon-Traits](Weapon-Traits)).

### Attacking
- Declare what weapon you are using
- Make sure you are within range (or figure out what your total penalty will be) 
- Determine any bonuses or negatives you have on the attack.
- Declare any modifiers you are applying to the attack.
- Roll a skill test. If you fail this test, this is a [Mitigated Attack](Terminology#Mitigated%20Attack).
- Your [Opponent](Terminology#Opponent) can use a [Reaction](Terminology#Reaction).
- Your [Opponent](Terminology#Opponent) [Takes Damage](#Taking%20Damage)

### Critical Hits
If an [Attack](Terminology#Attack) is a [Critical Success](Skills#Critical%20Success) it deals +1 [Damage](Terminology#Damage).

### Combat Modifiers
These are modifiers you can apply to attacks and manoeuvres which will put you at a negative to the skill test but will make the attack or manoeuvre do additional things. Several other powerful modifiers can be learned by taking specific combat training. 

#### Difficult Hit
*Action modifier (-1, -3, -5)*

You make your attacks harder to predict and therefore harder to avoid. You can give yourself a -1, -3 or -5 to your skill test to give your opponent a similar negative to any reactions.

#### Heavy Strike
*Action modifier varies*

Your [Attack](Terminology#Attack) does 1 additional [Damage](Terminology#Damage). The penalty for this is variable, see [Calculating Damage](#Calculating%20Damage).

#### Reposition
*Action modifier (-1)*

before making a melee attack or manoeuvre, you can move to a different side of your opponent.

#### Vitals Hit
*Action modifier (-2)*

Your [Attack](Terminology#Attack) strikes a person's vitals. An [Attack](Terminology#Attack) that rolls [Doubles](Skills#Doubles), is always considered a vitals hit.


---
### Calculating Damage
When you attack with a weapon it will deal an amount of damage, this is calculated as follows:

| Damage Bonus | Damage | Heavy Strike Penalty |
| ------------ | ------ | -------------------- |
| 1-5          | 1      | $Damage\ Bonus - 6$    |
| 6-10         | 2      | $Damage\ Bonus - 11$    |
| 11-15        | 3      | $Damage\ Bonus - 16$    |
| 16+          | 4      | -                    | 

Damage bonus usually includes your Strength, along with bonuses from the item you are wielding, this value generally doesn't change. You should also figure out what your [Heavy Strike](#Heavy%20Strike) penalty is.

> So if a character with 3 strength wields a melee weapon with a damage bonus of 5, they have a total damage bonus of 8. This means that their weapon deals 2 damage and their [Heavy Strike](#Heavy%20Strike) penalty is (-3).

### Taking Damage
If you fail to mitigate an incoming attack, you will take damage.
[Armour](Armour) is your first line of defence against attacks. Your armour provides you with a small amount of [Armour Integrity](Armour#Armour%20Integrity) which can absorb incoming damage. 

* Adjust incoming damage based on if you have [Weakness and Resistance](Armour#Weakness%20and%20Resistance) to the attack.
* Deduct incoming damage from your [Armour Integrity](Armour#Armour%20Integrity).
* Any remaining damage is converted to an [Injury](Injury).

> Example, if your character takes 3 damage from a piercing attack while wearing armour weak to piercing with 2 [Armour Integrity](Armour#Armour%20Integrity). Your character's Armour Integrity is reduced to 0, with 2 damage still left unaccounted for you take a [Severe Injury](Injury#Severe%20Injury).


