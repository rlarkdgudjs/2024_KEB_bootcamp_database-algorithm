def factorial(num) -> int :
    pass

def nCr(n,r) -> int :
    """
    조합 함수
    :param n:
    :param r:
    :return:
    """
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return numerator / denominator

if __name__ == "__main__":
    n = int(input("INPUT n : "))
    r = int(input("INPUT r : "))
    print(f"{n}C{r} = {nCr(n,r)}")