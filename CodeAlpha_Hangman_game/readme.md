# Hangman Game Using Python

## Project Overview

This project is developed as part of the CodeAlpha Python Programming Internship. The project focuses on creating a classic Hangman game using Python programming concepts.

The main objective of this project is to implement programming logic, user interaction, conditional statements, loops, and string handling to create an interactive word-guessing game.

## About Hangman Game

Hangman is a word guessing game where the player attempts to guess a hidden word by suggesting letters within a limited number of attempts.

In this project, the computer randomly selects a word, and the player has to guess the correct letters. For every incorrect guess, the number of remaining attempts decreases. The player wins by guessing the complete word before running out of attempts.

## Project Objectives

The main objectives of this project are:

- Develop a simple interactive game using Python
- Understand string manipulation
- Implement loops and conditional statements
- Generate random word selections
- Improve problem-solving skills

## Features

- Random word selection
- User input handling
- Letter guessing system
- Limited attempts for wrong guesses
- Display of guessed letters
- Win and lose conditions
- Interactive gameplay

## Technologies Used

- Python
- Random Module
- VS Code / PyCharm
- GitHub

## Python Concepts Used

- Variables and Data Types
- Conditional Statements
- Loops
- Functions
- Lists
- Strings
- User Input Handling
- Random Module

## Working of the Game

The Hangman game works using the following steps:

1. The program selects a random word from a predefined word list.
2. The selected word is hidden from the player.
3. The player enters one letter as a guess.
4. The program checks whether the guessed letter exists in the word.
5. If the guess is correct, the letter position is revealed.
6. If the guess is incorrect, the number of remaining attempts decreases.
7. The game continues until:
   - The player guesses the complete word (Win)
   - The player runs out of attempts (Lose)

## Project Structure

Hangman-Game

- hangman.py
- screenshots
- README.md

## How to Run the Project

1. Download or clone the repository.

2. Make sure Python is installed on your system.

3. Open the project folder in the terminal.

4. Run the Python file:

```bash
python hangman.py
