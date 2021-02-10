import pathlib
import random

from typing import List, Optional, Tuple
from random import randint

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    
    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool=True,
        max_generations: Optional[float]=float('inf')
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool=False) -> Grid:
        grid = [[0] * self.cols for _ in range(self.rows)]

        if randomize == False:
            return grid
        else:
            row = 0
            for i in grid:
                col = 0
                for _ in i:
                    grid[row][col] = random.randint(0, 1)
                    col += 1
                row += 1
            return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        grid = self.curr_generation
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
        grid = self.curr_generation
        mas = [[0] * self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                l=0
                n =0
                if grid[i][j]:
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
        grid = mas
        return grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        max_generations = self.max_generations
        if self.generations > max_generations:
            return False
        else:
            return True

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.prev_generation == self.curr_generation:
            return False
        else: 
            return True

    @staticmethod
    def from_file(filename: pathlib.Path) -> 'GameOfLife':
        """
        Прочитать состояние клеток из указанного файла.
        """
        A = []
        with open(filename) as file:
            for line in filename.readlines():
                A = [line.split() for line in filename]
        self.curr_generatin = A
        game_r = GameOfLife([len(A[0]), len(A)])
        return game_r

    def save(filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        some = 0
        grid = self.curr_generation
        with open(filename, 'w') as file:
            for i in grid:
                score = 0
                for v in i:
                    if score == 0 and some > 0:
                        print(f'\n{v}', file=file, end='')
                    else:
                        print(v, file=file, end='')
                        some += 1
                    score += 1


        
