import sys
import threading
import numpy

def compute_height(n, parents):
    koks = [[] for i in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else :
            koks[parents[i]].append(i)
    return height(root, koks)

def height(x, koks):
    if not koks[x]:
        return 1
    else:
        return max(height(berns, koks) for berns in koks[x]) + 1


def main():
    method = input().lower()
    if method == 'i':
        n = int(input())
        parents = list(map(int, input().split()))
    elif method == 'f':
        valid_filename = False
        while not valid_filename:
            try:
                filename = input()
                if 'a' in filename:
                    raise ValueError("Invalid filename")
                with open(f"./test/{filename}") as f:
                    n = int(f.readline())
                    parents = list(map(int, f.readline().split()))
                    valid_filename = True
            except (FileNotFoundError, ValueError):
                print("Invalid file name or format. Try again.")
    else:
        print("Invalid input method")
        return
    
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
