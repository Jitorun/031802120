import pygame, sys, random
from os import path
from numpy.distutils.fcompiler import pg
from pygame.locals import *

# 一些常量
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
BACKGROUNDCOLOR = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
gray = (128, 128, 128)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
FPS = 40

VHNUMS = 3
CELLNUMS = VHNUMS * VHNUMS
MAXRANDTIME = 100
HIGH_SCORE_FILE = "./high_score.txt"

def load_data():
    # 加载历史最高分
    file_path = HIGH_SCORE_FILE
    if path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                high_score = int(f.read())
            except:
                high_score = 0
    return high_score

def draw_text(self, text, size, color, x, y):
    font = pg.font.SysFont(self.font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    self.screen.blit(text_surface, text_rect)

# 退出
def terminate():
    pygame.quit()
    sys.exit()

# 随机生成游戏盘面
def newGameBoard():
    board = []
    for i in range(CELLNUMS):
        board.append(i)
    blackCell = CELLNUMS - 1
    board[blackCell] = -1

    for i in range(MAXRANDTIME):
        direction = random.randint(0, 3)
        if (direction == 0):
            blackCell = moveLeft(board, blackCell)
        elif (direction == 1):
            blackCell = moveRight(board, blackCell)
        elif (direction == 2):
            blackCell = moveUp(board, blackCell)
        elif (direction == 3):
            blackCell = moveDown(board, blackCell)
    return board, blackCell


# 若空白图像块不在最左边，则将空白块左边的块移动到空白块位置
def moveRight(board, blackCell):
    if blackCell % VHNUMS == 0:
        return blackCell
    board[blackCell - 1], board[blackCell] = board[blackCell], board[blackCell - 1]
    return blackCell - 1


# 若空白图像块不在最右边，则将空白块右边的块移动到空白块位置
def moveLeft(board, blackCell):
    if blackCell % VHNUMS == VHNUMS - 1:
        return blackCell
    board[blackCell + 1], board[blackCell] = board[blackCell], board[blackCell + 1]
    return blackCell + 1


# 若空白图像块不在最上边，则将空白块上边的块移动到空白块位置
def moveDown(board, blackCell):
    if blackCell < VHNUMS:
        return blackCell
    board[blackCell - VHNUMS], board[blackCell] = board[blackCell], board[blackCell - VHNUMS]
    return blackCell - VHNUMS


# 若空白图像块不在最下边，则将空白块下边的块移动到空白块位置
def moveUp(board, blackCell):
    if blackCell >= CELLNUMS - VHNUMS:
        return blackCell
    board[blackCell + VHNUMS], board[blackCell] = board[blackCell], board[blackCell + VHNUMS]
    return blackCell + VHNUMS

def High_score(score):
    font = pygame.font.SysFont("SimHei", 25)
    text = font.render("High Score:" + str(score), True, BLUE)
    windowSurface.blit(text, (100, 750))

def New_High_score(score):
    font = pygame.font.SysFont("SimHei", 25)
    text = font.render("New High Score:" + str(score), True, BLUE)
    windowSurface.blit(text, (100, 750))

def Step_num(count):
    font = pygame.font.SysFont("SimHei", 25)
    text = font.render("Step:" + str(count), True, BLUE)
    windowSurface.blit(text, (0, 750))

# 是否完成
def isFinished(board, blackCell,count,score):
    for i in range(CELLNUMS - 1):
        if board[i] != i:
            return False
    if score == 0:
        New_High_score(count)
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write(str(count))
    elif count < score:
        score = count
        New_High_score(score)
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write(str(count))
    else:
        High_score(score)
    return True

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(windowSurface, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(windowSurface, ic, (x, y, w, h))
    smallText = pygame.font.SysFont('SimHei', 20)#comicsansms
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    windowSurface.blit(textSurf, textRect)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        windowSurface.fill(BACKGROUNDCOLOR)
        largeText = pygame.font.SysFont('SimHei', 115)#comicsansms
        TextSurf, TextRect = text_objects('GAME', largeText)
        TextRect.center = ((1530 / 2), (750 / 2))
        windowSurface.blit(TextSurf, TextRect)
        button("GO", 450, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 950, 450, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)

def game_loop1():
    gameBoard, blackCell = newGameBoard()
    finish = False
    count = 0
    while True:
        windowSurface.fill(BACKGROUNDCOLOR)
        Step_num(count)
        score = load_data()
        High_score(score)
        button("Quit", 750, 750, 50, 30, red, bright_red, quitgame)
        # button("Random", 550, 750, 100, 30, red, bright_red, newGameBoard)
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if finish:
                continue
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    if blackCell % VHNUMS != VHNUMS - 1:
                        count += 1
                    blackCell = moveLeft(gameBoard, blackCell)
                if event.key == K_RIGHT or event.key == ord('d'):
                    if blackCell % VHNUMS != 0:
                        count += 1
                    blackCell = moveRight(gameBoard, blackCell)
                if event.key == K_UP or event.key == ord('w'):
                    if blackCell < CELLNUMS - VHNUMS:
                        count += 1
                    blackCell = moveUp(gameBoard, blackCell)
                if event.key == K_DOWN or event.key == ord('s'):
                    if blackCell >= VHNUMS:
                        count += 1
                    blackCell = moveDown(gameBoard, blackCell)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                col = int(x / cellWidth)
                row = int(y / cellHeight)
                index = col + row * VHNUMS
                if (
                        index == blackCell - 1 or index == blackCell + 1 or index == blackCell - VHNUMS or index == blackCell + VHNUMS):
                    gameBoard[blackCell], gameBoard[index] = gameBoard[index], gameBoard[blackCell]
                    blackCell = index
                    count += 1

        if (isFinished(gameBoard, blackCell,count,score)):
            gameBoard[blackCell] = CELLNUMS - 1
            finish = True

        for i in range(CELLNUMS):
            rowDst = int(i / VHNUMS)
            colDst = int(i % VHNUMS)
            rectDst = pygame.Rect(colDst * cellWidth, rowDst * cellHeight, cellWidth, cellHeight)

            if gameBoard[i] == -1:
                continue

            rowArea = int(gameBoard[i] / VHNUMS)
            colArea = int(gameBoard[i] % VHNUMS)
            rectArea = pygame.Rect(colArea * cellWidth, rowArea * cellHeight, cellWidth, cellHeight)
            windowSurface.blit(gameImage, rectDst, rectArea)

        for i in range(VHNUMS + 1):
            pygame.draw.line(windowSurface, BLACK, (i * cellWidth, 0), (i * cellWidth, gameRect.height))
        for i in range(VHNUMS + 1):
            pygame.draw.line(windowSurface, BLACK, (0, i * cellHeight), (gameRect.width, i * cellHeight))

        button("Random", 550, 750, 100, 30, red, bright_red, game_loop1)
        windowSurface.blit(gameImage, (780, 0))
        # button("try again", 150, 450, 100, 50, green, bright_green, newGameBoard)

        pygame.display.update()
        mainClock.tick(FPS)

def game_loop():
    gameBoard, blackCell = newGameBoard()
    finish = False
    count = 0
    while True:
        windowSurface.fill(BACKGROUNDCOLOR)
        Step_num(count)
        score = load_data()
        High_score(score)
        button("Quit", 750, 750, 50, 30, red, bright_red, quitgame)
        # button("Random", 550, 750, 100, 30, red, bright_red, newGameBoard)
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if finish:
                continue
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    if blackCell % VHNUMS != VHNUMS - 1:
                        count += 1
                    blackCell = moveLeft(gameBoard, blackCell)
                if event.key == K_RIGHT or event.key == ord('d'):
                    if blackCell % VHNUMS != 0:
                        count += 1
                    blackCell = moveRight(gameBoard, blackCell)
                if event.key == K_UP or event.key == ord('w'):
                    if blackCell < CELLNUMS - VHNUMS:
                        count += 1
                    blackCell = moveUp(gameBoard, blackCell)
                if event.key == K_DOWN or event.key == ord('s'):
                    if blackCell >= VHNUMS:
                        count += 1
                    blackCell = moveDown(gameBoard, blackCell)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                col = int(x / cellWidth)
                row = int(y / cellHeight)
                index = col + row * VHNUMS
                if (index == blackCell - 1 or index == blackCell + 1 or index == blackCell - VHNUMS or index == blackCell + VHNUMS):
                    gameBoard[blackCell], gameBoard[index] = gameBoard[index], gameBoard[blackCell]
                    blackCell = index
                    count += 1

        if (isFinished(gameBoard, blackCell,count,score)):

            gameBoard[blackCell] = CELLNUMS - 1

            finish = True

        button("Quit", 750, 750, 50, 30, red, bright_red, quitgame)
        for i in range(CELLNUMS):
            rowDst = int(i / VHNUMS)
            colDst = int(i % VHNUMS)
            rectDst = pygame.Rect(colDst * cellWidth, rowDst * cellHeight, cellWidth, cellHeight)
            
            if gameBoard[i] == -1:
                continue

            rowArea = int(gameBoard[i] / VHNUMS)
            colArea = int(gameBoard[i] % VHNUMS)
            rectArea = pygame.Rect(colArea * cellWidth, rowArea * cellHeight, cellWidth, cellHeight)
            windowSurface.blit(gameImage, rectDst, rectArea)

        for i in range(VHNUMS + 1):
            pygame.draw.line(windowSurface, BLACK, (i * cellWidth, 0), (i * cellWidth, gameRect.height))
        for i in range(VHNUMS + 1):
            pygame.draw.line(windowSurface, BLACK, (0, i * cellHeight), (gameRect.width, i * cellHeight))

        button("Random", 550, 750, 100, 30, red, bright_red, game_loop1)
        windowSurface.blit(gameImage, (780, 0))

        pygame.display.update()
        mainClock.tick(FPS)

def quitgame():
    pygame.quit()
    quit()

# 初始化
pygame.init()
mainClock = pygame.time.Clock()

# 加载图片
gameImage = pygame.image.load(r'./e_2.jpg')
gameRect = gameImage.get_rect()

# 设置窗口
windowSurface = pygame.display.set_mode((1530, 785))
pygame.display.set_caption('拼图')
clock = pygame.time.Clock()
pygame.font.SysFont('arial',32)
cellWidth = int(gameRect.width / VHNUMS)
cellHeight = int(gameRect.height / VHNUMS)

game_intro()
game_loop()

pygame.quit()
quit()
# 游戏主循环
