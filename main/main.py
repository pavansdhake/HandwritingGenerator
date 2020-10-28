from PIL import Image
import Digit.Digit as DigitBuilder
import Digit.constants as Constants


img = Image.new('RGBA', (2100, 1000), 'white')

# Left and Right braces
left = Image.open(Constants.left_braces)
right = Image.open(Constants.right_braces)

lw, lh = left.size
rw, rh = right.size

L = lw + 10
R = 2100 - rw - 10

cursorX = L
cursorY = 0

offsetX = 200
offsetY = 100

print('Handwriting generator: \n\n')
print('Enter the input matrix : \n\n')

while True:
    row = input()
    if row == '':
        break

    data = row.split(" ")
    for num in data:
        temp = DigitBuilder.get_number(int(num))
        img.paste(temp, (cursorX, cursorY))
        w, h = temp.size
        cursorX += offsetX
    cursorX = L
    cursorY += offsetY

img.paste(left, (0, 20))
img.paste(right, (2100 - rw, 20))

img.show()
