# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from cellfight import Cell

class CellLife(Cell):
    def __init__(self, width = 1500, height = 1000, cell_size = 10, speed = 10):
        Cell.__init__(self, 20, width, height)
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width + 10, height + 10
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)


        # Скорость протекания игры
        self.speed = speed
        self.foodstart()
        self.birthday()

    def dr(self):
        for nu in range(self.number):
            pygame.draw.rect(self.screen, (193, 0, 32), (self.cells[nu, 1] * 10, self.cells[nu, 2] * 10, self.cell_size - 1, self.cell_size - 1))
        for num in range(self.meal):
            pygame.draw.rect(self.screen, (57, 255, 20), (self.foods[num, 0] * 10 , self.foods[num, 1] * 10, self.cell_size - 1, self.cell_size - 1))



    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('blue'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.dr()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


if __name__ == '__main__':
    game = CellLife()
    game.run()
            