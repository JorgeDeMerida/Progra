def sum_list(*integers):
    n = 0
    sum_integer = 0
    for integer in integers:
        sum_integer = sum_integer + int(integers[n])
        n += 1

    return sum_integer

def main():
    print(sum_list("1", "8", "11"))

if __name__ == "__main__":
    main()