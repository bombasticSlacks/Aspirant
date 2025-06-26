---
layout: default
title: Character Development
has_children: true
parent: Telling The Story
---

# Character Development

As you adventure, your character will become stronger. This can happen in a number of ways. When completing quests, you will gain XP. XP in this game stands for “Experience Potential”. During [Downtime](Telling-The-Story#Downtime), you can convert XP into character development, whether it be increased skills or new training.

When you rest, based on the length of the rest, you will have time which could be spent training. Spending XP to train is either a [downtime activity](Activities#Downtime%20Activity) or [travel activity](Activities#Travel%20Activity).

## Learning

Aside from inherent progression, the experts of the world have much to teach your character. As you travel you should learn everything you can spending your XP to gain new [Skills](Core/Skills) and [Training](#Training).

You can learn using:

- [Supervised Training](Activities#Supervised%20Learning).
- [Night Training](Activities#Night%20Learning).
- [Socialize](Activities#Socialize).

When you learn something, it will either be [Unknown](#Unknown), [In Progress](#In%20Progress), [Known](#Known).

### Requirements

A character can’t learn from nothing. When your character desires to learn something [Unknown](#Unknown), a person needs to be paid for [Teaching](Services#Teaching), or they need a [Training Manual](Game/Example-Gear#Training%20Manual). Either way, they will also need to have XP available to spend.

### Unknown

A skill or training is considered unknown if you haven't spent any XP towards learning it.

### In Progress

A skill or training is considered in progress if you have spent some XP, but not the required amount to learn it.

### Known

A skill or training is considered known if you have spent the required XP on it. At this point you benefit from it.

## Progression

As your characters gain [Total XP](Game/Blocks/Total-XP) you gain additional benefits beyond your [Learning](#Learning). These are called [Character-Milestones](Character-Milestones) and you receive them as follows:

| [Total XP](Game/Blocks/Total-XP) | Reward                                                            |
| -------------------------------- | ----------------------------------------------------------------- |
| 10                               | [Basic Milestones](Character-Milestones#Basic%20Milestones)       |
| 15                               | [Basic Milestones](Character-Milestones#Basic%20Milestones)       |
| 20                               | [Basic Milestones](Character-Milestones#Basic%20Milestones)       |
| 25                               | [Advanced Milestones](Character-Milestones#Advanced%20Milestones) |
| 30                               | [Advanced Milestones](Character-Milestones#Advanced%20Milestones) |
| 35                               | [Advanced Milestones](Character-Milestones#Advanced%20Milestones) |

## Training

Basic, advanced, and master training represents powerful new abilities that your character can learn to possess. Trainings can either be:

- Passive - just does something all the time for you.
- Elective - gives you a new ability/option you can use at will.
- Power Based - Requires spending [Power](Game/Core/Blocks/Power) to activate.
- Once Per Downtime - Very powerful abilities that can only be used once before resting in a city.

### Training Tiers
Training can be split into 
#### Basic
Basic training should fundamentally be known by any practitioners of the training school.

#### Advanced
Advanced training should be known only be those with experience, but should still be relatively ubiquitous. Taking an Advanced training requires already having a [Basic](#Basic) training in the [Training School](#Training%20School).

#### Master
Master level trainers should be rare and not readily available. A master should be a person of notoriety, and gaining training from them should require more than just an exchange of [Currency](Core/Equipment#Currency). Taking a master training should require already having a [Advanced](#Advanced) training in the [Training School](#Training%20School).

### Types Of Training
There are a number of standard character archetypes and group archetypes you will run into in Aspirant. These will make up the bulk of training you can learn and have available. Some characters and groups will notably fit into more than one of these archetypes, in that case they could teach trainings from any school they fit into.

They fit into two broad categories:
#### Discipline
A discipline is a fully fleshed out school of training. Progression in a discipline will look like this:
```mermaid
flowchart LR
	B[Basic]
	A1[Advanced]
	A2[Advanced]
	A3[Advanced]
	M[Master]
    B --> A1
    B --> A2
    B --> A3
    A1 --> M
    A2 --> M
    A3 --> M
```

#### Concept
A concept is a more streamlined idea, which you can obtain a basic idea of and then refine over time. Progression in a concept looks like this:
```mermaid
flowchart LR
	B[Basic]
	A1[Advanced]
    B --> A1
```

### Training School
This is a perhaps non-exhaustive list of 
#### Weapons Enthusiast
*More than just some fighter, you are a hobbyist with an interest in the workings of weapons and using them very effectively.*
#### Hunter
*A master of defeating an enemy with preparation. You believe knowledge is power when it comes to defeating an enemy.*
#### Knight
*A master of armour and defense, a knight knows how to move well in heavy armour.*
#### Commander
*Leaders with the expertise to support and coordinate their allies.*
#### Assassin
*A master of killing and stealth, specializing in using small weapons to kill.*
#### Paladin
*Holy warriors filled with faith and hope.*
#### Mercenary
*Soldiers of fortune who believe in overwhelming odds to gain victory.*
#### Arcanist
*Masters of imbuing the arcane into everything around them.*
#### Crafter
*Experts in creating things out of materials.*
#### Dyamist
*Experts in changing energy and elements, and how it flows all around us.*
#### Mystic
*Those who commune with the other side. Perceivers of things unseen.*
#### Shaper
*Sorcerers that shape the world around them.*
#### Healer
*Those who use science or superstition to cure the sick and wounded.*
#### Spymaster
*Those who shape the world from the shadows.*

- [Academic](Academic)
- [Brawler](Brawler)
- [Labourer](Labourer)

- [Rogue](Rogue)
- [Shaper](Shaper)
- [Star](Star)
- [Wanderer](Wanderer)
