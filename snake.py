import pygame
import random
import time

pygame.init()
font = pygame.font.Font(None, 36)
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
fruit = pygame.image.load('apple.png')
pygame.display.set_caption("SNAKE")
pygame.mixer.music.load("back.wav")
pygame.mixer.music.play(-1)
backgraund=pygame.image.load("back.png")

class Snake:

    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 10
        self.dx = 5  
        self.dy = 0
        self.d = 5
        self.is_add = False
        self.score = 0
        self.level = 1

    def draw(self):
        for i in range(len(self.elements)):
            if self.elements[i][0] != 0 and self.elements[i][1] !=0:
                pygame.draw.circle(screen, (255, 0,  0  ), self.elements[i], self.radius)

    def add_to_snake(self):
        self.size += 1
        for i in range (5):
            self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

class Food:
    def __init__(self):
        self.x = random.randint(75,700)
        self.y = random.randint(75,500)
        self.onscreen = True
        

    def draw(self):    
        screen.blit(fruit, (self.x,self.y))


def collision():
    if (food.x in range(snake.elements[0][0] - 28, snake.elements[0][0])) and  (food.y in range(snake.elements[0][1] - 28, snake.elements[0][1])) :
        snake.is_add = True 
        if snake.is_add == True:
            #В зависимости от лвла границы появления еды сужается
            if snake.level == 1:
                food.x = random.randint(75,700)
                food.y = random.randint(75,500)
            if snake.level == 2:
                food.x = random.randint(100,675)
                food.y = random.randint(100,475)
            if snake.level == 3:
                food.x = random.randint(125,650)
                food.y = random.randint(125,450)
            eatingSound.play()
            snake.d += 1
            snake.score += 1
    #Сужается проверка границы в зависимости от лвла
    if snake.level == 1:  
        if  (770 <= snake.elements[0][0] or snake.elements[0][0] <= 30) or (570 <= snake.elements[0][1] or snake.elements[0][1] <= 30):
            game_over()
    if snake.level == 2:
        if  (745 <= snake.elements[0][0] or snake.elements[0][0] <= 55) or (545 <= snake.elements[0][1] or snake.elements[0][1] <= 55):
            game_over()
    if snake.level == 3:
        if  (720 <= snake.elements[0][0] or snake.elements[0][0] <= 80) or (520 <= snake.elements[0][1] or snake.elements[0][1] <= 80):
            game_over()

def game_over():
    
    screen.fill((0, 0, 0))
    res = font.render('G A M E   O V E R!', True, (0, 90, 255))
    res1 = font.render('total score: ' + str(snake.score), True, (0, 90, 255))
    screen.blit(res, (250,150))
    screen.blit(res1, (270,250))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()

snake = Snake()
food = Food()
running = True

FPS = 20

clock = pygame.time.Clock()



eatingSound=pygame.mixer.Sound('eat1.wav')
while running:
    mill = clock.tick(FPS)
    screen.blit(backgraund,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                snake.dx = snake.d
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -snake.d
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -snake.d
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = snake.d
    if snake.score == 10:
        snake.level = 2
    if snake.score == 20:
        snake.level = 3
    #collision()
    #screen.fill((255,255,255))
    #Рисуется граница в зависимости от лвла
    if snake.level == 1:
        wallsurface = pygame.draw.rect(screen,(0,0,0),(0,0,800,600),50)
    if snake.level == 2:
        wallsurface = pygame.draw.rect(screen,(0,0,0),(0,0,800,600),100)
    if snake.level == 3:
        wallsurface = pygame.draw.rect(screen,(0,0,0),(0,0,800,600),150)
    snake.move()
    snake.draw()
    food.draw()
    res2 = font.render('score: ' + str(snake.score), True, (0, 90, 255))
    screen.blit(res2,(700,0))

    collision()
    pygame.display.flip()
