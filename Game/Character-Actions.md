---
layout: default
title: Character Actions
parent: Characters
grand_parent: Running The Game
nav_order: 0
---

# Character Actions
This is a list of generic actions that are shared among monsters.

## Avoid(X)
Reaction
{: .label .label-yellow }

*The monster avoids incoming damage using movement or tools.*

* If an [Opponent](Terminology#Opponent) performs a [Successful Attack](Terminology#Successful%20Attack), you may perform a [Fixed Difficulty](Skills#Fixed%20Difficulty)(X). If you succeed, you ignore the effects of the attack unless otherwise specified.

## Attack(X, TYPE, DAMAGE)
Attack
{: .label .label-red }

*The monster strikes out, harming an enemy.*

* If you succeed a [Fixed Difficulty](Skills#Fixed%20Difficulty)(X), you get a [Successful Attack](Terminology#Successful%20Attack) against the [Opponent](Terminology#Opponent), this attack deals DAMAGE [Damage](Terminology#Damage), and has a [Types of Damage](Injury#Types%20of%20Damage) of TYPE.

> Attack(3, [Impact](Injury#Impact), 2) is an attack at a +3 to succeed, that deals 2 impact damage.


## Ranged Attack(X, TYPE, DAMAGE, RANGE)
Attack
{: .label .label-red }

*The monster launches a long ranged strike.*

* If you succeed a [Fixed Difficulty](Skills#Fixed%20Difficulty)(X), you get a [Successful Attack](Terminology#Successful%20Attack) against the [Opponent](Terminology#Opponent), this attack deals DAMAGE [Damage](Terminology#Damage), and has a [Types of Damage](Injury#Types%20of%20Damage) of TYPE. It has a [Range](Weapons#Range) of RANGE.

> Attack(3, [Impact](Injury#Impact), 2, [Short](Movement#Short)) is an attack at a +3 to succeed, that deals 2 impact damage at a range of short.


## Grapple(X, OPPOSED)
Attack
{: .label .label-red }

*The monster lunges for a grab, trying to control you.*

* The monster performs a [Fixed Difficulty](Skills#Fixed%20Difficulty)(X) to [Grapple](Special-Combat-Actions#Grapple).
* The [Opposed Difficulty](Skills#Opposed%20Difficulty) penalty for dealing with the [Grapple](Special-Combat-Actions#Grapple) is OPPOSED.

## Shove(X, DISTANCE)
Attack
{: .label .label-red }

*The monster throws its weight at you, sending you flying.*

* The monster performs a [Shove](Special-Combat-Actions#Shove), moving a distance of DISTANCE.

## Phobia(FEAR)
Trait
{: .label .label-purple }

*This character is terrified of something.*

* When exposed to FEAR the creature is [Stunned](Effects#Stunned) for a [Combat Turn](Terminology#Combat%20Turn).
* After exposure, they will no longer be effected for the duration of the [Scene](Terminology#Scene)).

## Resistance(X)
Trait
{: .label .label-purple }

*This character has the will to refuse to die.*

* This character can become [Wounded](Effects#Wounded) as normal. 
* When trying to resist [Injury-Effects](Injury-Effects) they make a [Fixed Difficulty](Skills#Fixed%20Difficulty)(X - penalties).

## Eruption(RANGE, TYPE, DAM)
Attack
{: .label .label-red }

*The creature explodes in an area causing harm to all those around it and destroying itself in the process.*

* Everyone within RANGE of the creature suffers an [Attack](Terminology#Attack) of [Types of Damage](Injury#Types%20of%20Damage) TYPE and [Damage](Terminology#Damage) DAM.
* The creature is [Defeated](Effects#Defeated) in the process.
