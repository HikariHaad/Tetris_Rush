# Tetris Game
This simple Tetris game is built using Processing 3.5.4. It features a grid-based playing field where colored blocks fall from the top, and the player can control their movement and rotation to create horizontal lines and score points. The game ends when the grid is filled, and a restart prompt appears on the screen.

How to Play /n
Control the Falling Blocks: Use the left and right arrow keys to move the falling block horizontally. The block will automatically fall down over time.

Rotate the Falling Block: Tetris blocks cannot be rotated in this implementation.

Score Points: Score points by completing horizontal lines of blocks. When a horizontal line is completed, it disappears, and your score increases.

Game Over: The game ends when the grid is completely filled with blocks. Click anywhere on the screen to restart the game.

Customization
Resolution: The game is designed for a resolution of 200x400 pixels, and the cell size is set to 20x20. You can adjust the RES_X, RES_Y, NUM_ROWS, and NUM_COLS constants for a different playing field size.

Colors: The game uses a predefined list of colors for the blocks. You can modify the COLORS list to change the appearance of the blocks.

Speed: The falling speed of the blocks increases over time. You can customize the speed adjustment in the draw function.

Dependencies
Processing 3.5.4
Getting Started
Download and install Processing.

Copy and paste the provided code into the Processing editor.

Run the sketch, and the game window will appear.

Follow the on-screen instructions to play the game.

Have fun playing Tetris!
