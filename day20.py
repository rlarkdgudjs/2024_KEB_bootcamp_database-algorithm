def factorial(num) -> int :
    result = 1
    for i in range(1,num+1):
        result = result * i
    return result

def nCr(n,r) -> int :
    """
    조합 함수
    :param n:
    :param r:
    :return:
    """
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerator / denominator)

if __name__ == "__main__":
    n = int(input("INPUT n : "))
    r = int(input("INPUT r : "))
    print(f"{n}C{r} = {nCr(n,r)}")