import sys

def main():
    arr = []
    print("Enter elements (enter -1 to stop):")
    
    while True:
        try:
            val = int(input())
            if val == -1:
                break
            arr.append(val)
        except ValueError:
            break

    print("Dynamic Heap Array Contents:")
    for i, val in enumerate(arr):
        print(f"arr[{i}] = {val}")
    
    print(f"Memory usage: {sys.getsizeof(arr)} bytes")

if __name__ == "__main__":
    main()