import pygame
from enum import Enum


class GameState(Enum):
    BUILD = 1
    SIMULATION = 2


# -- CONFIG --
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
GRID_SIZE = 10
CELL_SIZE = WINDOW_WIDTH // GRID_SIZE
TARGET_FPS = 60

# -- COLORS --
BACKGORUND_COLOR = (30, 30, 30)
GRID_COLOR = (50, 50, 50)
HIGHLIGHT_COLOR = (255, 255, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Automata")
    clock = pygame.time.Clock()

    cursor_x = 0
    cursor_y = 0

    game_state = GameState.BUILD
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_state == GameState.BUILD:
                        game_state = GameState.SIMULATION
                    else:
                        game_state = GameState.BUILD
                if game_state == GameState.BUILD:
                    if event.key == pygame.K_w and cursor_y > 0:
                        cursor_y -= 1
                    if event.key == pygame.K_s and cursor_y < (GRID_SIZE - 1):
                        cursor_y += 1
                    if event.key == pygame.K_a and cursor_x > 0:
                        cursor_x -= 1
                    if event.key == pygame.K_d and cursor_x < (GRID_SIZE - 1):
                        cursor_x += 1

        screen.fill(BACKGORUND_COLOR)
        if game_state == GameState.BUILD:
            screen.fill((40, 40, 50))

        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = pygame.Rect(
                    x * CELL_SIZE,
                    y * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE,
                )
                pygame.draw.rect(screen, GRID_COLOR, rect, 1)

        if game_state == GameState.SIMULATION:
            clock.tick(TARGET_FPS)

        if game_state == GameState.BUILD:
            highlight_rect = pygame.Rect(
                cursor_x * CELL_SIZE,
                cursor_y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            )
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, highlight_rect, 3)

        pygame.display.flip()


if __name__ == "__main__":
    main()
