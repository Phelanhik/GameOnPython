import pygame

class ChoiceOfCadrsRak():
    def __init__(self, character):
        self.character = character
        self.n = 0
        self.nr = 1
        self.nl = 15
        self.nmr = 29
        self.nml = 36
        self.npr = 45
        self.npl = 55
        self.njp = 65
        self.njpl = 74

    def choising(self):
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_x]:
            self.npr = 45
            self.npl = 55
            if self.character.y >= self.character.dno:
                if self.character.right:
                    self.n = self.nr
                    self.nr += 1
                    if self.n == 14:
                        self.n = 0
                        self.nr = 1
                elif not self.character.right:
                    self.n = self.nl
                    self.nl += 1
                    if self.n == 28:
                        self.n = 14
                        self.nl = 15
                if self.character.move:
                    if self.character.right:
                        self.n = self.nmr
                        self.nmr += 1
                        if self.n == 35:
                            self.n = 28
                            self.nmr = 29
                    elif not self.character.right:
                        self.n = self.nml
                        self.nml += 1
                        if self.n == 42:
                            self.n = 35
                            self.nml = 36
            if self.character.y < self.character.dno:
                if self.character.right:
                    self.n = 42
                elif not self.character.right:
                    self.n = 43
        elif keys[pygame.K_x] and self.character.y == self.character.dno:
            if self.character.right:
                self.n = self.npr - 1
                self.npr += 1
                if self.n == 54:
                    self.n = 44
                    self.npr = 45
            elif not self.character.right:
                self.n = self.npl - 1
                self.npl += 1
                if self.n == 64:
                    self.n = 54
                    self.npl = 55
        elif keys[pygame.K_x] and self.character.y < self.character.dno:
            if self.character.right:
                self.n = self.njp
                self.njp += 1
                if self.n == 73:
                    self.n = 64
                    self.njp = 65
            elif not self.character.right:
                self.n = self.njpl
                self.njpl += 1
                if self.n == 82:
                    self.n = 73
                    self.njpl = 74
        return self.n