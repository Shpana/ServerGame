
class Matrix (list):

    def __init__(self, rows, cols):
        self._cols = cols
        self._rows = rows
        for i in range(rows * cols): self.append(0)

    def GetIndex(self, x, y) -> int:
        return x * self._cols + y

    def FillRect(self, start, end, area) -> None:
        x1 = min(start[0], end[0])
        x2 = max(start[0], end[0])
        y1 = min(start[1], end[1])
        y2 = max(start[1], end[1])
        print((x2 - x1 + 1) * (y2 - y1 + 1))
        if ((x2 - x1 + 1) * (y2 - y1 + 1) != area):
            return "Area"

        nflag = False
        rflag = False
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if (self[self.GetIndex((j + 1) % self._rows, i)] == 1 or
                    self[self.GetIndex((j - 1) % self._rows, i)] == 1 or
                    self[self.GetIndex(j, (i + 1) % self._cols)] == 1 or
                    self[self.GetIndex(j, (i - 1) % self._cols)] == 1):
                    nflag = True
                    break

                if (self[self.GetIndex(j, i)] != 0):
                    rflag = True

            if (nflag): break

        if (not nflag): return "N-flag"
        if (rflag): return "R-flag"

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                self[self.GetIndex(j, i)] = 1

        return 1

    def GetInfo(self) -> None:
        print("-----------------")
        for i in range(self._cols):
            for j in range(self._rows):
                print(self[self.GetIndex(i, j)], end = " ")
            print()
