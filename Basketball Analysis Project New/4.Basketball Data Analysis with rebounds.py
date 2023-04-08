import pygame, sys
from pygame.locals import *
  
#Pygame Junk
pygame.init()
Display_Surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Basketball Data Analysis in Pygame")
CourtImg = pygame.image.load("bb_court.jpg")
CourtImg = pygame.transform.scale(CourtImg, (700,600))
Green = (0, 255, 0)
Red = (255, 0, 0)
White = (255, 255, 255)
Black = (0, 0, 0)
Yellow = (255,255,0)
game_font = pygame.font.SysFont("arial", 32)

#Textfile Junk - Will need to be updated manually
f1 = "FILE NAME"
f2 = "FILE NAME"

docs = [f1,f2]

#Variables
shots = []
Rshots = []
rebounds = []
Rrebounds = []
defRebound = 0
offRebound = 0
ngames = "All"
players = "All"

for x in range(len(docs)):
    TextFile = open(docs[x], "r")
    for line in TextFile:
        line = line.split(',')
        #If it's a rebound and not a shot
        if int(line[3]) == 3:
            player_number = int(line[2])
            reboundType = int(line[4].rstrip())
            temp_array = [player_number, reboundType]
            rebounds.append(temp_array)
            if x == len(docs) - 1:
                Rrebounds.append(temp_array)
            if int(line[4]) == 1:
                defRebound += 1
            else:
                offRebound += 1
        else:
            pos_x = int(line[0])
            pos_y = int(line[1])
            player_number = int(line[2])
            shot_scored = int(line[3].rstrip())
            temp_array = [pos_x, pos_y, player_number, shot_scored]
            shots.append(temp_array)
            if x == len(docs) - 1:
                Rshots.append(temp_array)
            
    TextFile.close()

#Shot statistics

print("For these stats any shot taken where they were fouled that resulted in a missed shot")
print("are only counted as fouls drawn and not a missed shot. If fouled and the shot goes in")
print("they are counted as a regular made shot. Only Fouls on shots are counted here.\n")

print("Shot Statistics Latest Game")
print("--------------------------------------------------------------------------------------\n")

shots_total = 0
shots_count = 0
fouls = 0
active_players = []
for shot in Rshots:
    #Overall
    if shot[3]==2:
        fouls += 1
    else:
        shots_total += int(shot[3])
        shots_count += 1

#Gathering Active Players
    player_in_list = False
    for x in active_players:
        if x[0] == shot[2]:
            player_in_list = True
            
    #Temperary array [number, shots taken, shots made, fould, def rebounds, off rebounds]
    if not(player_in_list):
        temp_array = [shot[2], 0, 0, 0, 0, 0]
        active_players.append(temp_array)

for rebound in Rrebounds:
    player_in_list = False
    for x in active_players:
        if x[0] == rebound[0]:
            player_in_list = True
            
    #Temperary array [number, shots taken, shots made, fould, def rebounds, off rebounds]
    if not(player_in_list):
        temp_array = [rebound[0], 0, 0, 0, 0, 0]
        active_players.append(temp_array)

#Gathering Players' stats
for shot in Rshots:
    for x in range(len(active_players)):
        if active_players[x][0] == shot[2]:
            if shot[3] == 2:
                active_players[x][3] += 1
            else:
                active_players[x][1] += int(shot[3])
                active_players[x][2] += 1

for rebound in Rrebounds:
    for x in range(len(active_players)):
        if active_players[x][0] == rebound[0]:
            if rebound[1] == 1:
                active_players[x][4] += 1
            else:
                active_players[x][5] += 1

active_players.sort()

#Print the stats
if shots_count != 0:
    print("Team Average: "+str(int(round((shots_total/shots_count),2)*100))+ "%")
print("Shots taken:", shots_count)
print("Fouls Drawn:", fouls)
print("Defensive Rebound: ", defRebound)
print("Offensive Rebounds: ", offRebound,"\n")

#Printing individual stats
print("Player \tShots Taken \tAverage \tFouls Drawn \tDef Rebounds \tOff Rebounds")
for player in active_players:
    if player[2] == 0:
        average = 0
    else:
        average = round((player[1]/player[2])*100)
    print(str(player[0]), "\t"+str(player[2]), "\t\t"+str(average)+ "% ","\t\t"+str(player[3]),"\t\t"+str(player[4]),"\t\t"+str(player[5]))

#Now Doing the exact same thing but all all games instead of just the most recent games
shots_total = 0
shots_count = 0
fouls = 0
active_players = []
for shot in shots:
    #Overall
    if shot[3]==2:
        fouls += 1
    else:
        shots_total += int(shot[3])
        shots_count += 1

