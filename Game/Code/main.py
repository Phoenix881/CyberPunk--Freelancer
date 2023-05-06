# Импортирование нужных библиотек и скриптов
import pygame
import data
import time
from pygame import mixer
from random import randint
from os import remove
import datetime



# Initialization of the pygame
pygame.init()
clock = pygame.time.Clock()

# Setting width and heigh of the games window and creating it
screenSize = (1280, 720) # 1280x720
screen = pygame.display.set_mode(screenSize)

# # Timer
# fontTimer = pygame.font.Font("Project/Game/Font-futuremillennium/FutureMillennium Italic.ttf", 14)
# timeStart = time.time() # Starting time in second
# timeEnd = int(timeStart) + (3*60) # Starting time in second plus 3 minutes
# def timer3M(x, y):
#     startTime = int(time.time())
#     flag = True
#     while flag:
#         nowTime = int(time.time())
#         secondsPassed = nowTime - startTime
#         if secondsPassed == 180:
#             flag = False
#             break
#         m, s = divmod(secondsPassed, 60)
#         timer = fontTimer.render(f"Timer 3:00 - {2-m}:{59-s}", True, "black")
#         screen.blit(timer, (x, y))



# Icon and title
pygame.display.set_caption("CyberPunk--Freelancer")
icon = pygame.image.load(data.ICON)
pygame.display.set_icon(icon)



# Generating random number for showing random background
randomBackground = randint(0, 3)
background = pygame.image.load(data.BACKGROUNDS[randomBackground])
background = pygame.transform.scale(background, screenSize)

# Adding background music
mixer.music.load("Game/Music/backgroundMusic.mp3")
mixer.music.play(-1)

# Adding player
playerSprite = [] # List of locations of choisen character's files

settingsFile = open("Game/settings.txt"); settings = []
settings = settingsFile.readlines() # Open file with settings, and assign its content to a python list

# Check what path-list is needed
if settings[1] == "Character(Cyborg/Punk/Biker): Cyborg\n":
    playerSprite = data.CYBORG[:]
if settings[1] == "Character(Cyborg/Punk/Biker): Punk\n":
    playerSprite = data.PUNK[:]
if settings[1] == "Character(Cyborg/Punk/Biker): Biker\n":
    playerSprite = data.BIKER[:]

diffucultyLevel = settings[2] # First line is instructions; second - character; third - difficulty
playerCoordinates = (495, 400); playerSize = (129, 148) # Player's coordinates(location) and size
player = pygame.transform.scale(pygame.image.load(playerSprite[0]), playerSize) #Starting image of a character
playerDownLeft = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)
playerDownRight = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)
playerUpLeft = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)
playerUpRight = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)



# Score and lifes
# 
# Every task - 10 points
# Every risky task - 50 points
# At the easy-mode the player has 5 lifes; at other modes - 3
score = 0
if diffucultyLevel == "Difficulty(Easy/Average/Hard): Easy":
    lifes = 5
if diffucultyLevel == "Difficulty(Easy/Average/Hard): Average" or diffucultyLevel == "Difficulty(Easy/Average/Hard): Hard":
    lifes = 3
fontScore = pygame.font.Font(data.ITALIC_FONT, 30)
fontLifes = pygame.font.Font(data.ITALIC_FONT, 16)
fontBestScore = pygame.font.Font(data.ITALIC_FONT, 14)
def showScore(x, y, points):
    score = fontScore.render(f"Score: {points}", True, "black") 
    screen.blit(score, (x, y))
def showLifes(x, y, numOfRemaing):
    lifes = fontLifes.render(f"Lifes: {numOfRemaing}", True, "black")
    screen.blit(lifes, (x, y))



# Best score
bestScoreFile = open("Game/Code/score.txt", "r"); bestScoreFileLines = []
bestScoreFileLines = bestScoreFile.readlines()
BS_score = bestScoreFileLines[1]; BS_score = int(BS_score[12:])
BS_dataFile = bestScoreFileLines[2]
BS_data = BS_dataFile[6:16]
BS_time = BS_dataFile[17:]
bestScoreFile.close()
def showBestScore(x, y):
    lifes = fontLifes.render(f"Best score[{BS_data}, {BS_time}]: {BS_score}", True, "black")
    screen.blit(lifes, (x, y))



# Debt
debtFont = pygame.font.Font(data.BASIC_FONT, 14)
def haveDebt(x, y):
    debt = debtFont.render("Debt: 200$", True, "black")
    screen.blit(debt, (x, y))

playedSuccesSound = False
def noDebt(x, y):
    global playedSuccesSound
    if playedSuccesSound == False:
        payed = mixer.Sound("Game/Music/debtPayed.wav")
        payed.play()
        playedSuccesSound = True
    debt = debtFont.render("Debt: payed", True, "black")
    screen.blit(debt, (x, y))

