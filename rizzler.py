def introduceGame():
    gameIntro = "This is a Rizz calcuator. Type ..."
    print( gameIntro )

# This functions takes in the 2 dimensional list of
#  words and ratings and returns just the words in that list. AKA Derizz
def derizz( rizzlerRatings ):
    rizzlerWords = []
    for currentPairIndex in range( len( rizzlerRatings ) ): # Go through rizzlerRatings, row by row
        rizzlerWords.append( rizzlerRatings[currentPairIndex][ 0 ] ) # Append the first word in rizzlerRatings

    return rizzlerWords


def main():
    restartthequestion = True
    while restartthequestion:
        userRizzScore = 0
        rizzlerRatings = [
            [ "Sui", 4 ],
            [ "Stop", 2 ],
            [ "Gyatt", 4 ],
        ]

        introduceGame()
        userRizzler = input( "Type in your rizzler line: " )
        userRizzlerWordsAsList = userRizzler.split()

        onlyRizzWords =  derizz(rizzlerRatings)
        for currentWord in userRizzlerWordsAsList:
            if currentWord in onlyRizzWords:
                indexofCurrentWord = onlyRizzWords.index( currentWord )
                userRizzScore += rizzlerRatings[ indexofCurrentWord ][1]
        
        print( userRizzScore )
        restart = input( " restart Yes or No : " )
        print(restart)
        if(restart.lower() == "yes"):
            continue
        else: restartthequestion = False
            






main()
