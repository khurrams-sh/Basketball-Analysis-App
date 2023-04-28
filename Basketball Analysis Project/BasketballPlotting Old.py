#Volleyball Plotting

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#loading the image of the court for the background of the plot
court = mpimg.imread('bb_court.png')

#opening point documents
f1 = open("FILENAME.txt", "r")

#making a list of text files to extract data points from
docs = [f1]

#initializing lists and variables
xCoords = []
yCoords = []
playerNums = []
makeMiss = []
   
#Extracting data from each text file in the document lists
for f in docs:
    
    #Reading first line
    point = f.readline()
 
    #Adding all the points to their respective lists at interger values
    while point != "":
        point = point.split(',')
        for x in range(0,4):
            point[x] = int(point[x])
            if x == 0:
                xCoords.append(point[x])
            elif x == 1:
                yCoords.append(point[x])
            elif x == 2:
                playerNums.append(point[x])
            else:
                makeMiss.append(point[x])
        point = f.readline()

    f.close()

again = 'y'
print(playerNums)
while again == 'y':
    #What would the user like to plot
    nGames = 0
    player = input("Enter A for all players or P to choose a player ").upper()
    if player == "P":
        nPlayer = int(input("What player would you like to see? "))
        
    if player == "A":
        for x in range(0,len(xCoords)):
            if makeMiss[x] == 0:
                C = 'red'
            else: 
                C = 'green'
            plt.scatter(xCoords[x],yCoords[x],color= C)

    else:
        for x in range(0,len(xCoords)):
            if playerNums[x] == nPlayer:
                if makeMiss[x] == 0:
                    C = 'red'
                else: 
                    C = 'green'
                plt.scatter(xCoords[x],yCoords[x],color= C)

    imgplot = plt.imshow(court)
    plt.show()

    again = input("Would you like to generate another graph?(y/n) ").lower()
    plt.gcf().clear()


