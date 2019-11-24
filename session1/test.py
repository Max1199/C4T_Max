playerX = 3
playerY = 3


def printMap(side):

    for i in range (side):
        for j in range (side):
            if i==playerX and j==playerY :
                print("P", end="  ")
            else :
                print("*", end="  ")
        print()

def run():
        global playerX, playerY
        direct = input("your move: ")
        if direct.lower() == "w" :
            if playerX >0 :
                playerX -= 1
        elif direct.lower() == "s" :
            if playerX < 6 :
                playerX += 1
        elif direct.lower() == "a" :
            if playerY > 0 :
                playerY -= 1
        elif direct.lower() == "d" :
            if playerY < 6 :
                playerY += 1 
printMap(7)

while (True) :

    run()
  


    printMap(7)