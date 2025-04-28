def recursife_nth_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        return recursife_nth_fibo(n-1) + recursife_nth_fibo(n-2)
# print(recursife_nth_fibo(5))
def main():
    n = input("Zadej idx v fibomacchci posloupnosti: ")
    n = int(n)
    vejsledek = recursife_nth_fibo(n)
    return print(vejsledek)


if __name__ == "__main__":
    main()
