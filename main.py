from utils import *
import pygame
import json

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PAINT.FM")

def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
    return grid

def draw_grid(win, grid):

    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))

        for j in range(COLS + 1):
            pygame.draw.line(win, BLACK, (j * PIXEL_SIZE, 0), (j * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    pygame.draw.line(WINDOW, BLACK, (0, 600), (600, 600))

    for button in buttons:
        button.draw(win)

    pygame.display.update()

def get_pos(position):
    x, y = position
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
button_y2 = button_y + 30
buttons = [
     Button(10, button_y, 20, 20, BLACK),
     Button(35, button_y, 20, 20, RED),
     Button(60, button_y, 20, 20, ORANGE),
     Button(85, button_y, 20, 20, YELLOW),
     Button(110, button_y, 20, 20, GRASS_GREEN),
     Button(135, button_y, 20, 20, GREEN),
     Button(160, button_y, 20, 20, BLUE_GREEN),
     Button(10, button_y2, 20, 20, CYAN),
     Button(35, button_y2, 20, 20, LIGHTBLUE),
     Button(60, button_y2, 20, 20, BLUE),
     Button(85, button_y2, 20, 20, PURPLE),
     Button(110, button_y2, 20, 20, MAGENTA),
     Button(135, button_y2, 20, 20, PINK),
     Button(160, button_y2, 20, 20, GRAY),
     # Button(195, button_y + 5, 40, 40, WHITE, "Fill", BLACK),
     Button(360, button_y, 50, 50, WHITE, "Erase", BLACK),
     Button(420, button_y, 50, 50, (224, 224, 224), "Clear", BLACK),
     Button(540, button_y, 50, 50, (255, 204, 229), "Save", BLACK),
     Button(480, button_y, 50, 50, (224, 224, 224), "Load", BLACK)
]

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    drawing_color = button.color
                    if button.text == "Fill":
                        pass
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK
                    if button.text == "Save":
                        with open("paint(1).txt", 'w') as paint_file:
                            json.dump(grid, paint_file)
                            drawing_color = BLACK
                    if button.text == "Load":
                        with open("paint.txt") as f:
                            grid = json.load(f)
                        drawing_color = BLACK

    draw(WINDOW, grid, buttons)


pygame.quit()