# Game Over text
playedGameOverSound = False
gameOverFont = pygame.font.Font(data.BOLD_FONT, 146)
def game_over_text():
    global playedGameOverSound
    if playedGameOverSound == False:
        gameOverSound = mixer.Sound("Game/Music/gameOver.mp3")
        gameOverSound.play()
        playedGameOverSound = True
    gameOver = gameOverFont.render("GAME OVER", True, "black")
    screen.blit(gameOver, (200, 300))



# Adding drones
#
# Add first drone
droneOneX = 440; droneOneY = 390; droneOneSize = (73, 71)
droneOne = pygame.transform.scale( pygame.image.load(data.DRONES[0]),  droneOneSize)
# Add second drone
droneTwoX = 420; droneTwoY = 440; droneTwoSize = (71, 71)
droneTwo = pygame.transform.scale(pygame.image.load(data.DRONES[1]), droneTwoSize)
# Add third drone
droneThreeX = 620; droneThreeY = 440
droneThree = pygame.transform.scale(pygame.image.load(data.DRONES[2]), droneTwoSize)
# Add fourth drone
droneFourX = 590; droneFourY = 390
droneFour = pygame.transform.scale( pygame.image.load(data.DRONES[3]), droneOneSize )



# Prepare hidden tasks and risky tasks - and to show them we will be just changing their images
# from transparent to visible
# First I define sizes of average tasks and risky ones
# Then I define positions of each drone
tasksSize = (30, 30.25); riskySize = (36, 36)
droneOneTaskCoordinates = (495, 430)    # First task
droneOneTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
droneTwoTaskCoordinates = (480, 480)    # Second task                         
droneTwoTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize)
droneThreeCoordinates = (600, 480)      # Third task
droneThreeTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize)
droneFourCoordinates = (585, 430)       # Fourth task
droneFourTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize)
droneOneRiskyCoordinates = (495, 430)   # First risky task
droneOneRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize)
droneTwoRiskyCoordinates = (480, 480)   # Second risky task
droneTwoRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize)
droneThreeRiskyCoordinates = (600, 480) # Third risky task
droneThreeRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize)
droneFourRiskyCoordinates = (585, 430) # Fourth risky task
droneFourRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize)



