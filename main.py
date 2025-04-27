"""
CSCI 128 Alien Invasion Revamped
Author: Weston Preising

Instructions:
1) pip install -r requirements.txt
2) python alien_invasion.py

Description:
The game was forked from https://github.com/ehmatthes/pcc_3e/tree/354813808eb999c0bcf7939904af582110f80aa7/solution_files/chapter_14/ex_14_5_high_score
I've added new modules, classes, functions and game logic to it.
You'll need pygame to run it

Changes made:
1) Added Use of WASD keys for left and right movement
2) Added y axis logic so the ship could go up and down; refactored arrow key / WASD for dual functionality
3) Changed to One Life Only
4) Added Gameover class to display gameover when game ends
5) added text_image_drawer helper function to be used for button and gameover classes
6) Add random alien fleet spawning logic
7) added halfway line to ensure ships and aliens don't spawn on each other

Textbook Resources:
1) Matthes, E. (2023). Python crash course: A hands-on, project-based introduction to programming. No Starch Press®.

Online Resources:
1) pygame key ref (https://www.pygame.org/docs/ref/key.html)
2) RGB Converter (https://www.w3schools.com/colors/colors_converter.asp)
3) RGB Dark red (https://www.rapidtables.com/web/color/red-color.html)
4) draw line (https://www.pygame.org/docs/ref/draw.html)
5) random numbers (https://docs.python.org/3/library/random.html)
6) pygame display (https://www.pygame.org/docs/ref/display.html)
"""

from alien_invasion import AlienInvasion

def main():
    ai = AlienInvasion()
    ai.run_game()
if __name__ == '__main__':
    main()
