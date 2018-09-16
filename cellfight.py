# -*- coding: utf-8 -*-
import numpy as np



class Cell():
    def __init__(self, number, width, height):
      
        self.width = width
        self.height = height
        self.bwidth = width // 10
        self.bheight = height // 10
        self.energy = 20
        self.epoch = 1
        self.number = number
    
    def day(self):
        self.move()
        self.collision()
        self.food()
        self.watch()

    def Lebensraum(self):
        self.leb = np.zeros((self.bwidth, self.bheight))
    
    
    def foodstart(self):
        self.meal = np.random.randint(self.number * 2, self.number * 5)
        self.foods = np.zeros((self.number * 10, 2))
        for a in range(self.meal):
            width = np.random.randint(1, self.bwidth)
            height = np.random.randint(1, self.bheight)
            self.foods[a, 0] = width
            self.foods[a, 1] = height
    
    def food(self):
        for n in range(self.number // 2):
            n += int(abs(self.meal.sum()))
            width = np.random.randint(1, self.bwidth)
            height = np.random.randint(1, self.bheight)
            self.foods[n, 0] = width
            self.foods[n, 1] = height
        self.meal = int(abs(self.meal.sum())) + self.number // 2
        
    def birthday(self):
        self.cells = np.zeros((self.bwidth, 3))
        for i in range(self.number):
            width = np.random.randint(1, self.bwidth)
            height = np.random.randint(1, self.bheight)
            self.cells[i, 0] = self.energy
            self.cells[i, 1] = width
            self.cells[i, 2] = height
    
    def collision(self):
        pass    
        
    
    def directions(self):
        self.n = [self.bwidth, self.bheight + 1]
        self.s = [self.bwidth, self.bheight - 1]
        self.w = [self.bwidth - 1, self.bheight]
        self.e = [self.bwidth + 1, self.bheight]
        self.nw = [self.bwidth - 1, self.bheight + 1]
        self.ne = [self.bwidth + 1, self.bheight + 1]
        self.sw = [self.bwidth - 1, self.bheight - 1]
        self.se = [self.bwidth + 1, self.bheight - 1]
        
    
    def resettlement(self):
        for n in range(self.number):
            energy = self.cells[n, 0]
            width = self.cells[n, 1]
            height = self.cells[n, 2]
            self.leb[width, height] = energy
        for nu in range(self.foods):
            wid = self.foods[nu, 0]
            hei = self.foods[nu, 1]
            self.leb[wid, hei] = -1
    
    def weight(self):
        pass
    
            
    def watch(self):
        self.eye = np.zeros((self.bwidth * 3, 6))
        for n in range(self.number):
            pass













            
