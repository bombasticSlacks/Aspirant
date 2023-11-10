---
layout: default
title: Monster Actions
parent: Monsters
grand-parent: Running The Game
nav_order: 2
---

## Monster Actions
This is a list of generic actions that are shared among monsters.

### Avoid(X)
*The monster avoids incoming damage using movement or tools.*

Reaction
{: .label }

* If an [Opponent](Terminology#Opponent) performs a [Successful Attack](Terminology#Successful%20Attack), you may perform a [Fixed Difficulty](Skills#Fixed%20Difficulty)(X). If you succeed, you ignore the effects of the attack unless otherwise specified.

### Attack(X, Y, Z)
*The monster strikes out, harming an enemy.*

Attack
{: .label }

* If you succeed a [Fixed Difficulty](Skills#Fixed%20Difficulty)(X), you get a [Successful Attack](Terminology#Successful%20Attack) against the [Opponent](Terminology#Opponent), this attack deals Z [Damage](Terminology#Damage), and has a [Types of Damage](Injury#Types%20of%20Damage) of Y.

> Attack(3, [Impact](Injury#Impact), 2) is an attack at a +3 to succeed, that deals 2 impact damage.


### Ranged Attack(X, Y, Z, R)
*The monster launches a long ranged strike.*

Attack
{: .label }

* If you succeed a [Fixed Difficulty](Skills#Fixed%20Difficulty)(X), you get a [Successful Attack](Terminology#Successful%20Attack) against the [Opponent](Terminology#Opponent), this attack deals Z [Damage](Terminology#Damage), and has a [Types of Damage](Injury#Types%20of%20Damage) of Y. It has a [Range](Weapons#Range) of R.

> Attack(3, [Impact](Injury#Impact), 2, [Short](Movement#Short)) is an attack at a +3 to succeed, that deals 2 impact damage at a range of short.


### Grapple(X)
*The monster lunges for a grab, trying to control you.*

Attack
{: .label }

* The monster performs a [Grapple](Special-Combat-Actions#Grapple).

### Shove(X, Y)
*The monster throws its weight at you, sending you flying.*

Attack
{: .label }

* The monster performs a [Shove](Special-Combat-Actions#Shove).