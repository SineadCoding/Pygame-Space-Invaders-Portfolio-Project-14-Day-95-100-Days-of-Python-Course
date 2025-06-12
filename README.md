# Pygame-Space-Invaders-Portfolio-Project-14-Day-95-100-Days-of-Python-Course
My (single level) version of the classic arcade game Breakout using Pygame.

This is a custom implementation of the classic Space Invaders game built with Pygame. It features pixel-style graphics, alien animations, player lives, and a score system. The objective is to shoot down all invading aliens before running out of rockets.

https://github.com/user-attachments/assets/a4849a7b-9992-466d-8b59-1ca3d9d30601
![Screenshot 2025-06-12 101439](https://github.com/user-attachments/assets/f9cf6e71-9c6e-4d17-b315-e34984a8c132)

Features:
Classic side-to-side alien movement with shooting capabilities
Player-controlled rocket with bullet firing
Multiple rocket lives and a life tracking system
Dynamic alien shooting intervals
Destructible blocks for cover
Score system with display
![Screenshot 2025-06-12 101655](https://github.com/user-attachments/assets/bf85ba5f-571f-452e-9914-e50d34534ca3)

Game over and victory screens with replay option:
https://github.com/user-attachments/assets/d2a2a100-57f1-442e-b282-a5e40aa19a7f

Requirements:
Python 3.7+
Pygame library
Install Pygame via pip if you haven't already

File Structure:
main.py: Main game logic
content/: Folder containing all required assets (background, alien sprites, rocket, bullets, blocks, etc.)

How to Run:
Ensure your working directory contains main.py and a content/ folder with all necessary images. Then run:

Controls:
Left Arrow: Move rocket left
Right Arrow: Move rocket right
Spacebar: Fire bullet

Notes:
The game resets on loss or victory when the replay button is clicked
The alien movement reverses direction when they hit screen bounds
Alien firing is randomized within a time interval
