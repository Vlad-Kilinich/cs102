import pygame
from pygame.locals import *
import math

from life import GameOfLife
from ui import UI

class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int=10, speed: int=10) -> None:
        super().__init__(life)
        
        
        self.speed = speed
        self.cell_size = cell_size
        self.life = life
        self.width = self.life.rows / self.cell_size
        
        self.heught = self.life.cols / self.cell_size
        
        self.screen_size = self.life.rows * cell_size, self.life.cols * cell_size
        self.screen = pygame.display.set_mode(self.screen_size)
        

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def draw_grid(self) -> None:
        y = 0
        grid = self.life.curr_generation

        for i in grid:
            x = 0
            for v in i:
                color = 'white' if v == 0 else 'green'
                pygame.draw.rect(self.screen, pygame.Color(color),
                                    pygame.Rect(x, y, self.cell_size, self.cell_size))
                x += self.cell_size
            y += self.cell_size

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = True if pause == False else False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        row = math.floor(x/self.cell_size)
                        col = math.floor(y/self.cell_size)
                        self.life.curr_generation[col][row] = 1 if self.life.curr_generation[col][row] == 0 else 0
                        self.draw_grid()

            if not self.life.is_changing and self.life.randomize == True:
                running = False

            if not pause:
                self.draw_lines()

                self.life.step()
                if self.life.generations > self.life.max_generations:
                    break
                self.draw_grid()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()
