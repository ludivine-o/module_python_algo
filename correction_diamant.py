def first_last_line(letter, choice):
    A = ((choice - 97) * '.' + str(chr(letter)) + (choice - 97) * '.' + "\n")
    return line

def center_diamond(letter, choice):
    side_dot = choice - letter -1
    middle_dot = 1
    line = first_last_line(letter, choice)
    letter += 1
    while letter != choice:
        new_line = (side_dot * "." + str(chr(letter)) + middle_dot * "." + str(chr(letter)) + side_dot * "." + "\n")
        side_dot -= 1
        middle_dot += 2
        letter += 1
        line += new_line
    while letter != ord("a"):
        new_line = (side_dot * "." + str(chr(letter)) + middle_dot * "." + str(chr(letter)) + side_dot * "." + "\n")
        side_dot += 1
        middle_dot -= 2
        letter -= 1
        line += new_line
    line += first_last_line(letter, choice)
    return line


choice = ord(input("choisir une lettre : ").lower())
letter = ord('a')




print(center_diamond(letter, choice))








