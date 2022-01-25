theLayout = {'1': ' ', '2': ' ', '3': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '7': ' ', '8': ' ', '9': ' '}

tic_keys = []

for key in theLayout:
    tic_keys.append(key)


def printlayout(layout):
    print(layout['7'] + '|' + layout['8'] + '|' + layout['9'])
    print('-+-+-')
    print(layout['4'] + '|' + layout['5'] + '|' + layout['6'])
    print('-+-+-')
    print(layout['1'] + '|' + layout['2'] + '|' + layout['3'])


def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printlayout(theLayout)
        print("Your turn, " + turn + ".Which place to move to?")

        move = input()

        if theLayout[move] == ' ':
            theLayout[move] = turn
            count += 1
        else:
            print("Sorry place already occupied. \n Which place to move to?")
            continue

        if count >= 5:
            if theLayout['7'] == theLayout['8'] == theLayout['9'] != ' ':
                printlayout(theLayout)
                print("\nGame Over.\n")
                print(" **** " + turn + " Won. ****")
                break
            elif theLayout['4'] == theLayout['5'] == theLayout['6'] != ' ':
                printlayout(theLayout)
                print("\nGame Over.\n")
                print(" **** " + turn + " Won. ****")
                break
            elif theLayout['1'] == theLayout['2'] == theLayout['3'] != ' ':  # across the bottom
                printlayout(theLayout)
                print("\nGame Over.\n")
                print(" **** " + turn + " Won. ****")
                break
            elif theLayout['1'] == theLayout['4'] == theLayout['7'] != ' ':  # down the left side
                printlayout(theLayout)
                print("\nGame Over.\n")
                print(" **** " + turn + " Won. ****")
                break
            elif theLayout['2'] == theLayout['5'] == theLayout['8'] != ' ':  # down the middle
                printlayout(theLayout)
                print("\nGame Over.\n")
                print(" **** " + turn + " Won. ****")
                break
            elif theLayout['3'] == theLayout['6'] == theLayout['9'] != ' ':  # down the right side
                printlayout(theLayout)
                print("\nGame Over.\n")
                print(" **** " + turn + " Won. ****")
                break
            elif theLayout['7'] == theLayout['5'] == theLayout['3'] != ' ':  # diagonal
                printlayout(theLayout)
                print("\nGame Over.\n")
                print(" **** " + turn + " Won. ****")
                break
            elif theLayout['1'] == theLayout['5'] == theLayout['9'] != ' ':  # diagonal
                printlayout(theLayout)
                print("\nGame Over.\n")
                print(" **** " + turn + " Won. ****")
                break

        # If neither X nor O wins and the layout is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("Game Tied!!")

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in tic_keys:
            theLayout[key] = " "

        game()


if __name__ == "__main__":
    game()
