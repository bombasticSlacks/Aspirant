---
layout: default
title: Undead
grand_parent: Running The Game
nav_order: 2
has_children: false
parent: Characters
---
# Undead
{: .no_toc }
The unliving, otherworldly, and cursed living dead.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## Fodder

---

Fodder
{: .label .label-green }
### The Hungry
*Corpse cursed with unlife after being preyed upon by another human while starving. Teeth click together as it gnaws at nothing, bony appendages with large chunks of flesh missing, seeming to have been bitten or ripped away. Necrotic ooze holds the creature barely together.*

| Initiative | Move                          | Threat | Integrity | Weakness | Resistance |
| ---------- | ----------------------------- | ------ | --------- | -------- | ---------- |
| 2          | [Close](../Core/Movement.md#Close) | 2      | -         | -        | -          |

* [Attack(3, Rending, 1)](../Core/Character-Actions.md#Attack(X,%20TYPE,%20DAMAGE))
* [Phobia(Sunlight)](../Core/Character-Actions.md#Phobia(FEAR))

#### Rewards
{: .no_toc }
* Knawed insides: 1 size [Basic Bits](../Bits#Basic%20Bits).

---

## Elite

---
Elite
{: .label .label-yellow }
### The Full
*Corpse cursed with unlife after performing the blasphemous act of devouring its allies. Its maw hangs open widely, dripping necrotic ooze. Portions of its body seem to have been reinforced with chunks of almost tumorous flesh.*

| Initiative | Move                          | Threat | Integrity | Weakness | Resistance |
| ---------- | ----------------------------- | ------ | --------- | -------- | ---------- |
| 3          | [Close](../Core/Movement.md#Close) | 4      | 3         | Magic    | Physical   |

* [Attack(5, Impact, 2)](../Core/Character-Actions.md#Attack(X,%20TYPE,%20DAMAGE))
* [Phobia(Sunlight)](../Core/Character-Actions.md#Phobia(FEAR))

Trait
{: .label .label-purple }
#### Crumbling Flesh
{: .no_toc}
*The creature's flesh is separate with large gushing streams of black ooze infecting everything nearby.*
* On taking [Damage](../Core/Terminology.md#Damage) for every damage taken up to one character in [Reach](../Core/Movement.md#Reach), determined randomly, takes 2 damage. Defeated undead can be selected for this ability and if targeted are revived at full power.

#### Rewards
{: .no_toc }
* Oozing stomach: 1 size of [Artisan Bits](../Bits#Artisan%20Bits).

---
## Boss

---
Boss
{: .label .label-red }
### The Cardinal
*A large corrupted religious figure draped in red, where a head should be a large burning red hand rests instead.*

| Initiative | Move                          | Threat | Integrity | Weakness                  | Resistance                |
| ---------- | ----------------------------- | ------ | --------- | ------------------------- | ------------------------- |
| 3,3        | [Close](../Core/Movement.md#Close) | 3      | 6         | [Life](../Core/Injury.md#Life) | [Heat](../Core/Injury.md#Heat) |

* [Avoid(4)](../Core/Character-Actions.md#Avoid(X))
* [Attack(5, Impact, 2)](../Core/Character-Actions.md#Attack(X,%20TYPE,%20DAMAGE))
* [Ranged Attack(5, Heat, 3, Short)](../Core/Character-Actions.md#Ranged%20Attack(X,%20TYPE,%20DAMAGE,%20RANGE))

Reaction
{: .label .label-yellow }
#### Rich Blood
{: .no_toc }
*The air around the cardinal wreaks with an almost maddening scent that can stop you dead in your tracks.*
* When a target moves within [Reach](../Core/Movement.md#Reach) of The Cardinal, they must succeed an [Identity](../Core/Spirit.md#Identity) [Fixed Difficulty](../Core/Skills.md#Fixed%20Difficulty)(0) or end their turn. This effect persists until The Cardinals next [Combat Turn](../Core/Terminology.md#Combat%20Turn).

Trait
{: .label .label-purple }
#### The Sun's Gaze
{: .no_toc }
*You've ripped the hand apart, but something is underneath!*
* This effect only happens once The Cardinal is at 0 integrity.
* Anyone [Close](../Core/Movement.md#Close) to The Cardinal at the end of its [Combat Turn](../Core/Terminology.md#Combat%20Turn) suffers a 1 [Damage](../Core/Terminology.md#Damage) [Heat](../Core/Injury.md#Heat) [Vitals](../Core/Injury.md#Vitals) [Injury](../Core/Injury.md) that can be mitigated by armour.
* The [Injury-Effects](../Core/Injury-Effects.md) is scorched lungs leaving the [Character](../Core/Terminology.md#Character) unable to breath and [Stunned](../Core/Effects.md#Stunned).
* If you suffer this injury twice in a row you are [On Fire](../Core/Effects.md#On%20Fire).

#### Rewards
{: .no_toc }
* Burning coal: [Exotic Resonant](../Resonant#Exotic%20Resonant).

---

