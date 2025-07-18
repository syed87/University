# Math Equation Game
A simple educational Python program that helps users practice solving algebraic equations.

## Overview
The Math Equation Game is an interactive program designed to help students practice basic algebra. The game presents simple equations where players must solve for the unknown variable 'x'. It's perfect for students learning algebra, teachers looking for practice tools, or anyone wanting to sharpen their mental math skills. The program generates random multiplication equations in the format a × x = b, where 'a' and 'b' are known numbers, and the player must determine the value of 'x'.

## Requirements
To run this game, you need:

A computer (Windows, Mac, or Linux) Python 3.9 or higher installed Basic ability to use a command line or terminal

Open your command prompt (Windows) or terminal (Mac/Linux) Type python --version or python3 --version Press Enter

If Python is installed, you'll see something like Python 3.12.7. If not, visit python.org to download and install it.

## Getting Started
Step 1: Download the Game

Download the TaskOne.py file to your computer

Step 2: Opem file in VS code

Run the file inside VS code, this will open the terminal and start the game

## How to Play
When you run the program, you'll see:

Welcome to the Math Equation Game! Solve 5 equations.

The game will present 5 equations, one at a time. Each equation looks like:

Question 1: 3 × x = 12 What is x?

When the game ends you'll see:

Game Over! Your score: 4/5

## Program Structure
The program consists of four main functions that work together:

generate_equation()

Creates random multiplication problems Generates two random numbers (1-10) Calculates the result Returns the equation components

display_equation(coefficient, result)

Shows the equation to the user Formats it as "a × x = result" Provides clean visual presentation

get_user_answer()

Handles user input Validates that input is a number Keeps asking until valid input received Includes error handling for non-numeric input

play_game()

Main game controller Manages game flow and scoring Loops through 5 questions Displays final results