player = pygame.transform.scale(pygame.image.load(playerSprite[0]), playerSize)
lastImg = playerSprite[0]
# Main game cycle
running = True; isInDebt = True
while running:
    # Set FPS
    clock.tick(60)
    # Draw everything
    # Draw background 
    screen.blit(background, (0, 0))

    # If player is out of lifes
    if lifes == 0:
        # gameOverFont = pygame.font.Font(data.BOLD_FONT, 146)
        # gameOver = gameOverFont.render("GAME OVER", True, "black")
        # screen.blit(gameOver, (200, 300))   
        game_over_text()
        for event in pygame.event.get():
            # If user closes the game - close the game
            if event.type == pygame.QUIT:
                running = False
                break
    else: # If he have lifes - game continues on
        # Draw player's starting view

        player = pygame.transform.scale(pygame.image.load(lastImg), playerSize)
        
        screen.blit(player, playerCoordinates)

        # Draw drones
        screen.blit(droneOne, (droneOneX, droneOneY))
        screen.blit(droneTwo, (droneTwoX, droneTwoY))
        screen.blit(droneThree, (droneThreeX, droneThreeY))
        screen.blit(droneFour, (droneFourX, droneFourY))

        # Draw average tasks
        screen.blit(droneOneTask, droneOneTaskCoordinates)
        screen.blit(droneTwoTask, droneTwoTaskCoordinates)
        screen.blit(droneThreeTask, droneThreeCoordinates)
        screen.blit(droneFourTask, droneFourCoordinates)

        # Draw risky tasks
        screen.blit(droneOneRisky, droneOneRiskyCoordinates)
        screen.blit(droneTwoRisky, droneTwoRiskyCoordinates)
        screen.blit(droneThreeRisky, droneThreeRiskyCoordinates)
        screen.blit(droneFourRisky, droneFourRiskyCoordinates)



        # States of the sprite. For now users haven't moved yet
        droneTwoPressed = False
        droneThreePressed = False
        droneOnePressed = False
        droneFourPressed = False



        # Where task appeared
        taskPositionOne = False
        taskPositionTwo = False
        taskPositionThree = False
        taskPositionFour = False

        # If was generated risky task
        isRisky = False



        # RANDOMIZATION
        randomDrone = randint(1, 4) # Pick a random drone which will "give" players a task
        riskyProbability = randint(1, 4) # Probability of a risky work is 25%
        if riskyProbability == 1:
            if randomDrone == 1: # Show task near the drone one; hide tasks near other drones
                droneOneRisky = pygame.transform.scale(pygame.image.load(data.RISKY_WORK), riskySize) 
                droneTwoRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneThreeRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneFourRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize)

                droneOneTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneTwoTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneThreeTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneFourTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize)

                taskPositionOne = True
                isRisky = True
                pygame.time.delay(500)
            if randomDrone == 2: # Show task near the drone two; hide tasks near other drones
                droneOneRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneTwoRisky = pygame.transform.scale(pygame.image.load(data.RISKY_WORK), riskySize) 
                droneThreeRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneFourRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize)

                droneOneTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneTwoTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneThreeTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneFourTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize)

                taskPositionTwo = True
                isRisky = True
                pygame.time.delay(500)
            if randomDrone == 3: # Show task near the drone three; hide tasks near other drones
                droneOneRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneTwoRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneThreeRisky = pygame.transform.scale(pygame.image.load(data.RISKY_WORK), riskySize) 
                droneFourRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize)

                droneOneTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneTwoTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneThreeTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneFourTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize)

                taskPositionThree = True
                isRisky = True
                pygame.time.delay(500)
            if randomDrone == 4: # Show task near the drone four; hide tasks near other drones
                droneOneRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneTwoRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneThreeRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneFourRisky = pygame.transform.scale(pygame.image.load(data.RISKY_WORK), riskySize)

                droneOneTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneTwoTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneThreeTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneFourTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize)

                taskPositionFour = True
                isRisky = True
                pygame.time.delay(500)
        else:
            if randomDrone == 1: # Show task near the drone one; hide tasks near other drones
                droneOneTask = pygame.transform.scale(pygame.image.load(data.AVERAGE_WORK), tasksSize) 
                droneTwoTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneThreeTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneFourTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize)

                droneOneRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneTwoRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneThreeRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneFourRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize)

                taskPositionOne = True
                pygame.time.delay(500)
            if randomDrone == 2: # Show task near the drone two; hide tasks near other drones
                droneOneTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneTwoTask = pygame.transform.scale(pygame.image.load(data.AVERAGE_WORK), tasksSize) 
                droneThreeTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneFourTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize)

                droneOneRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneTwoRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneThreeRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneFourRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize)

                taskPositionTwo = True
                pygame.time.delay(500)
            if randomDrone == 3: # Show task near the drone three; hide tasks near other drones
                droneOneTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneTwoTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneThreeTask = pygame.transform.scale(pygame.image.load(data.AVERAGE_WORK), tasksSize) 
                droneFourTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize)

                droneOneRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneTwoRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneThreeRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneFourRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize)

                taskPositionThree = True
                pygame.time.delay(500)
            if randomDrone == 4: # Show task near the drone four; hide tasks near other drones
                droneOneTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneTwoTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneThreeTask = pygame.transform.scale(pygame.image.load(data.CLOAK), tasksSize) 
                droneFourTask = pygame.transform.scale(pygame.image.load(data.AVERAGE_WORK), tasksSize)

                droneOneRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneTwoRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneThreeRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize) 
                droneFourRisky = pygame.transform.scale(pygame.image.load(data.CLOAK), riskySize)

                taskPositionFour = True
                pygame.time.delay(500)
        


        # Check что там юзер жамкает на клаве
        for event in pygame.event.get():
            # If user closes the game - close the game
            if event.type == pygame.QUIT:
                running = False
                break

            # Check if any key is pressed
            if event.type == pygame.KEYDOWN:
                # Check which one is pressed and then change sprite's apperiance 
                # 0 - idle; 1 - down right; 2 - down left; 3 - up right; 4 - up left

                # Key W -> Up left
                if event.key == pygame.K_w: 
                    player = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)
                
                    playerDownLeft = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)
                    playerDownRight = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)
                    playerUpRight = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)

                    playerUpLeft = pygame.transform.scale(pygame.image.load(playerSprite[4]), (129, 148))
                    lastImg = playerSprite[4]
                    screen.blit(playerUpLeft, playerCoordinates)
                    droneOnePressed = True

                # Key S -> Down left
                if event.key == pygame.K_s:
                    player = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)

                    playerDownRight = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)
                    playerUpLeft = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)
                    playerUpRight = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)

                    playerDownLeft = pygame.transform.scale(pygame.image.load(playerSprite[2]), (110, 148))
                    lastImg = playerSprite[2]
                    screen.blit(playerDownLeft, playerCoordinates)
                    droneTwoPressed = True

                # Key L -> Down right
                if event.key == pygame.K_l:
                    player = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)

                    playerDownLeft = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)
                    playerUpLeft = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)
                    playerUpRight = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)

                    playerDownRight = pygame.transform.scale(pygame.image.load(playerSprite[1]), (129, 148))
                    lastImg = playerSprite[1]
                    screen.blit(playerDownRight, playerCoordinates)
                    droneThreePressed = True

                # Key P -> Up right
                if event.key == pygame.K_p:
                    player = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)

                    playerDownLeft = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)
                    playerDownRight = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)
                    playerUpLeft = pygame.transform.scale(pygame.image.load(data.CLOAK), playerSize)

                    playerUpRight = pygame.transform.scale(pygame.image.load(playerSprite[3]), (129, 148))
                    lastImg = playerSprite[3]
                    screen.blit(playerUpRight, playerCoordinates)
                    droneFourPressed = True



        
        # Results if task appeared somewhere and players picked it 
        if isRisky == False:
            if taskPositionOne == True and droneOnePressed == True:
                score+=10
            if taskPositionTwo == True and droneTwoPressed == True:
                score+=10
            if taskPositionThree == True and droneThreePressed == True:
                score+=10
            if taskPositionFour == True and droneFourPressed == True:
                score+=10
        else:
            if diffucultyLevel == "Difficulty(Easy/Average/Hard): Easy":
                boomOrMoney = randint(1, 16) # Probability of a bad work at the easy-mode is 1/16 or 6,25%
                if boomOrMoney == 1:
                    if taskPositionOne == True and droneOnePressed == True:
                        score-=50
                        lifes-=1
                    if taskPositionTwo == True and droneTwoPressed == True:
                        score-=50
                        lifes-=1
                    if taskPositionThree == True and droneThreePressed == True:
                        score-=50
                        lifes-=1
                    if taskPositionFour == True and droneFourPressed == True:
                        score-=50
                        lifes-=1
                else:
                    if taskPositionOne == True and droneOnePressed == True:
                        score+=60
                    if taskPositionTwo == True and droneTwoPressed == True:
                        score+=60
                    if taskPositionThree == True and droneThreePressed == True:
                        score+=60
                    if taskPositionFour == True and droneFourPressed == True:
                        score+=60
            if diffucultyLevel == "Difficulty(Easy/Average/Hard): Average":
                boomOrMoney = randint(1, 12) # Probability of a bad work at the average-mode is 1/12 or 8,3%
                if boomOrMoney == 1:
                    if taskPositionOne == True and droneOnePressed == True:
                        score-=50
                        lifes-=1
                    if taskPositionTwo == True and droneTwoPressed == True:
                        score-=50
                        lifes-=1
                    if taskPositionThree == True and droneThreePressed == True:
                        score-=50
                        lifes-=1
                    if taskPositionFour == True and droneFourPressed == True:
                        score-=50
                        lifes-=1
                else:
                    if taskPositionOne == True and droneOnePressed == True:
                        score+=50
                    if taskPositionTwo == True and droneTwoPressed == True:
                        score+=50
                    if taskPositionThree == True and droneThreePressed == True:
                        score+=50
                    if taskPositionFour == True and droneFourPressed == True:
                        score+=50
            if diffucultyLevel == "Difficulty(Easy/Average/Hard): Hard":
                boomOrMoney = randint(1, 8) # Probability of a bad work at the easy-mode is 1/8 or 12,5%
                if boomOrMoney == 1:
                    if taskPositionOne == True and droneOnePressed == True:
                        score-=50
                        lifes-=1
                    if taskPositionTwo == True and droneTwoPressed == True:
                        score-=50
                        lifes-=1
                    if taskPositionThree == True and droneThreePressed == True:
                        score-=50
                        lifes-=1
                    if taskPositionFour == True and droneFourPressed == True:
                        score-=50
                        lifes-=1
                else:
                    if taskPositionOne == True and droneOnePressed == True:
                        score+=50
                    if taskPositionTwo == True and droneTwoPressed == True:
                        score+=50
                    if taskPositionThree == True and droneThreePressed == True:
                        score+=50
                    if taskPositionFour == True and droneFourPressed == True:
                        score+=50
        
        # Display stats - score, lifes and best score
        showScore(x=10, y=10, points=score)
        showLifes(x=10, y=40, numOfRemaing=lifes)
        showBestScore(x=10, y=56)
        # Display if have a debt
        if isInDebt == True and score < 200:
            haveDebt(x=10, y=72)
        if isInDebt == True and score >= 200:
            score -= 200
            haveDebt(x=10, y=72)
            isInDebt = False
        if isInDebt == False:
            noDebt(x=10, y=72)

        #timer3M(x=10, y=70)



        # If player beat the previous record - make this a new record
        if score > int(BS_score):
            remove("Game/Code/score.txt")
            newBestScore = score
            newBestScoreFile = open("Game/Code/score.txt", "x")
            now = datetime.datetime.now()
            today = datetime.date.today()
            current_data  = today.strftime("%d.%m.%Y")
            current_time = now.strftime("%H:%M:%S")
            new_content = [f"Best score\n", f"Best score: {newBestScore}\n", f"Time: {current_data}-{current_time}"]
            newBestScoreFile.writelines(new_content)


    
    pygame.display.update()
