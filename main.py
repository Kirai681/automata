import pygame
import config as c
from src.grid import Grid
from src.game_state import GameState


def main():
    pygame.init()
    screen = pygame.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))
    pygame.display.set_caption("Automata")
    clock = pygame.time.Clock()
    grid = Grid(c.GRID_SIZE, c.GRID_SIZE)

    state = GameState()

    all_items = pygame.sprite.Group()
    all_components = pygame.sprite.Group()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and not state.is_paused():
                    state.pause()
                    print("pause")
                elif event.key == pygame.K_ESCAPE and state.is_paused():
                    state.resume()
                    print("resume")
                if event.key == pygame.K_SPACE and not state.is_paused():
                    state.toggle_simulation()

        screen.fill(c.BACKGORUND_COLOR)

        if state.is_build():
            for y in range(grid.height):
                for x in range(grid.width):
                    rect = pygame.Rect(
                        x * c.CELL_SIZE,
                        y * c.CELL_SIZE,
                        c.CELL_SIZE,
                        c.CELL_SIZE,
                    )
                    pygame.draw.rect(screen, c.GRID_COLOR, rect, 1)

        clock.tick(c.TARGET_FPS)

        all_components.update()
        all_components.draw(screen)

        all_items.update()
        all_items.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
