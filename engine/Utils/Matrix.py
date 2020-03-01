
class Matrix (list):

    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        for i in range(rows * cols): self.append(0)

    def GetIndex(self, x, y) -> int:
        return x * self._rows + y
        
