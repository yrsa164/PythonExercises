def printStars(Xstars, Ksign):
    starAndCharList = []
    starsToChange = getAsciiCharacters(33, 126)
    charCounter = 0
    for x in range(Xstars):
        starAndCharList.append('*')
        if charCounter == 94:
            charCounter = 0
        if (x +1) % Ksign == 0:
            starAndCharList[x] = starsToChange[charCounter]
            charCounter += 1

    print(starAndCharList)


def getAsciiCharacters(charStart, charStop):
    avalibleCharacterList = []
    charCounter = charStop - charStart
    for x in range(charCounter+1):
        avalibleCharacterList.append(chr(charStart + x))
    return avalibleCharacterList


printStars(600, 3)
