import mymath


if __name__ == "__main__":
    n = int(input("INPUT n : "))
    r = int(input("INPUT r : "))
    print(f"{n}C{r} = {mymath.nCr(n,r)}")