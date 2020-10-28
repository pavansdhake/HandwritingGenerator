from PIL import Image
import Digit.Digit as DigitBuilder


def get_handwritten_matrix(matrix):
    img = Image.new('RGB', (2100, 1000), 'white')
    cursorX = 0
    cursorY = 0

    offsetX = 200
    offsetY = 100

    for i in range(0, len(matrix)):
        row = matrix[i]
        for num in row:
            temp = DigitBuilder.get_number(int(num))
            img.paste(temp, (cursorX, cursorY))
            cursorX += offsetX
        cursorX = 0
        cursorY += offsetY

    return img