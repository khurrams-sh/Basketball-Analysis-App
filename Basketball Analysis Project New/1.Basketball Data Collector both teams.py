import pygame, sys
from pygame.locals import *

#Pygame Junk
pygame.init()
Display_Surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Basketball Data")
CourtImg = pygame.image.load("Full Court.jpg")
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
filename = "FILE NAME"
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
                   
    #Paint Board
    Display_Surface.blit(CourtImg, (0, 0))
    pygame.draw.rect(Display_Surface, Green, (710, 20, 80, 55), 0)
    pygame.draw.rect(Display_Surface, Red, (710, 95, 80, 55), 0)
    pygame.draw.rect(Display_Surface, Yellow, (710, 170, 80, 55), 0)
    pygame.draw.rect(Display_Surface, Black, (710, 420, 80, 120), 0)
    pygame.draw.rect(Display_Surface, Black, (705, 317, 100, 20), 0)
    

    text = game_font.render(str(player_number), True, White)
    text2 = game_font3.render("Home",True, Black)
    text3 = game_font3.render("Away",True, Black)
    text4 = game_font3.render("Player",True, White) 
    text6 = game_font3.render("Fouled",True, Black)
    
    Display_Surface.blit(text,(720, 460))
    Display_Surface.blit(text2,(55, 70))
    Display_Surface.blit(text3,(605, 70))
    Display_Surface.blit(text4,(725,440))
    Display_Surface.blit(text6,(722,187))
    
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
                    shot_scored = False
                    fouled = True
                
                elif 0<mouseX<674 and 20<mouseY<588:
                    if 40<mouseX<348:
                        team = 1
                    else:
                        team = 2
                        
                    if shot_scored:
                        TextFile.write(str(mouseX) + "," + str(mouseY) + "," + str(player_number) + "," + str(1) + "," + str(team)+"\n")
                        temp_array = [mouseX, mouseY, 1]
                        shots_location.append(temp_array)
                    elif fouled:
                        TextFile.write(str(mouseX) + "," + str(mouseY) + "," + str(player_number) + "," + str(2) + "," + str(team)+"\n")
                        temp_array = [mouseX, mouseY, 2]
                        shots_location.append(temp_array)
                    else:
                        TextFile.write(str(mouseX) + "," + str(mouseY) + "," + str(player_number) + "," + str(0) + "," + str(team)+"\n")
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




