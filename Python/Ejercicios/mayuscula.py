def mayus(string):
    return_upper = ""
    for letter in string:
        if "a" in letter:
            return_upper = return_upper + "A"
        elif "b" in letter:
            return_upper = return_upper + "B"
        elif "c" in letter:
            return_upper = return_upper + "C"
        elif "d" in letter:
            return_upper = return_upper + "D"
        elif "e" in letter:
            return_upper = return_upper + "E"
        elif "f" in letter:
            return_upper = return_upper + "F"
        elif "g" in letter:
            return_upper = return_upper + "G"
        elif "h" in letter:
            return_upper = return_upper + "H"
        elif "i" in letter:
            return_upper = return_upper + "I"
        elif "j" in letter:
            return_upper = return_upper + "J"
        elif "k" in letter:
            return_upper = return_upper + "K"
        elif "l" in letter:
            return_upper = return_upper + "L"
        elif "m" in letter:
            return_upper = return_upper + "M"
        elif "n" in letter:
            return_upper = return_upper + "N"
        elif "ñ" in letter:
            return_upper = return_upper + "Ñ"
        elif "o" in letter:
            return_upper = return_upper + "O"
        elif "p" in letter:
            return_upper = return_upper + "P"
        elif "q" in letter:
            return_upper = return_upper + "Q"
        elif "r" in letter:
            return_upper = return_upper + "R"
        elif "s" in letter:
            return_upper = return_upper + "S"
        elif "t" in letter:
            return_upper = return_upper + "T"
        elif "u" in letter:
            return_upper = return_upper + "U"
        elif "v" in letter:
            return_upper = return_upper + "V"
        elif "w" in letter:
            return_upper = return_upper + "W"
        elif "x" in letter:
            return_upper = return_upper + "X"
        elif "y" in letter:
            return_upper = return_upper + "Y"
        elif "z" in letter:
            return_upper = return_upper + "Z"
        elif " " in letter:
            return_upper = return_upper + " "
    return return_upper


def main():
    print(mayus(input("Cadena a capitalizar: ")))


if __name__ == "__main__":
    main()