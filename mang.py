import pygame, sys
from random import randint
pygame.init()

pygame.mixer.music.load("backgroundmusic.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.75)

background = pygame.image.load("taustakas.png")
background = pygame.transform.scale(background, (1280, 720))


moneySound = pygame.mixer.Sound("money.mp3")

ekraan = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Troll kulda varastamas")


pilt = pygame.image.load("troll.png")
pilt = pygame.transform.scale(pilt, (200, 179))

pilt2 = pygame.image.load("goldcoin.png")
pilt2 = pygame.transform.scale(pilt2, (100, 100))



#tegelase atribuudid
x = 200
y = 200
samm = 10
pygame.key.set_repeat(1,10)

#kuldse mundi atribuudid
x2 = randint(0, 1180)
y2 = randint(100, 620)

#mangu oleku determinerid
running = True
menu = True
game = False
scoreboard = False

#fondid
bigFont = pygame.font.SysFont("Corbel", 35)
smallFont = pygame.font.SysFont("Corbel", 20)

#raha
raha = 100
maxRaha = 100

while running:
    
    #menuu
    while menu:
        ekraan.fill([19, 138, 51])
        ekraan.blit(pilt, (500,100))
        
        #start nupp
        text = bigFont.render("START", True, [0, 0, 0])
        pygame.draw.rect(ekraan, [255, 225, 255], [500, 300, 200, 80], 0)
        ekraan.blit(text, (550, 325))
        
        #valju nupp
        text = bigFont.render("EXIT", True, [0, 0, 0])
        pygame.draw.rect(ekraan, [255, 225, 255], [500, 400, 200, 80], 0)
        ekraan.blit(text, (565, 425))
        
        #seletav tekst
        text = smallFont.render("In order to win the game you have to make trolls bank account grow by feeding it with coins appearing on the screen.", True, [255, 255, 255])
        ekraan.blit(text, (190, 500))
        
        text = smallFont.render("You are given one minute to gather as much money as possible, but be awared that the more money you have the harder it gets.", True, [255, 255, 255])
        ekraan.blit(text, (140, 530))
        
        
        pygame.display.flip()
        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN:
                hiir_x, hiir_y = i.pos
                
                #exit button
                if 500 <= hiir_x <= 700 and 400 <= hiir_y <= 480:
                    running = False
                    menu = False
                #start button
                elif 500 <= hiir_x <= 700 and 300 <= hiir_y <= 380:
                    menu = False
                    game = True
                
            elif i.type == pygame.QUIT:
                running = False
                menu = False
                
    start_ticks = pygame.time.get_ticks()
    while game:        
        #raha counter
        textToDisplay = "Money in the bank: " + str(round(raha))
        text = bigFont.render(textToDisplay, True, [255, 255, 255])
    
        textToDisplay2 = "Highscore: " + str(round(maxRaha))
        text2 = bigFont.render(textToDisplay2, True, [255, 255, 255])
        
        textToDisplay3 = "Time left: " + str(round(60 - (pygame.time.get_ticks() - start_ticks)/ 1000))
        text3 = bigFont.render(textToDisplay3, True, [255, 255, 255])
    
        #mang ise
        
                
        ekraan.fill([19, 138, 51])
        ekraan.blit(background, (0, 0))
        ekraan.blit(text, (20, 20))
        ekraan.blit(text2, (20, 50))
        ekraan.blit(text3, (20, 80))
        ekraan.blit(pilt2, (x2, y2))
        ekraan.blit(pilt, (x,y))
        pygame.display.flip()
    
        if raha > maxRaha:
            maxRaha = raha
    
        if raha < 100:
            raha -= 0.025
        elif raha < 200:
            raha -= 0.05
        else:
            raha -= 0.075
        
        if 60 - (pygame.time.get_ticks() - start_ticks)/ 1000 < 1:
            game = False
            menu = True
            scoreboard = True
    
    
        #kui saab mundi katte
        if x - 10 <= x2 + 25 <= x + 210 and y - 10 <= y2 + 25 <= y + 200:
            pygame.mixer.Sound.play(moneySound)
            x2 = randint(0, 1180)
            y2 = randint(100, 620)
            raha += 20
        

    
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
                game = False
            # Kui sündmuseks on klahvi allavajutamine…
            elif i.type == pygame.KEYDOWN:
                # ... ja klahviks on nooleklahv üles liikumiseks,...
                if i.key == pygame.K_UP and y >= 10:
                     # ... siis vähendame y-koordinaati
                     y = y - samm
                elif i.key == pygame.K_DOWN and y <= 530:
                     y = y + samm
                elif i.key == pygame.K_LEFT and x >= 10:
                    x = x - samm
                elif i.key == pygame.K_RIGHT and x <= 1070:
                    x = x + samm
        #mundi liikumine
        pygame.time.delay(5)
        if raha < 200:
            y2 -= 1.5
        elif raha < 400:
            y2 -= 1.75
        elif raha < 700:
            y2 -= 2
        else:
            y2 -= 2.25
        
    
        if y2 < -100:
            pygame.time.delay(50)
            x2 = randint(0, 1180)
            y2 = randint(0, 620)
    while scoreboard:
        textToDisplay = "U scored: " + str(round(maxRaha)) + " points"
        text = bigFont.render(textToDisplay, True, [255, 255, 255])
  
        ekraan.fill([19, 138, 51])
        ekraan.blit(text, (480, 250))
        
        text = bigFont.render("OK", True, [0, 0, 0])
        pygame.draw.rect(ekraan, [255, 225, 255], [500, 300, 200, 80], 0)
        ekraan.blit(text, (565, 325))
        
        pygame.display.flip()
        
        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN:
                hiir_x, hiir_y = i.pos
                #OK button
                if 500 <= hiir_x <= 700 and 300 <= hiir_y <= 380:
                    menu = True
                    scoreboard = False
                    raha = 100
                    maxRaha = raha
            elif i.type == pygame.QUIT:
                running = False
                scoreboard = False
                
                
                
            
                
        
pygame.quit()