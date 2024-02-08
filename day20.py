
import random


if __name__ == "__main__":
    count = 0
    answer = random.randint(1, 100)
    while(True):
        input_num = int(input())
        if answer != input_num:
            count += 1
            if input_num < answer:
                print(f'up, current count : {count}')
            else:
                print(f'down, current count : {count}')
        else:
            count += 1
            break
    print(f"answer : {answer}, count : {count}번")
