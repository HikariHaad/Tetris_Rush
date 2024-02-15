# this game code is based on Processing 3.5.4

import random

# global constants for resolution in x and y along with calculation for the constant cell size of 20 x 20 for rows and cols

RES_X = 200
RES_Y = 400
NUM_ROWS = int(RES_Y / 20)
NUM_COLS = int(RES_X / 20)

# Colors list in order of red, blue, green, yellow, purple, white, black. More colors can be added or removed without any problems in the code.
COLORS = [[255, 51, 52], [12, 150, 228], [30, 183, 66], [246, 187, 0], [76, 0, 153], [255, 255, 255], [0, 0, 0]]

# the Block class to generate individual blocks


class Block:

    def __init__(self, color=None, row=-1, col=-1, val=1, moving=False):  # Block initializer along with necessary attributes and bogus default values
        if color is None:
            color = [210, 210, 210]  # default color for an empty cell
        self.color, self.row, self.col, self.moving, self.val = color, row, col, moving, val

    def __str__(self):  # string representation of a block for debugging purposes
        return (' -' + str(self.color[0]) + str(self.color[1]) + str(self.color[2]) + ' ' + str(self.row) + ' ' + str(
            self.col) + ' ' + str(self.moving) + ' ' + str(self.val) + '- ')

    def display(self):  # display method to draw each block on Processing output window
        fill(self.color[0], self.color[1], self.color[2])
        rect(self.col * 20, self.row * 20, 20, 20)

    def swap(self, other):  # swapping cell attributes for movement and animation except for val, row, and col as they are unique cell identifiers
        if self.moving and other.color == [210, 210, 210]:  # only swap with empty cells as tetris elements can only occupy empty spaces / cannot pass through other colored elements
            temp_color, temp_moving = self.color, self.moving
            self.color, self.moving = other.color, other.moving
            other.color, other.moving = temp_color, temp_moving
        else:
            pass

# main Game class


class Game:

    def __init__(self):  # Game class identifier along with attributes
        self.grid = None
        self.speed, self.score = 0, 0  # speed and score initialized to 0
        self.create()
        self.x_move = False

    def __str__(self):  # string representation of the Game class is the string representation of all blocks individually for potential debugging purposes
        result = ''
        for block in self.grid:
            result = result + str(block)
        return result

    def create(self):  # initializer method to create the empty grid with empty cells
        self.grid = []
        k = 0
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                self.grid.append(Block(row=r, col=c, val=k))
                k += 1

    def block_spawn(self):  # spawning a new block each time the previously spawned block stops moving
        if not self.is_moving():  # check for no more movement on the grid through this method defined later
            empty_flag = True
            # generate random col and random color for spawning the block. No problem or bug if the col number generated is already taken as another is generated due to no movement on the board
            rand_col = random.randint(0, NUM_COLS - 1)  
            rand_color = random.randint(0, len(COLORS) - 1)
            for block in self.grid:  # if a block is successfully generated, it is put in the topmost row hence block.row = 0, while the col and color are random 
                if block.color == [210, 210, 210] and block.row == 0 and block.col == rand_col:
                    block.color, block.moving = COLORS[rand_color], True
                    return True
            return False  # if no block can be spawned, the function returns False. This can be used to check for a filled board hence end the game.

    def display(self):  # display method for Game class to draw all the blocks in the grid
        for block in self.grid:
            block.display()

        if game.end():  # if the game ends, a separate message with the score and a prompt is generated on the screen
            # the numbers used to generate the font size and the point at which printing starts is made dynamic to adjust for different resolution sizes
            textSize(((RES_X * RES_Y) ** 0.3) // 1.3)
            fill(0, 0, 0)
            text("Score: " + str(self.score), RES_X // 3 , RES_Y // 2)
            textSize(((RES_X * RES_Y) ** 0.3) // 1.6)
            fill(0, 0, 0)
            text("Click to restart.", RES_X // 5, RES_Y // 1.1)
        else:
            textSize(((RES_X * RES_Y) ** 0.3) // 1.5)  # printing the score by default
            fill(0, 0, 0)
            text("Score: " + str(self.score), RES_X // 2.1, RES_Y // 8)

    def is_moving(self):  # check for a moving block on the board, and if no block is moving, this function prompts the block spawn method to create another block
        for block in self.grid:
            if block.moving:
                return True
        return False

    def fall(self):  # the fall method to make the colored blocks fall until the reach the ground or another block using the swap method in the Block class
        for block in self.grid:
            if block.moving:
                if block.row < NUM_ROWS - 1 and self.grid[block.val + NUM_COLS].color == [210, 210, 210]:  # conditions for empty block and the ground using NUM_ROWS
                    block.swap(self.grid[block.val + NUM_COLS])
                    return False  # as soon as the block is swapped, returning False as one movement has been completed
                else:
                    block.moving = False  # once the block stops moving or cannot move any longer, adjust the moving attribute to False
                    return True

    def control(self, _key):  # the input method to control the block movement 
        self.x_move = True  # to limit the movement in x to a single cell, using this attribute
        for block in self.grid:
            if block.moving:  # finding the currently moving block on the board as only that block can be controlled with the arrow keys
                if block.col >= 1 and _key == LEFT and self.x_move:
                    block.swap(self.grid[block.val - 1])  # swap with the left block for LEFT input
                elif block.col <= NUM_COLS - 2 and _key == RIGHT and self.x_move:
                    block.swap(self.grid[block.val + 1])  # swap with the right block for RIGHT input
                    self.x_move = False

    def scoring(self):  # the scoring method to increase the score by 1 for each vertical stack of 4
        for block in self.grid:
            try:  # use try and except to evade running into IndexErrors as all blocks are checked for a stack of 4, so the program can be easily adjusted for other number of stack in the game
                if block.color == self.grid[block.val + NUM_COLS].color == self.grid[block.val + (2 * NUM_COLS)].color == self.grid[block.val + (3 * NUM_COLS)].color != [210, 210, 210]:  # condition for a stack of 4
                    block.color, self.grid[block.val + NUM_COLS].color, self.grid[block.val + (2 * NUM_COLS)].color, self.grid[block.val + (3 * NUM_COLS)].color = [210, 210, 210], [210, 210, 210], [210, 210, 210], [
                        210, 210, 210]  # if a stack of 4 is found, change the colors to default hence removing them
                    return True
            except IndexError:
                continue

    def end(self):  # check for end of the game
        for block in self.grid:
            if block.color == [210, 210, 210]:  # the game will not end if even a single empty cell remains
                return False
        return True

    def clear(self):  # clear the game if the game ends by initializing it again
        self.__init__()


game = Game()


def setup():  # setting up the board
    size(RES_X, RES_Y)
    background(210)
    stroke(180)


def mouseClicked():  # restart the game once mouse clicked if and only if the game ends by filling the board
    if game.end():  # remove this condition to see the game restart without it ending by a mouse click
        game.clear()


def draw():
    if frameCount % (max(1, int(8 - game.speed))) == 0 or frameCount == 1:  # dynamic frame rate to adjust speed
        background(210)
        game.display()  # calling the display method to print everything on the Processing output
        game.block_spawn()
        if game.fall():  # once a block falls to the ground, increase the speed by 0.25
            game.speed += 0.25
        if game.scoring():  # increase the game score if the scoring method return True and reset the speed
            game.score += 1
            game.speed = 0


def keyPressed():
    game.control(keyCode)  # get the keyCode which is keyboard input and pass through the control method
