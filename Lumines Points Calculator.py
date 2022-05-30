score = 0
level = 0

skinTargetSquares = [22, 16, 16, 16, 28, 16, 16, 14,
                     26, 18, 18, 18, 18, 24, 26, 28,
                     28, 30, 32, 32, 32, 32, 32, 32]
skinNames = ["Shinin'", "URBANIZATION", "ROUND ABOUT", "SLIPPING",
             "Shake ya body", "SQUAREDANCE", "TALK 2 YOU", "JUST...",
             "I hear the music in my soul", "DARKSIDE BESIDE THE RIVER",
             "ABACK", "WORKING IN THE HOLE", "SISTER WALK", "Da-Di-Do",
             "STRANGERS", "Holiday in summer", "TAKE A DOG OUT A WALK",
             "Big Elapso", "My Generation", "MEGURO", "SPIRITS",
             "Get up and Go", "FLY INTO THE SKY", "Lights"]
skinLevelsToNewSkin = [4, 4, 4, 4, 4, 4, 4, 4,
                       4, 4, 4, 4, 4, 4, 4, 4,
                       5, 5, 5, 5, 5, 5, 5, 5]

comboStage = 0
comboStageMax = 3
comboMultiplier = [1, 4, 8, 16]

POINTS_PER_SQUARE = 40

def calculate_points_for_skin(skinIndex, squaresErasedOnSweep, printSkinInfo):
    global comboStage
    
    pointsEarned = 0
    squaresErased = 0 #For quota, not total squares erased
    targetSquaresErased = skinTargetSquares[skinIndex]
    levelsToNewSkin = skinLevelsToNewSkin[skinIndex]

    if (printSkinInfo):
        print("Current skin: " + skinNames[skinIndex])
        print("Squares to levelup: ", skinTargetSquares[skinIndex])
        print("Levelups needed: ", skinLevelsToNewSkin[skinIndex])
        print('')
    
    while (levelsToNewSkin > 0):
        squaresErased += squaresErasedOnSweep
        basePoints = (squaresErasedOnSweep * POINTS_PER_SQUARE)
        if (squaresErased >= 4):
            #Combo maintained, increment multiplier
            comboStage = min(comboStage + 1, comboStageMax)
        else:
            #Dropped combo
            if (comboStage > 0): 
                comboStage = 0
        pointsEarned += basePoints * comboMultiplier[comboStage]
        if (squaresErased > targetSquaresErased):
            levelsToNewSkin -= 1
            squaresErased = 0
    return (pointsEarned)

#Assumes that comboStage will remain the same throughout entire run
def calculate_points_for_run(squaresErasedPerSweep, printSkinScores, printSkinInfo):
    score = 0
    for skinIndex in range(len(skinTargetSquares)):
        
        pointsScored = calculate_points_for_skin(skinIndex,
                                                 squaresErasedPerSweep,
                                                 printSkinInfo)

        if (printSkinScores):
            print("Score for \"" + skinNames[skinIndex] + "\" while making",
              squaresErasedPerSweep, "squares per sweep:", pointsScored)
        score += pointsScored
    return (score)

#print("Final score: ", calculate_points_for_run(4, False, False))
