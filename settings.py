import pygame

# set color RGB codes
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GRASS_GREEN = (128, 255, 0)
GREEN = (0, 255, 0)
BLUE_GREEN = (0, 255, 128)
CYAN = (0, 255, 255)
LIGHTBLUE = (0, 128, 255)
BLUE = (0, 0, 255)
PURPLE = (127, 0, 255)
MAGENTA = (255, 0, 255)
PINK = (255, 0, 127)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# game & screen configuration
FPS = 240
WIDTH, HEIGHT = 600, 700
ROWS = COLS = 40
TOOLBAR_HEIGHT = HEIGHT - WIDTH
PIXEL_SIZE = WIDTH // COLS
BG_COLOR = WHITE
DRAW_GRID_LINES = False  # we want to hide pixel girds or make it True to see

def get_font(size):
    return pygame.font.SysFont("Monocraft", size)




