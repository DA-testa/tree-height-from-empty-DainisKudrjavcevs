import sys
import threading
import numpy as np

def compute_height(n, parents):
    heights = np.zeros(int(n))
    max_height = 0
    for i in range(int(n)):
        if heights[i] > 0:
            continue
        height = 0
        j = i
        while j != -1:
            if heights[j] > 0:
                height += heights[j]
                break
            else:
                height += 1
                j = int(parents[j])
        heights[i] = height
        if height > max_height:
            max_height = height
    return max_height

def get_input():
    while True:
        input_method = input().strip()
        if input_method in ["I", "F"]:
            break
        else:
            print("Invalid input method")
    
    if input_method == "F":
        filename = input().strip()
        if filename.endswith(".txt"):
            n, parents = main(filename)
            if n and parents:
                height = compute_height(n, parents)
                print(int(height))
    else:
        n = input().strip()
        if n:
            parents = input().strip().split(" ")
            if parents:
                height = compute_height(n, parents)
                print(int(height))

def main(filename):
    try:
        with open(f"./test/{filename}") as f:
            contents = f.readlines()
    except:
        print("Invalid filename")
        return None, None

    n = contents[0].strip()
    if n:
        parents = contents[1].strip().split(" ")
        if parents:
            return n, parents
    return None, None

sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)
threading.Thread(target=get_input).start()
