import pygame
import random

from pygame.locals import *
from typing import List, Tuple
from random import randint

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]

class GameOfLife:

    def __init__(self, width: int=640, height: int=480, cell_size: int=10, speed: int=10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

# Устанавливаем размер окна
        self.screen_size = width, height
# Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

# Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

# Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
# Создание списка клеток
        self.create_grid(True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_lines()

# Отрисовка списка клеток
# Выполнение одного шага игры (обновление состояния ячеек)
# PUT YOUR CODE HERE
            self.draw_grid()
            self.get_next_generation()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool=False) -> Grid:
        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """


        self.grid = [[0] * self.cell_width for _ in range(self.cell_height)]

        if randomize == False:
            return self.grid
        else:
            row = 0
            for i in self.grid:
                col = 0
                for _ in i:
                    self.grid[row][col] = random.randint(0, 1)
                    col += 1
                row += 1
            return self.grid


    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        y = 0
        grid = self.grid

        for i in grid:
            x = 0
            for v in i:
                color = 'white' if v == 0 else 'green'
                pygame.draw.rect(self.screen, pygame.Color(color),
                                    pygame.Rect(x, y, self.cell_size, self.cell_size))
                x += self.cell_size
            y += self.cell_size


    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """
        grid = self.grid
        relative_neighbours = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
        list_of_neighbors = []

        for i in relative_neighbours:
            i[0] += cell[0]
            i[1] += cell[1]

        for i in relative_neighbours:
            row, col = i
            try:
                if row >= 0 and col >= 0:
                    list_of_neighbors.append(grid[row][col])
                else:
                    continue
            except IndexError:
                continue

        return list_of_neighbors


    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        grid = self.grid
        mas = [[0] * self.cell_width for _ in range(self.cell_height)]
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                l=0
                n =0
                if self.grid[i][j]:
                    n =1
                spisok = self.get_neighbours([i, j])
                for k in spisok:
                    if k:
                        l += 1
                    else:
                        pass
                if (l >= 2) and (n ==1) and (l<=3):
                    mas[i][j] = 1
                elif (l==3) and (n ==0):
                    mas[i][j] = 1
                else:
                    mas[i][j] =0
        self.grid = mas
        return self.grid
