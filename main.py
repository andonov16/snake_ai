from game_objects.game_field import *
import pygame
import time
import threading


GAME_FIELD = GameField(16, 16)
FIELD_SIZE = 16
CELL_SIZE = 16
SCREEN = pygame.display.set_mode((FIELD_SIZE * CELL_SIZE, FIELD_SIZE * CELL_SIZE))
GAME_DELAY = 0.25


def move_event() -> None:
    while True:
        time.sleep(GAME_DELAY)
        output = GAME_FIELD.move_player()
        if GAME_FIELD.game_over:
            return


def refresh_screen() -> None:
    for y in range(FIELD_SIZE):
        for x in range(FIELD_SIZE):
            color = (51, 51, 51)
            if GAME_FIELD.field[y, x] == 10:
                color = (255, 0, 0)
            elif GAME_FIELD.field[y, x] == 5:
                color = (255, 255, 255)

            pygame.draw.rect(SCREEN,
                             color,
                             pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def main() -> None:
    pygame.init()
    pygame.display.set_caption("AI Snake")

    move_thread = threading.Thread(target=move_event)
    move_thread.start()

    running = True
    while (not GAME_FIELD.game_over) and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    GAME_FIELD.player.turn_down()
                elif event.key == pygame.K_UP:
                    GAME_FIELD.player.turn_up()
                elif event.key == pygame.K_LEFT:
                    GAME_FIELD.player.turn_left()
                elif event.key == pygame.K_RIGHT:
                    GAME_FIELD.player.turn_right()

        refresh_screen()

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
