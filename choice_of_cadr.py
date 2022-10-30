
import pygame


class ChoiceOfCadrs():
    def __init__(self, character):
        self.character = character
    
    def __init__(self, y, dno, right, move):
        self.dno = dno
        self.right = right
        self.move = move
        self.y = y
        self.n = 0
        self.nr = 1
        self.nl = 15
        self.nmr = 29
        self.nml = 37
        self.npr = 47
        self.npl = 61
        self.njp = 53
        self.njpl = 67

    def choising(self):
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_x]:
            if self.y >= self.dno:
                if self.right:
                    self.n = self.nr
                    self.nr += 1
                    if self.n == 14:
                        self.n = 1
                        self.nr = 1
                elif not self.right:
                    self.n = self.nl
                    self.nl += 1
                    if self.n == 28:
                        self.n = 15
                        self.nl = 15
                if self.move:
                    if self.right:
                        self.n = self.nmr
                        self.nmr += 1
                        if self.n == 36:
                            self.n = 29
                            self.nmr = 29
                    elif not self.right:
                        self.n = self.nml
                        self.nml += 1
                        if self.n == 44:
                            self.n = 37
                            self.nml = 37
            if self.y < self.dno:
                if self.right:
                    self.n = 44
                elif not self.right:
                    self.n = 45
        elif keys[pygame.K_x] and self.y == self.dno:
            if self.right:
                self.n = self.npr
                self.npr += 1
                if self.n == 52:
                    self.n = 46
                    self.npr = 46
            elif not self.right:
                self.n = self.npl
                self.npl += 1
                if self.n == 66:
                    self.n = 60
                    self.npl = 60
        elif keys[pygame.K_x] and self.y < self.dno:
            if self.right:
                self.n = self.njp
                self.njp += 1
                if self.n == 60:
                    self.n = 53
                    self.njp = 53
            elif not self.right:
                self.n = self.njpl
                self.njpl += 1
                if self.n == 73:
                    self.n = 67
                    self.njpl = 67
        return self.n