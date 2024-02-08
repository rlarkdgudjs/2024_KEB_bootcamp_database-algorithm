import mymath
import time

if __name__ == "__main__":
    n = int(input("INPUT n : "))
    r = int(input("INPUT r : "))
    start = time.time()
    print(f"{n}C{r} = {mymath.nCr(n,r)}")
    end = time.time()
    print(end-start)