#Gathering Active Players
    player_in_list = False
    for x in active_players:
        if x[0] == shot[2]:
            player_in_list = True
            
    #Temperary array [number, shots taken, shots made, fould, def rebounds, off rebounds]
    if not(player_in_list):
        temp_array = [shot[2], 0, 0, 0, 0, 0]
        active_players.append(temp_array)

for rebound in rebounds:
    player_in_list = False
    for x in active_players:
        if x[0] == rebound[0]:
            player_in_list = True
            
    #Temperary array [number, shots taken, shots made, fould, def rebounds, off rebounds]
    if not(player_in_list):
        temp_array = [rebound[0], 0, 0, 0, 0, 0]
        active_players.append(temp_array)

#Gathering Players' stats
for shot in shots:
    for x in range(len(active_players)):
        if active_players[x][0] == shot[2]:
            if shot[3] == 2:
                active_players[x][3] += 1
            else:
                active_players[x][1] += int(shot[3])
                active_players[x][2] += 1

for rebound in rebounds:
    for x in range(len(active_players)):
        if active_players[x][0] == rebound[0]:
            if rebound[1] == 1:
                active_players[x][4] += 1
            else:
                active_players[x][5] += 1

active_players.sort()

#Print the stats
print("\n\nYear Long Cumulative Stats")
if shots_count != 0:
    print("Team Average: "+str(int(round((shots_total/shots_count),2)*100))+ "%")
print("Shots taken:", shots_count)
print("Fouls Drawn:", fouls)
print("Defensive Rebound: ", defRebound)
print("Offensive Rebounds: ", offRebound,"\n")

#Printing individual stats
print("Player \tShots Taken \tAverage \tFouls Drawn \tDef Rebounds \tOff Rebounds")
for player in active_players:
    if player[2] == 0:
        average = 0
    else:
        average = round((player[1]/player[2])*100)
    print(str(player[0]), "\t"+str(player[2]), "\t\t"+str(average)+ "% ","\t\t"+str(player[3]),"\t\t"+str(player[4]),"\t\t"+str(player[5]))

#Everything below this is for the plots#

selection = 1

while True:
#Shot Distribution
    if selection == 1:
        colour1 = Red
        colour2 = White
    else:
        colour1 = White
        colour2 = Red
        
    Display_Surface.blit(CourtImg, (0, 0))

    pygame.draw.rect(Display_Surface, Black, (680, 40, 120, 400), 0)
    text1 = game_font.render(ngames, True,White)
    Display_Surface.blit(text1, (690,90))
    
    text2 = game_font.render(str(players), True,White)
    Display_Surface.blit(text2, (690,190))

    text3 = game_font.render("Games", True,colour1)
    Display_Surface.blit(text3, (690,50))
    
    text4 = game_font.render("Players", True,colour2)
    Display_Surface.blit(text4, (690,150))
   
    if ngames == "All":
        choice = shots
    else:
        choice = Rshots
          
    for shot in choice:
        if players == "All":
            if int(shot[3]) == 1:
                pygame.draw.circle(Display_Surface, Green, (int(shot[0]), int(shot[1])), 8, 0)
            elif int(shot[3]) == 0:
                pygame.draw.circle(Display_Surface, Red, (int(shot[0]), int(shot[1])), 8, 0)
            else:
                pygame.draw.circle(Display_Surface, Yellow, (int(shot[0]), int(shot[1])), 8, 0)
        else:
            if int(shot[2]) == players:
                if int(shot[3]) == 1:
                    pygame.draw.circle(Display_Surface, Green, (int(shot[0]), int(shot[1])), 8, 0)
                elif int(shot[3]) == 0:
                    pygame.draw.circle(Display_Surface, Red, (int(shot[0]), int(shot[1])), 8, 0)
                else:
                    pygame.draw.circle(Display_Surface, Yellow, (int(shot[0]), int(shot[1])), 8, 0)
            
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                if selection == 1:
                    if ngames == "All":
                        ngames = "Last"
                    else:
                        ngames = "All"
                else:
                    if players == "All":
                        players = 0
                    else:
                        players += 1

            if event.key == K_LEFT:
                if selection == 1:
                    if ngames == "All":
                        ngames = "Last"
                    else:
                        ngames = "All"
                else:
                    if players == "All" or players == 0:
                        players = "All"
                    else:
                        players -= 1
                    
            if event.key == K_UP:
                selection = 1

            if event.key == K_DOWN:
                selection = 2
                
                           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
