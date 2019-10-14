NUM_LINES = 25
NUM_COLS = 40
HOR_SIDE = 5

START_X_OFFSET = 0
SYMBOL = '*'

def printSots():
    xOffset = START_X_OFFSET;
    for y in range(NUM_LINES):
        line = ''
        for x in range(NUM_COLS):
            if (y % 2 == 0):
                if (isMarkOdd(xOffset, x)):
                    line += SYMBOL
                else :
                    line += ' '
            else:
                if (isMarkNotOdd(xOffset, x)):
                    line += SYMBOL
                else :
                    line += ' '
        if (y % 2 == 0):
            xOffset += HOR_SIDE+1;

        print(line)

def isMarkOdd(startOffset, iPos):
    fullline = HOR_SIDE * 2 + 2
    tail = (iPos - startOffset) % fullline
    return tail < HOR_SIDE

def isMarkNotOdd(startOffset, iPos):
    fullline = HOR_SIDE * 2 + 2
    tail = (iPos - startOffset + 1) % (fullline / 2)
    return tail==0 

printSots()
