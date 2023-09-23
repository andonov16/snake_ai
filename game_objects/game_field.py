import numpy as np
import random
from game_objects.snake import *


class GameField:
    game_over = False

    def __init__(self, height, width, seed: int = 16):
        self.height = height
        self.width = width
        self.seed = seed
        self.field = np.full((height, width), -1)
        random.seed(self.seed)

        self.__generate_apple__()
        self.__generate_snake()

    def __generate_apple__(self) -> None:
        while True:
            apple_y = random.randint(2, self.height - 3)
            apple_x = random.randint(2, self.width - 3)
            if self.field[apple_y, apple_x] == -1:
                self.field[apple_y, apple_x] = 10
                return

    def __generate_snake(self) -> None:
        while True:
            head_y = random.randint(2, self.height - 3)
            head_x = random.randint(2, self.width - 3)
            if self.field[head_y, head_x] == -1:
                self.field[head_y, head_x] = 5
                self.player = Snake(Node(head_y, head_x))
                return

    # returns (old, new) Node
    def move_player(self):
        old = self.player.body[-1]  # Get the tail of the snake
        new = Node(old.x + self.player.direction[0], old.y + self.player.direction[1])

        # Check if the player exited the field
        if new.x < 0 or new.y < 0 or new.x >= self.width or new.y >= self.height:
            self.game_over = True
            return None

        # Check if the player bit itself
        if self.field[new.x, new.y] == 5:
            self.game_over = True
            return None

        ate = False

        # Check if the player ate the apple
        if self.field[new.x, new.y] == 10:
            self.player.size += 1
            ate = True
            self.__generate_apple__()  # Regenerate the apple when eaten

        self.player.body.append(new)  # Add the new head to the body

        # Update the field
        self.field[new.x, new.y] = 5

        # If the player didn't eat an apple, remove the old tail
        if not ate:
            removed_tail = self.player.body.pop(0)
            self.field[removed_tail.x, removed_tail.y] = -1

        # Check if the player has won
        if self.player.size == (self.width * self.height):
            self.game_over = True
            return None

        return old, new
