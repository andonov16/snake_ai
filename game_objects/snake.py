from game_objects.node import *


class Snake:
    size = 1
    body = list()
    direction = (1, 0)

    def __init__(self, head_node: Node) -> None:
        self.body.append(head_node)

    def turn_up(self) -> None:
        if self.direction == (1, 0):
            return
        self.direction = (-1, 0)

    def turn_down(self) -> None:
        if self.direction == (-1, 0):
            return
        self.direction = (1, 0)

    def turn_left(self) -> None:
        if self.direction == (0, 1):
            return
        self.direction = (0, -1)

    def turn_right(self) -> None:
        if self.direction == (0, -1):
            return
        self.direction = (0, 1)
