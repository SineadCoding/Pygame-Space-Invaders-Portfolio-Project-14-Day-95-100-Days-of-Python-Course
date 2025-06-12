# Pygame Space Invaders Portfolio Project 14 Day 95 100 Days of Python Course
My (single level) version of the classic arcade game Breakout using Pygame.

This is a custom implementation of the classic Space Invaders game built with Pygame. It features pixel-style graphics, alien animations, player lives, and a score system. The objective is to shoot down all invading aliens before running out of rockets.

https://github.com/user-attachments/assets/6632fe65-bf77-494c-aaa7-238e754b5167

#

![Screenshot 2025-06-12 101439](https://github.com/user-attachments/assets/f45928c4-38ab-4e2e-bb13-65a2de550a0a)

Features:

Classic side-to-side alien movement with shooting capabilities

Player-controlled rocket with bullet firing

Multiple rocket lives and a life tracking system

Dynamic alien shooting intervals

Destructible blocks for cover

Score system with display



Game over and victory screens with replay option:

https://github.com/user-attachments/assets/6d1d035f-c174-4b82-aa70-46de2b908800

#

Requirements:

Python 3.7+

Pygame library

Install Pygame via pip if you haven't already

#

File Structure:

main.py: Main game logic

content/: Folder containing all required assets (background, alien sprites, rocket, bullets, blocks, etc.)

#

How to Run:

Ensure your working directory contains main.py and a content/ folder with all necessary images. Then run:

#

Controls:

Left Arrow: Move rocket left

Right Arrow: Move rocket right

Spacebar: Fire bullet

#

Notes:

The game resets on loss or victory when the replay button is clicked

The alien movement reverses direction when they hit screen bounds

Alien firing is randomized within a time interval
