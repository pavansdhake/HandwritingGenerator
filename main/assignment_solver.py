import Thresholding.thresholding as Thresholding

print("Assignment Solver\n")
print("============================================\n\n")

print("Enter matrix A : \n")
size = 10

A = []

i = 0
while i < 10:
    row = input()
    data = row.split(" ")
    r = []
    for pixel in data:
        r.append(int(pixel))
    A.append(r)
    i += 1

print("Enter matrix B : \n")
B = []

i = 0
while i < 10:
    row = input()
    data = row.split(" ")
    r = []
    for pixel in data:
        r.append(int(pixel))
    B.append(r)
    i += 1

print("Enter matrix C : \n")
C = []

i = 0
while i < 10:
    row = input()
    data = row.split(" ")
    r = []
    for pixel in data:
        r.append(int(pixel))
    C.append(r)
    i += 1

print("Enter matrix D : \n")
D = []

i = 0
while i < 10:
    row = input()
    data = row.split(" ")
    r = []
    for pixel in data:
        r.append(int(pixel))
    D.append(r)
    i += 1

while True:
    print("Enter the command : \n\n")
    command = input()

    if command == "start":
        question_number = input("Enter the Question Number : \n")
        print("\n Enter the curve data : \n")
        Thresholding.thresholding(A, B, C, D, question_number)

    elif command == "exit":
        break
