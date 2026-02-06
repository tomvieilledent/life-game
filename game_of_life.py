#!/usr/bin/env python3
"""
Conway's Game of Life
A cellular automaton simulation with 1500x1000 pixel display
"""

import pygame
import random
import sys


# Configuration
WIDTH = 1500
HEIGHT = 1000
CELL_SIZE = 5
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)


class GameOfLife:
    """Conway's Game of Life implementation"""

    def __init__(self):
        """Initialize pygame and game state"""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Conway's Game of Life - Space: Pause | R: Random | C: Clear | Click: Toggle")
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.running = True
        self.paused = False
        self.randomize_grid()

    def randomize_grid(self):
        """Fill grid with random cells"""
        for i in range(ROWS):
            for j in range(COLS):
                self.grid[i][j] = random.choice([0, 1])

    def clear_grid(self):
        """Clear all cells"""
        for i in range(ROWS):
            for j in range(COLS):
                self.grid[i][j] = 0

    def count_neighbors(self, row, col):
        """Count living neighbors around a cell"""
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                r = (row + i) % ROWS
                c = (col + j) % COLS
                count += self.grid[r][c]
        return count

    def update_grid(self):
        """Apply Conway's Game of Life rules"""
        new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                neighbors = self.count_neighbors(i, j)
                
                if self.grid[i][j] == 1:
                    # Cell is alive
                    if neighbors in [2, 3]:
                        new_grid[i][j] = 1
                else:
                    # Cell is dead
                    if neighbors == 3:
                        new_grid[i][j] = 1

        self.grid = new_grid

    def draw_grid(self):
        """Draw the grid on screen"""
        self.screen.fill(BLACK)

        for i in range(ROWS):
            for j in range(COLS):
                if self.grid[i][j] == 1:
                    pygame.draw.rect(
                        self.screen,
                        WHITE,
                        (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    )

    def handle_mouse_click(self, pos):
        """Toggle cell state on mouse click"""
        x, y = pos
        col = x // CELL_SIZE
        row = y // CELL_SIZE
        if 0 <= row < ROWS and 0 <= col < COLS:
            self.grid[row][col] = 1 - self.grid[row][col]

    def handle_events(self):
        """Handle user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r:
                    self.randomize_grid()
                elif event.key == pygame.K_c:
                    self.clear_grid()
                elif event.key == pygame.K_ESCAPE:
                    self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self.handle_mouse_click(event.pos)

    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()

            if not self.paused:
                self.update_grid()

            self.draw_grid()
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


def main():
    """Entry point"""
    game = GameOfLife()
    game.run()


if __name__ == "__main__":
    main()
