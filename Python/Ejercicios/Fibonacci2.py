def fibonacci_recu(n):
    if n <= 1:
        return 1
    return fibonacci_recu(n-1) + fibonacci_recu(n-2)

def main():
   for a in range(10):
        print(fibonacci_recu(a))

if __name__ == "__main__":
    main()