xo = "_________"
new_xo = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
print("---------")
print("| " + xo[0] + " " + xo[1] + " " + xo[2] + " |")
print("| " + xo[3] + " " + xo[4] + " " + xo[5] + " |")
print("| " + xo[6] + " " + xo[7] + " " + xo[8] + " |")
print("---------")

while True:
    player = "X"

    counter = -1
    for i in xo:
        counter += 1
        new_xo[counter] = str(i)

    coordinates = []

    sprawdzenie = True
    while sprawdzenie:
        coordinates = input("Enter the coordinates:").split()
        try:                        #zakomentować
            int(coordinates[0])
            sprawdzenie = False
        except ValueError:
            print("You should enter numbers!")
            sprawdzenie = True

    number_xo = 0
    all_coordinates = [['1', '1'], ['1', '2'], ['1', '3'], ['2', '1'], ['2', '2'], ['2', '3'], ['3', '1'], ['3', '2'], ['3', '3']]
    c2 = -1    # pozycja podanych koordynatow

    while (int(coordinates[0]) > 3) or (int(coordinates[1]) > 3):  # if more 3
        print("Coordinates should be from 1 to 3!")
        coordinates = input("Enter the coordinates:").split()

    for i in all_coordinates:  # numer sprawdzanej
        c2 += 1
        if coordinates[0] == i[0] and coordinates[1] == i[1]:
            break
    while xo[c2] == "X" or xo[c2] == "O":
        print("This cell is occupied! Choose another one!")
        coordinates = input("Enter the coordinates:").split()
        c2 = -1
        for i in all_coordinates:  # numer sprawdzanej
            c2 += 1
            if coordinates[0] == i[0] and coordinates[1] == i[1]:
                break
        continue
    c4 = 0
    for i in all_coordinates:     # dodawanie x
        c4 += 1
        if coordinates[0] == i[0] and coordinates[1] == i[1] and c4 % 2 != 0 and c4 < 9:
            new_xo[c2] = "X"
        else:
            new_xo[c2] = "O"
    xo = "".join(new_xo)

    print("---------")
    print("| " + xo[0] + " " + xo[1] + " " + xo[2] + " |")
    print("| " + xo[3] + " " + xo[4] + " " + xo[5] + " |")
    print("| " + xo[6] + " " + xo[7] + " " + xo[8] + " |")
    print("---------")

    win = [[xo[0], xo[1], xo[2]],
           [xo[3], xo[4], xo[5]],
           [xo[6], xo[7], xo[8]],
           [xo[0], xo[4], xo[8]],
           [xo[2], xo[4], xo[6]],
           [xo[0], xo[3], xo[6]],
           [xo[2], xo[5], xo[8]],
           [xo[1], xo[4], xo[7]]]
    result = 1
    counterX = 0
    counterO = 0
    for i in win:
        if i == ['X', 'X', 'X']:
            counterX += 1
        if i == ['O', 'O', 'O']:
            counterO += 1
    x = 0
    o = 0
    space = 0
    for k in str(xo):
        if k == 'X':
            x += 1
        if k == 'O':
            o += 1
        if k == '_':
            space += 1
    if counterO == 1 and counterX == 0:
        print("O wins")
        break
    if counterO == 0 and counterX == 1:
        print("X wins")
        break
    if counterO == counterX and counterO == 0 and space == 0:
        print("Draw")
        break
    if counterO == 0 and counterX == 0:
        if space > 0:
            if not (x - o > 2 or o - x > 2):
                print("Game not finished")

    if counterO > 0 and counterX > 0:
        print("Impossible")
    if x - o > 1 or o - x > 1:
        print("Impossible")
