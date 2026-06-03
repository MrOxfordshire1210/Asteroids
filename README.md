# Asteroids
A basic re-creation of the classic game 'Asteroids'. Developed through Boot.dev online course.

# How to Play
W - Move Forward
S - Move Backward
A - Turn Left
D - Turn Right
Space - Shoot

Destory the asteroids and try to stay alive for as long as possible

# Tech
Built within Python using Pygame

# Files
main.py - The Main Game
circleshape.py - Setup for players, asteroids and bullets
constants.py - game settings
player.py - player setup
asteroid.py - individual asteroid setup
asteroidfield.py - asteroid spawner and randomiser
shot.py - bullet setup

# How to play
Install Python 3.10 or newer
Create a virtual environment: python3 -m venv .venv
Activate the virtual environment:

    On Linux/Mac: source .venv/bin/activate
    On Windows: .venv\Scripts\activate

Install Pygame: pip install pygame==2.6.1
Run the game: python main.py

# Settings
Enter constants.py and change the values associated with the variables.
For example:
    PLAYER_SPEED (changes the speed in which the player moves) = 200 -> could be changed to 400 to be faster

# Possible Updates
Scoring System
Multiple Lives
Sound Effects
Death Effects


