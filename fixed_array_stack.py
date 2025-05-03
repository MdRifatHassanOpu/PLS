MAX_SIZE = 100  # Conceptual fixed size

def main():
    arr = [None] * MAX_SIZE
    current_size = 0
    
    print(f"Enter elements (max {MAX_SIZE}), enter -1 to stop:")
    while current_size < MAX_SIZE:
        try:
            val = int(input())
            if val == -1:
                break
            arr[current_size] = val
            current_size += 1
        except ValueError:
            break

    print("Fixed Stack Array Contents:")
    for i in range(current_size):
        print(f"arr[{i}] = {arr[i]}")

if __name__ == "__main__":
    main()