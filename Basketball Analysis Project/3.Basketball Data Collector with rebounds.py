import pygame, sys
from pygame.locals import *

#Pygame Junk
pygame.init()
Display_Surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Basketball Data")
CourtImg = pygame.image.load("bb_court.jpg")
CourtImg = pygame.transform.scale(CourtImg, (700,600))
Green = (0, 255, 0)
Red = (255, 0, 0)
Yellow = (255,255,0)
White = (255, 255, 255)
Black = (0, 0, 0)
game_font = pygame.font.SysFont("arial", 64)
game_font2 = pygame.font.SysFont("arial", 14)
game_font3 = pygame.font.SysFont("arial", 16)

#Textfile Junk
filename = "FILENAME.txt"
TextFile = open(filename, "w")

#Variables
shot_scored = True
player_number = 00
reboundType = 0
rebound = False
shots_location = []
newPlayer = False
fouled = False
count = 0
colour = White

while True:
    #Get mouse position
    mouseX, mouseY = pygame.mouse.get_pos()
    if rebound:
        colour = Red
            
    #Paint Board
    Display_Surface.blit(CourtImg, (0, 0))
    pygame.draw.rect(Display_Surface, Green, (710, 20, 80, 55), 0)
    pygame.draw.rect(Display_Surface, Red, (710, 95, 80, 55), 0)
    pygame.draw.rect(Display_Surface, Yellow, (710, 170, 80, 55), 0)
    pygame.draw.rect(Display_Surface, White, (710, 350, 35, 35), 0)
    pygame.draw.rect(Display_Surface, White, (755, 350, 35, 35), 0)
    pygame.draw.rect(Display_Surface, Black, (680, 470, 120, 120), 0)
    pygame.draw.rect(Display_Surface, Black, (705, 317, 100, 20), 0)
    pygame.draw.rect(Display_Surface, colour, (725, 395, 50, 25), 0)

    text = game_font.render(str(player_number), True, White)
    text2 = game_font2.render("Def",True, Black)
    text3 = game_font2.render("Off",True, Black)
    text4 = game_font3.render("Current Player",True, White)
    text5 = game_font3.render("Rebounds",True, White)
    text6 = game_font3.render("Fouled",True, Black)
    text7 = game_font3.render("Enter",True, Black)
    
    Display_Surface.blit(text,(710, 510))
    Display_Surface.blit(text2,(713,355))
    Display_Surface.blit(text3,(759,355))
    Display_Surface.blit(text4,(690,485))
    Display_Surface.blit(text5,(710,320))
    Display_Surface.blit(text6,(722,187))
    Display_Surface.blit(text7,(730,400))
    
    #Paint Shots
    for shot in shots_location:           
        if shot[2] == 0:
            pygame.draw.circle(Display_Surface, Red, (shot[0], shot[1]), 10, 0)
        elif shot[2] == 1:
            pygame.draw.circle(Display_Surface, Green, (shot[0], shot[1]), 10, 0)
        else:
            pygame.draw.circle(Display_Surface, Yellow, (shot[0], shot[1]), 10, 0)
        
    if fouled:
        pygame.draw.rect(Display_Surface, Yellow, (710, 245, 80, 55), 0)        
    elif shot_scored:
        pygame.draw.rect(Display_Surface, Green, (710, 245, 80, 55), 0)
    else:
        pygame.draw.rect(Display_Surface, Red, (710, 245, 80, 55), 0)
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if 710<mouseX<787 and 20<mouseY<75:
                    shot_scored = True
                    fouled = False
                elif 710<mouseX<787 and 95<mouseY<150:
                    shot_scored = False
                    fouled = False
                elif 710<mouseX<787 and 170<mouseY<225:
                    fouled = True
                    shot_scored = False
                elif 710<mouseX<745 and 350<mouseY<385:
                    rebound = True
                    reboundType = 1
                elif 755<mouseX<790 and 350<mouseY<385:
                    rebound = True
                    reboundType = 2
                elif 725<mouseX<775 and 395<mouseY<420:                   
                    TextFile.write(str(0) +"," + str(0) + "," + str(player_number) + "," + str(3) +"," +str(reboundType) +"\n")
                    rebound = False
                    colour = White
                
                elif 0<mouseX<674 and 20<mouseY<588:
                    if shot_scored:
                        TextFile.write(str(mouseX) + "," + str(mouseY) + "," + str(player_number) + "," + str(1) +"\n")
                        temp_array = [mouseX, mouseY, 1]
                        shots_location.append(temp_array)
                    elif fouled:
                        TextFile.write(str(mouseX) + "," + str(mouseY) + "," + str(player_number) + "," + str(2) +"\n")
                        temp_array = [mouseX, mouseY, 2]
                        shots_location.append(temp_array)
                    else:
                        TextFile.write(str(mouseX) + "," + str(mouseY) + "," + str(player_number) + "," + str(0) +"\n")
                        temp_array = [mouseX, mouseY, 0]
                        shots_location.append(temp_array)

        if event.type == KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RIGHT:
                        player_number += 1

                    if event.key == K_LEFT:
                        if player_number == 0:
                            player_number = 0
                        else:
                            player_number -= 1
                            
        if event.type == QUIT:
            TextFile.close()
            pygame.quit()
            sys.exit()
                    
                    
    # update the display window
    pygame.display.update()




