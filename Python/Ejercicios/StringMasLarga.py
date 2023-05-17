def string_more_larger(*strings):
    n = 0
    for string in strings:
        if len(strings[n - 1]) < len(strings[n]):
            more_larger = strings[n]
            n += 1
        else:
            more_larger = strings[n-1]
            n += 1

    return more_larger


def main():
    print(string_more_larger("ana", "beto", "camila"))

if __name__ == "__main__":

    main()