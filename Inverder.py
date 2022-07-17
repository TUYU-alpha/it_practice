import pygame
from pygame import mixer
import random
import math

#pygameの初期化（必須）
pygame.init()

#画面サイズの指定
screen = pygame.display.set_mode((800, 600))

#画面の配色を指定
#screen.fill((150, 150, 150))

#ウィンドウ名を指定
pygame.display.set_caption('Inveders Game')

#プレイヤーイメージの読み込み
playerImg =pygame.image.load('player.png')

#プレイヤーイメージを設置する座標変数の指定
playerX, playerY = 370, 480

#横移動（X軸）変化初期値指定
playerX_change = 0

#敵（エネミー）を設定
enemyImg =pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change, enemyY_change = 1, 40

#bullet
bulletImg =pygame.image.load('bullet.png')
bulletX, bulletY =0, 480
bulletX_change, bulletY_change = 0, 0.3
bullet_state = 'ready'

#音声の出力をさせる
#mixer.Sound('laser.wav').play()

score_value = 0

def player(x, y):
    #プレイヤーイメージを表示させる
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    #プレイヤーイメージを表示させる
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    #バレットが表示されている間「fire」に変更
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

#ゲーム開始時にアクティブにさせる
running = True

#ゲームの起動時間を定義（Falseに変更で終了）
while running:

    #背景を常に更新
    screen.fill((0, 0, 0))

    #何かイベントを起こすまで続ける
    for event in pygame.event.get():

        #ゲームを「閉じる」時に条件変化
        if event.type == pygame.QUIT:
            running = False

        #何かキーを押した時に条件変化
        if event.type == pygame.KEYDOWN:

            #左キー押したら左へ
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1

            #右キー押したら右へ
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        #キーから手を離したら変化を止める
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #Player
    playerX += playerX_change

    #画面端から先(画面外)へいかないようにする
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #Enemy
    if enemyY > 440:
        break
    enemyX += enemyX_change

    #左端に来たら一段下げて右へ移動
    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change

    #右端に来たら一段下げて左へ移動
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = 'ready'
        score_value += 1
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50,150)

    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -=bulletY_change

    #Score
    font = pygame.font.SysFont(None,32)
    message = font.render(f"Score: {str(score_value)}", True, (255, 255, 255))
    screen.blit(message, (20, 50))

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    #ゲームを起動している間は常に情報更新
    pygame.display.update()
