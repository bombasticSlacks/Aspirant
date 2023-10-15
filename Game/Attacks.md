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
When you attack something, your range is how far you can engage them from. With melee weapons, you need to be within 2m. With Range, Thrown, and Magic you have a range, but it is possible to attack up to 5x your range, but you will suffer [Distance Penalty](#Distance%20Penalty). #TODOMovement 
* Magic attacks have a range of 10m
* Thrown have a range of 3 times your [Strength](Strength)
* Ranged attacks will be defined in the weapons [traits](Weapons#[Weapon-Traits](Weapon-Traits)).

### Attacking
- Declare what weapon you are using
- Make sure you are within range (or figure out what your total penalty will be) 
- Determine any bonuses or negatives you have on the attack.
- Declare any modifiers you are applying to the attack.
- Roll a skill test. If you fail this test, the attack fails.
- If your attack doesn’t target a specific location, roll the hit location dice to determine where you hit.
- Your opponent can at this point attempt to avoid your attack if they would like to and have a reaction available. If they avoid, the attack fails.
- You compare the penetration value on your attack to the armour value of the limb you are trying to hit (this will be covered in depth later in this chapter). If you fail to penetrate, the attack fails.
- Roll a d6, add any relevant damage bonuses, and consult the damage chart for what corresponding injury they will take.

### Combat Modifiers
These are modifiers you can apply to attacks and manoeuvres which will put you at a negative to the skill test but will make the attack or manoeuvre do additional things. Several other powerful modifiers can be learned by taking specific combat training. 

#### Called Shot
Your attack has a guaranteed hit location. -2 for arm or leg shots, -1 for chest shots, -3 for head shots.

#### Difficult Hit
You make your attacks harder to predict and therefore harder to avoid. You can give yourself a -1, -3 or -5 to your skill test to give your opponent a similar negative to any reactions.
#### Reposition
before making a melee attack or manoeuvre, you can move to a different side of your opponent. Puts the attack/manoeuvre at a -1.

#### Heavy Strike
Your attack does 1 additional damage. The penalty for this is variable, see [Calculating Damage](#Calculating%20Damage).

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

### Dealing Damage
Generally, a weapon or attack will already have a calculated [Calculating Damage](#Calculating%20Damage) it causes. A weapon will have a damage value written as follows: "X(Y)". What this means is that the weapon does X damage, and you could take a negative on the [Attack](Terminology#Attack) to cause it to do 1 additional damage.

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


