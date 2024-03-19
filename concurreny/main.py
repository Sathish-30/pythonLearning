from concurrent.futures import ProcessPoolExecutor,wait
import os , time
from time import sleep
from random import random

def task(n) -> list:
    arr = []
    for i in range(n):
        arr.append(i)
    return arr if len(arr) > 0 else [3 , 4 ,5]

def main() -> None:
    executor = ProcessPoolExecutor(max_workers = 4)
    arr = [0 , 3]
    futures = [executor.submit(task , 
                n = chunks) for chunks in arr]

    wait(futures)
    for res in futures:
        print(res.result())


if __name__ == "__main__":
    main()