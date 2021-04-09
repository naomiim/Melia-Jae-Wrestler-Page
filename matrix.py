"""
__filename__ = "matrix.py"
__course__ = "SDEV 300 6382"
__author__ = "Naomi Martinez"
__copyright__ = "None"
__credits__ = "Naomi Martinez"
__license__ = "Pyzo GPL"
__version__ = "1.0.0"
__maintainer__ = "Naomi Martinez"
__email__ = "nmartinezwilson@student.umgc.edu"
__status__ = "Project 4"
"""
import numpy as np

def checkEntry(inputValue):
    """
    matrix main()
    """

    try:
        float(inputValue)
    except ValueError:
        return False
    return True

# matrix input function
def getMatrix():
    mat = np.zeros((3, 3))
    for row in range(3):
        for column in range(3):
            check = False
            while not check:
                num = input('Enter element at position ({:d},{:d}): '.format(row + 1, column + 1))
                check = checkEntry(num)
                if not check:
                    print('Please enter a numeric value!')
            mat[row, column] = float(num)
        print()
    return mat

# welcome message
print ('****** Welcome to the Matrix Game *****')

print ('\n Do you want to play the Matrix Game?')

# yes or no input

answer = input("Enter yes or no: ")

# if yes input
if answer == "yes":

    print('Enter first matrix: ')
    mat1 = getMatrix()

    print('Enter second matrix: ')
    mat2 = getMatrix()

    # matrix options
    print('Enter option:\n1.Addition\n2.Subtraction\n3.Matrix multiplication\n4.Element by element multiplication\n5.Exit')
    choice = int(input())

    while choice != 5:
        if choice == 1:
            print ('\n You chose addition')
            # addition input function
            res = mat1 + mat2
        elif choice == 2:
            print ('\n You chose subtraction')
            # subtraction input function
            res = mat1 - mat2
        elif choice == 3:
            print ('\n You chose Matrix Multiplication')
            # matrix multiplication input function
            res = np.matmul(mat1, mat2)
        elif choice == 4:
            print ('\n You chose Element by element multiplication')
            # element multiplication input function
            res = np.multiply(mat1, mat2)
        print('\n Result:')
        print(res)
        print('\n Transpose of result:')
        print(res.T)
        print('\n Mean of rows:')
        print(np.mean(res, 1))
        print('\n Mean of columns:')
        print(np.mean(res, 0))

# if answered no
elif answer == "no":
    print ('*****Thanks for Playing!*****')
