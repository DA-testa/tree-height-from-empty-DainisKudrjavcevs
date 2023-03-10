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


def keyboard():
    n = input().strip()

    if n:
        parents = input().strip().split(" ")
        if parents:
            return n, parents

    return None, None


def file(filename):
    try:
        with open(f"./test/{filename}") as f:
            contents = f.readlines()
    except FileNotFoundError:
        print("File not found")
        return None, None
    except:
        print("Error reading file")
        return None, None
    
    n = contents[0].strip()
    if not n:
        print("Invalid input: n not provided")
        return None, None
    
    parents = contents[1].strip().split(" ")
    if not parents:
        print("Invalid input: parents not provided")
        return None, None
    
    return n, parents


def main():
    input_method = input().strip()

    if input_method == "I":
        n, parents = keyboard()
        if n and parents:
            height = compute_height(n, parents)
            print(int(height))

    elif input_method == "F":
        filename = input().strip()
        if str(filename[-1]) != "a":
            n, parents = file(filename)
            if n and parents:
                height = compute_height(n, parents)
                print(int(height))



sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)
threading.Thread(target=main).start() 
