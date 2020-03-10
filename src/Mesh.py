
import engine
import pygame

class Mesh (object):

    def __init__(self, cols, rows, scale):
        self._cols = cols
        self._rows = rows
        self._scale = scale
        self._scroll_x = 38
        self._scroll_y = 80
        self._max_scroll = 900
        self._min_scroll = -100
        self._in_rect = False

    def Update(self) -> None:
        # self.MoveMesh()

        pos = pygame.mouse.get_pos()
        self._in_rect = pos[0] > self._scroll_x and pos[0] < self._scale * self._cols + self._scroll_x\
        and pos[1] > self._scroll_y and pos[1] < self._scale * self._rows + self._scroll_y

    def Render(self) -> None:
        for i in range(self._cols + 1):
            pygame.draw.aaline(engine._window_surface, (255, 255, 255),
            (self._scale * i + self._scroll_x, self._scroll_y),
            (self._scale * i + self._scroll_x, self._rows * self._scale + self._scroll_y))

        for j in range(self._rows + 1):
            pygame.draw.aaline(engine._window_surface, (255, 255, 255),
            (self._scroll_x, self._scale * j + self._scroll_y),
            (self._cols * self._scale + self._scroll_x, self._scale * j + self._scroll_y))

        pos = pygame.mouse.get_pos()
        x = ((pos[0] - (self._scroll_x % self._scale)) // self._scale) * self._scale + (self._scroll_x % self._scale)
        y = ((pos[1] - (self._scroll_y % self._scale)) // self._scale) * self._scale + (self._scroll_y % self._scale)
        if (pos[0] > self._scroll_x and pos[0] < self._scale * self._cols + self._scroll_x
        and pos[1] > self._scroll_y and pos[1] < self._scale * self._rows + self._scroll_y):
            pygame.draw.rect(engine._window_surface, (100, 100, 200),
            (x, y, self._scale, self._scale))

    def MoveMesh(self) -> None:
        _delta = pygame.mouse.get_rel()
        if (pygame.mouse.get_pressed()[2]):
            self._scroll_x += _delta[0]
            self._scroll_y += _delta[1]

        self._scroll_x = max(self._min_scroll, self._scroll_x)
        self._scroll_x = min(self._scroll_x, self._max_scroll)

        self._scroll_y = max(self._min_scroll, self._scroll_y)
        self._scroll_y = min(self._scroll_y, self._max_scroll)

    def GetMatrixPos(self, start, end):
        x1 = max(((start[0] - self._scroll_x) // self._scale), 0)
        y1 = max(((start[1] - self._scroll_y) // self._scale), 0)
        x2 = max(((end[0] - self._scroll_x) // self._scale), 0)
        y2 = max(((end[1] - self._scroll_y) // self._scale), 0)
        return ((x1, y1), (x2, y2))

    def RenderMatrix(self, matrix):
        for i in range(self._cols):
            for j in range(self._rows):
                value = matrix[matrix.GetIndex(i, j)]
                if (value == 1):
                    pygame.draw.rect(engine._window_surface, (150, 150, 255),
                    (j * self._scale + self._scroll_x, i * self._scale + self._scroll_y,
                    self._scale, self._scale))
                elif (value == 2):
                    pygame.draw.rect(engine._window_surface, (250, 150, 150),
                    (j * self._scale + self._scroll_x, i * self._scale + self._scroll_y,
                    self._scale, self._scale))
