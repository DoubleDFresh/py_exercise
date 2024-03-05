"""This function returns 'black' or 'white' based upon the inputted column and row

columns / rows begin at 1 and end at 8
white = 1,1 1,3 2,0 2,4 3,1 (always even sum)
black = 1,2 2,1 2,3 (always odd)

"""
# the argument is passed to the function and assigned as the value to the parameter

def getChessSquareColor(column, row):
    if (column < 1 or column > 8) or (row < 1 or row > 8):
        return ''
    if (column + row) % 2 == 0:
        return 'white'
    else:
        return 'black'
    
assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'  #error - book image is from 0 - 7, but code is 1 - 8
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''