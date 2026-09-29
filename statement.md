# Treasure Hunt Game

## 1. Problem Statement

The **Treasure Hunt Game** is a Python-based interactive game designed to provide users with a simple text-based adventure experience.

In the game, the player starts from the **Library** and explores different locations such as the **Library, Laboratory, Garden, and Cave**. At each location, the player can search for clues and move to the next location. The objective is to collect clues and reach the Cave to find the hidden treasure.

The project provides an interactive environment where the player makes choices through keyboard input. The game also includes random events while moving between locations, making the gameplay more interactive.

---

## 2. Scope of the Project

The scope of the project is to develop a basic command-line treasure hunt game using Python programming concepts.

The project includes:

* A menu-driven interface for starting, getting help, or exiting the game.
* Multiple locations that the player can explore.
* A clue-searching mechanism.
* A movement mechanism between locations.
* Storage of collected clues.
* Random events during movement.
* Input validation for invalid choices.
* A winning condition when the player reaches the treasure.
* A counter for the total number of clues collected.
* An option to quit the game at any point.

The project is designed as a console-based application and does not require a graphical user interface or external database.

---

## 3. Target Users

The target users of this project are:

* Students learning Python programming.
* Beginners interested in understanding basic game development.
* Users who want to play a simple text-based adventure game.
* Students who want to understand how programming concepts can be combined to create an interactive application.

---

## 4. High-Level Features

### 4.1 Main Menu

The game provides a main menu with three options:

1. Play
2. Help
3. Quit

The player can select an option by entering the corresponding choice.

### 4.2 Player Name

At the beginning of the program, the player enters their name. The name is then used during the game to provide personalized messages.

### 4.3 Location-Based Exploration

The game contains four main locations:

* Library
* Laboratory
* Garden
* Cave

The player starts at the Library and progresses through the locations in sequence.

### 4.4 Clue Searching

At each location, the player can choose the **Search** option to discover a clue.

The discovered clues are stored so that the game can keep track of the clues collected by the player.

### 4.5 Movement System

The player can choose the **Move** option to travel to the next location.

The next location is determined according to the game's predefined room structure.

### 4.6 Random Events

When the player moves, the game generates a random number and displays a random event such as:

* Finding a shortcut
* A clear path
* Something unusual happening

This adds variety to the gameplay.

### 4.7 Treasure Discovery

The final location is the Cave. After reaching the treasure, the game displays a congratulatory message and shows the total number of clues collected.

### 4.8 Help and Instructions

The Help option provides instructions explaining how to:

* Go to locations
* Search for clues
* Collect clues
* Reach the Cave
* Exit the game

---

## 5. Python Concepts Used

The project demonstrates several basic Python programming concepts, including:

* Lists
* Tuples
* Sets
* Dictionaries
* Functions
* `if-elif-else` statements
* `while` loops
* User input
* Random number generation
* Dictionary access
* String formatting
* Basic program modularization

The project uses Python's `random` module to generate random events during movement.

---

## 6. Project Objective

The main objective of this project is to demonstrate how fundamental Python programming concepts can be combined to create an interactive command-line application.

The project focuses on applying programming concepts such as data structures, functions, loops, conditional statements, user input, and modules in a practical project.
