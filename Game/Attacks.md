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
When you attack something, your range is how far you can engage them from. With melee weapons, you need to be within 2m. With Range, Thrown, and Magic you have a range, but it is possible to attack up to 5x your range, but you will suffer [Distance Penalty](#Distance%20Penalty). 
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