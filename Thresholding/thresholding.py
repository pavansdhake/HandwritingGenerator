import Handwritting.Handwriting as Handwriting


def thresholding(A, B, C, D, question_number):
    Boundary = []
    Set = []
    while True:
        command = input()
        if command == "end":
            break
        else:
            data = command.split(" ")
            x1 = int(data[1])
            y1 = int(data[2])
            x2 = int(data[3])
            y2 = int(data[4])

            m = (y2 - y1)/(x2 - x1)
            c = int(y1 - m*x1)
            set = [m, c]
            Boundary.append(x2)
            Set.append(set)

    Ares = solve_threshold(A, Boundary, Set)
    Bres = solve_threshold(B, Boundary, Set)
    Cres = solve_threshold(C, Boundary, Set)
    Dres = solve_threshold(D, Boundary, Set)

    a = Handwriting.get_handwritten_matrix(Ares)
    a.save('../Solutions/' + str(question_number) + 'a.jpg')
    b = Handwriting.get_handwritten_matrix(Bres)
    b.save('../Solutions/' + str(question_number) + 'b.jpg')
    c = Handwriting.get_handwritten_matrix(Cres)
    c.save('../Solutions/' + str(question_number) + 'c.jpg')
    d = Handwriting.get_handwritten_matrix(Dres)
    d.save('../Solutions/' + str(question_number) + 'd.jpg')
    return


def solve_threshold(matrix, boundary, Cset):
    new_matrix = []
    for j in range(0, 10):
        row = matrix[j]
        new_row = []
        for i in range(0, 10):
            data = row[i]
            for p in range(0, len(boundary)):
                if data <= boundary[p]:
                    pixel = Cset[p][0] * data + Cset[p][1]
                    new_row.append(pixel)
                    break
        new_matrix.append(new_row)
    return new_matrix