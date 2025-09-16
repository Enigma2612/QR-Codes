import pygame, sys, pprint
from pygame import Vector2 as vec

W,H = 1400, 900
WIN = pygame.display.set_mode((W,H))
FPS = 60
clock = pygame.time.Clock()

grid = [[0 for _ in range(21)] for _ in range(21)]
with open(r'base grids/v1_base_grid.txt') as f: grid = eval(f.read())
tile_size = 32

link = ''
no_of_chars = len(link)

def draw_grid(pos, grid):
    rows = len(grid)
    cols = len(grid[0])
    surf = pygame.Surface((rows*tile_size, cols*tile_size))
    surf.fill('white')
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                block = pygame.Surface((tile_size, tile_size))
                surf.blit(block, (j*tile_size, i*tile_size))
            pygame.draw.line(surf, 'grey', (0, i*tile_size), (surf.get_width(), i*tile_size),2)
            pygame.draw.line(surf, 'grey', (j*tile_size, 0), (j*tile_size, surf.get_height()),2)
    WIN.blit(surf, surf.get_rect(center = pos))
    return surf.get_rect(center=pos)

while True:
    WIN.fill('coral')
    mpos = pygame.mouse.get_pos()
    jmouse = pygame.mouse.get_just_pressed()
    kmouse = pygame.mouse.get_pressed()
    jkeys = pygame.key.get_just_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); sys.exit()
        
    grid_rect = draw_grid((W//2, H//2), grid)
    if (grid_rect.left <= mpos[0] <= grid_rect.right) and (grid_rect.top <= mpos[1] <= grid_rect.bottom):
        rel_mpos = vec(mpos) - vec(grid_rect.topleft)
        rel_tpos = tx,ty = rel_mpos//tile_size
        tx,ty = int(tx), int(ty)

        # if jmouse[0]: grid[ty][tx] = not grid[ty][tx]; print(tx,ty); pprint.pprint(grid)
        try:
            if kmouse[0]: grid[ty][tx] = 1
            if kmouse[2]: grid[ty][tx] = 0
        except: pass
        if jkeys[pygame.K_SPACE]: print(grid)


    pygame.display.update()
