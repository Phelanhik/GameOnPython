
from Rumble_code.Rumble_II import RumbleII


class ChoiceOfCadrsRumbleII():
    def __init__(self, character):
        self.character = character
        self.n = 0
        self.nr = 1
        self.nl = 15
        self.nmr = 29
        self.nml = 37
        self.npr = 47
        self.npl = 53
        self.njp = 59
        self.njpl = 67

    def choising(self):
        if self.character.a not in self.character.actions['x']:
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
                        if self.n == 36:
                            self.n = 28
                            self.nmr = 29
                    elif not self.character.right:
                        self.n = self.nml
                        self.nml += 1
                        if self.n == 44:
                            self.n = 36
                            self.nml = 37
            if self.character.y < self.character.dno:
                if self.character.right:
                    self.n = 44
                elif not self.character.right:
                    self.n = 45
        elif self.character.a in self.character.actions['x'] and self.character.y == self.character.dno:
            if self.character.right:
                self.n = self.npr
                self.npr += 1
                if self.n == 52:
                    self.n = 45
                    self.npr = 46
            elif not self.character.right:
                self.n = self.npl
                self.npl += 1
                if self.n == 60:
                    self.n = 52
                    self.npl = 53
        elif self.character.a in self.character.actions['x'] and self.character.y < self.character.dno:
            if self.character.right:
                self.n = self.njp
                self.njp += 1
                if self.n == 66:
                    self.n = 60
                    self.njp = 61
            elif not self.character.right:
                self.n = self.njpl
                self.njpl += 1
                if self.n == 73:
                    self.n = 66
                    self.njpl = 67
        return self.n