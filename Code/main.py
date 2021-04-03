import cv2
import numpy as np
import math
import random
import pygame
clock = pygame.time.Clock()
from pygame import mixer
# Intialize the pygame
pygame.init()

# create the screen

screen = pygame.display.set_mode((800, 600))

# Background configurations


background = pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Background\\background1.png')
mixer.music.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Musics\\background.wav')
mixer.music.play(-1)

# Caption and Icon configurations

pygame.display.set_caption("Space Battle")
icon = pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Display\\ufo.png')
pygame.display.set_icon(icon)


# Player configurations

playerimgarray=[]
playerimgarray.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Rocket\\rocket 1.png'))
playerimgarray.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Rocket\\rocket 2.png'))
playerimgarray.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Rocket\\rocket 3.png'))
playerimgarray.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Rocket\\rocket 4.png'))
playerimgarray.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Rocket\\rocket 5.png'))
playerimgarray.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Rocket\\rocket 6.png'))
playerimgarray.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Rocket\\rocket 7.png'))

playerX = 320
playerY = 365
playerX_change = 0

player_it=-1

def player(x, y, i):
    screen.blit(playerimgarray[i], (x, y))

# Enemy configurations

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (1).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (2).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (3).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (4).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (5).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (6).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (7).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (8).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (9).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (10).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (11).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (12).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (13).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (14).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (15).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (16).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (17).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (18).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (19).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (20).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (21).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (22).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (23).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (24).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (25).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (26).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (27).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (28).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (29).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (30).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (31).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (32).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (33).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (34).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (35).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (36).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (37).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (38).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (39).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (40).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (41).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (42).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (43).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (44).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (45).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (46).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (47).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (48).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (49).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (50).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (51).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (52).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (53).png'))
enemyImg.append(pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Enemy\\frame (54).png'))


for i in range(num_of_enemies):
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

enemy_it = -1

# Bullet configurations

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Pictures\\Bullet\\bullet3.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 20
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 40:
        return True
    else:
        return False

# Score configurations

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

def show_score(player_name,x, y):
    score = font.render("Player Name: "+player_name+"    "+"Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Game Over configurations

over_font = pygame.font.Font('freesansbold.ttf', 64)
g_o=1
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    g_o=0
#Database
player_names=[]
player_score=[]
datas = list(zip(player_names, player_score))
def read_from_data_base():
    f = open("C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Player Data\\data.txt", "r")
    run=True
    while run:
        s = f.readline()
        if (len(s) == 0):
             break
        b=s.split(" ")
        player_names.append(b[0])
        player_score.append(int(b[1]))
    f.close()

def update_data_base(p_n,p_s):
    tmp=p_n.split(' ')
    p_n=tmp[0]
    player_names.append(p_n)
    player_score.append(int(p_s))
    datas = list(zip(player_names, player_score))
    datas.sort(key=lambda x: x[1], reverse=True)
    myfile = open("C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Player Data\\data.txt", "w")
    lim = 0
    for i, j in datas:
        x = str(j)
        myfile.write(i + " " + x + "\n")
        lim = lim + 1
        if lim == 5:
            break
    myfile.close
def show_list():
    score = font.render("Player Name        Score", True, ( 133, 253, 6 ))
    screen.blit(score, (200, 100))
    it = 1
    for i, j in datas:
        score = font.render(i ,True, (  133, 253, 6))
        screen.blit(score, (200, 100 + 50 * it))
        score = font.render(str(j) ,True, (  133, 253, 6 ))
        screen.blit(score, (500, 100 + 50 * it))
        it = it + 1
    score = font.render("Press space to continue", True, (255, 255, 255))
    screen.blit(score, (200, 500))

f=1
read_from_data_base()
datas = list(zip(player_names, player_score))
datas.sort(key=lambda x: x[1], reverse=True)
running = True
while running:
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    if f==1:
       show_list()
    else:
      break
    #show_score(textX, testY)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                f=0
    pygame.display.update()
    k = cv2.waitKey(10)
    if k == 27:
        break
name= "----------"
pos=0
f=1
def entername():
    score = font.render("Enter your name:", True, (133, 253, 6))
    screen.blit(score, (100, 100))
    score = font.render(name, True, ( 1, 1, 0 ))
    screen.blit(score, (420, 100))
    score = font.render("Enter Space to continue", True, (255, 255, 255))
    screen.blit(score, (200 , 500))

def welcome(str):
    score = font.render("Welcome to Space Battle "+str, True, (133, 253, 6 ))
    screen.blit(score, (100, 300))
    #score = font.render()
    score = font.render("Press Space to continue", True, (255, 255, 255))
    screen.blit(score, (200, 500))

def game_info():
    g_info = font.render("Game Instruction: ",True,(133, 253, 6))
    screen.blit(g_info,(100,90))
    g_info1 = font.render("To Go Left: Show Two Fingers.", True, (133, 253, 6))
    screen.blit(g_info1, (100, 190))
    g_info2 = font.render("To Go Right: Show Three Fingers.", True, (133, 253, 6))
    screen.blit(g_info2, (100, 290))
    g_info3 = font.render("To Shoot: Show Four Fingers.", True, (133, 253, 6))
    screen.blit(g_info3, (100, 390))
    g_info4 = font.render("Press Space To Continue.", True, (255, 255, 255))
    screen.blit(g_info4, (200, 490))
    #screen.blit()
def must_print_name():
    g_info = font.render("You Must Enter Your Name.", True, (133, 253, 6))
    screen.blit(g_info, (100, 300))

mpr = 0

bk=1
while running:
    if bk==0:
        break
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    if mpr == 1:
       must_print_name()
    if f==1:
        entername()

    elif f==2:
        game_info()
    else :
        welcome(name)
    if pos:
        mpr = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if f>=3:
                    bk=0
                if(f==1 and pos):
                  while pos<=9 and name[pos] == '-':
                    str1 = list(name)
                    str1[pos] = " "
                    name = "".join(str1)
                    pos = pos + 1
                if(f==1 and pos==0):
                      mpr = 1
                else:
                      f = f + 1
                      print(pos)

            if event.key == pygame.K_BACKSPACE:
                pos = pos - 1
                str1 = list(name)
                str1[pos] = "-"
                name = "".join(str1)
                if pos < 0:
                    pos = 0
            if pos < 10:
                if event.key == pygame.K_a:
                    str1 = list(name)
                    str1[pos] = "a"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_b:
                    str1 = list(name)
                    str1[pos] = "b"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_c:
                    str1 = list(name)
                    str1[pos] = "c"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_d:
                    str1 = list(name)
                    str1[pos] = "d"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_e:
                    str1 = list(name)
                    str1[pos] = "e"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_f:
                    str1 = list(name)
                    str1[pos] = "f"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_g:
                    str1 = list(name)
                    str1[pos] = "g"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_h:
                    str1 = list(name)
                    str1[pos] = "h"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_i:
                    str1 = list(name)
                    str1[pos] = "i"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_j:
                    str1 = list(name)
                    str1[pos] = "j"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_k:
                    str1 = list(name)
                    str1[pos] = "k"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_l:
                    str1 = list(name)
                    str1[pos] = "l"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_m:
                    str1 = list(name)
                    str1[pos] = "m"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_n:
                    str1 = list(name)
                    str1[pos] = "n"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_o:
                    str1 = list(name)
                    str1[pos] = "o"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_p:
                    str1 = list(name)
                    str1[pos] = "p"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_q:
                    str1 = list(name)
                    str1[pos] = "q"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_r:
                    str1 = list(name)
                    str1[pos] = "r"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_s:
                    str1 = list(name)
                    str1[pos] = "s"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_t:
                    str1 = list(name)
                    str1[pos] = "t"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_u:
                    str1 = list(name)
                    str1[pos] = "u"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_v:
                    str1 = list(name)
                    str1[pos] = "v"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_w:
                    str1 = list(name)
                    str1[pos] = "w"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_x:
                    str1 = list(name)
                    str1[pos] = "x"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_y:
                    str1 = list(name)
                    str1[pos] = "y"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_z:
                    str1 = list(name)
                    str1[pos] = "z"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_0:
                    str1 = list(name)
                    str1[pos] = "0"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_1:
                    str1 = list(name)
                    str1[pos] = "1"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_2:
                    str1 = list(name)
                    str1[pos] = "2"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_3:
                    str1 = list(name)
                    str1[pos] = "3"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_4:
                    str1 = list(name)
                    str1[pos] = "4"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_5:
                    str1 = list(name)
                    str1[pos] = "5"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_6:
                    str1 = list(name)
                    str1[pos] = "6"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_7:
                    str1 = list(name)
                    str1[pos] = "7"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_8:
                    str1 = list(name)
                    str1[pos] = "8"
                    name = "".join(str1)
                    pos = pos + 1
                if event.key == pygame.K_9:
                    str1 = list(name)
                    str1[pos] = "9"
                    name = "".join(str1)
                    pos = pos + 1
    pygame.display.update()
    k = cv2.waitKey(10)
    if k == 27:
        break

cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    # read image
    ret, img = cap.read()
    img = cv2.flip(img, 10)
    # get hand data from the rectangle sub window on the screen
    cv2.rectangle(img, (400, 400), (600, 200), (0, 255, 0), 0)
    h = 200
    w = 250
    x = 200
    y = 400
    crop_img = img[x:x + w, y:y + h]

    # convert to gray_scale
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

    # applying gaussian blur
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)

    # thresholdin: Otsu's Binarization method
    _, thresh1 = cv2.threshold(blurred, 127, 255,
                               cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # show thresholded image
    cv2.imshow('Thresholded', thresh1)

    # check OpenCV version to avoid unpacking error
    (version, _, _) = cv2.__version__.split('.')

    if version == '3':
        image, contours, hierarchy = cv2.findContours(thresh1.copy(),
                                                      cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    elif version == '4':
        contours, hierarchy = cv2.findContours(thresh1.copy(), cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_NONE)
    # find contour with max area
    cnt = max(contours, key = lambda x: cv2.contourArea(x))

    # create bounding rectangle around the contour (can skip below two lines)
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(crop_img, (x, y), (x+w, y+h), (0, 0, 255), 0)

    # finding convex hull
    hull = cv2.convexHull(cnt)

    # drawing contours
    drawing = np.zeros(crop_img.shape,np.uint8)
    cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 0)
    cv2.drawContours(drawing, [hull], 0,(0, 0, 255), 0)

    # finding convex hull
    hull = cv2.convexHull(cnt, returnPoints=False)

    # finding convexity defects
    defects = cv2.convexityDefects(cnt, hull)
    count_defects = 0
    cv2.drawContours(thresh1, contours, -1, (0, 255, 0), 3)

    # applying Cosine Rule to find angle for all defects (between fingers)
    # with angle > 90 degrees and ignore defects
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]

        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])

        # find length of all sides of triangle
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

        # apply cosine rule here
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57

        # ignore angles > 90 and highlight rest with red dots
        if angle <= 90:
            count_defects += 1
            cv2.circle(crop_img, far, 1, [0,0,255], -1)
        #dist = cv2.pointPolygonTest(cnt,far,True)

        # draw a line from start to end i.e. the convex points (finger tips)
        # (can skip this part)
        cv2.line(crop_img,start, end, [0,255,0], 2)
        #cv2.circle(crop_img,far,5,[0,0,255],-1)

    # define actions required
    if count_defects == 1:
        cv2.putText(img,"TWO", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 2:
        X = "THREE"
        cv2.putText(img, X, (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
    elif count_defects == 3:
        cv2.putText(img,"This is 4 :P", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 4:
        cv2.putText(img,"5!!!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    else:
        cv2.putText(img,"one!!!", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

    # show appropriate images in windows
    # cv2.imshow('Gesture', img)
    all_img = np.hstack((drawing, crop_img))
   #  cv2.imshow('Contours', all_img)

   #GAME PART STARTS BELOW

    player_it = player_it + 1
    enemy_it = enemy_it + 1

    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    if count_defects == 1:
        playerX_change = -5
    elif count_defects == 2:
        playerX_change = 5
    elif count_defects == 3:
        if bullet_state == "ready":
            bulletSound = mixer.Sound('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Musics\\bullet.wav')
            bulletSound.play()
            # Get the current x cordinate of the spaceship
            bulletX = playerX + 65
            fire_bullet(bulletX, bulletY)
    else:
        playerX_change = 0

    playerX += playerX_change
    if playerX <= -80:
        playerX = -80
    elif playerX >= 680:
        playerX = 680

    # Enemy Movement
    for i in range(num_of_enemies):

            # Game Over
            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                if g_o==1:
                    update_data_base(name, score_value)
                    g_o=0
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 7
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -7
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound('C:\\Users\\Nasif Imtiaj\\Documents\\Projects\\SBWHG\\Musics\\explosion.wav')
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], enemy_it % 54)

    # Bullet Movement
    if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

    if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

    player(playerX, playerY, player_it % 7)
    show_score(name,testY, textX)
    pygame.display.update()
    k = cv2.waitKey(10)
    if k == 27:
        break
    clock.tick(70)