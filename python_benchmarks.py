import timeit
import sys
from python_implementations import fixed_array_stack, dynamic_array_heap

def run_benchmarks():
    with open('test_input.txt') as f:
        test_data = [int(line.strip()) for line in f if line.strip().isdigit()]
    
    print("Fixed Stack Array:")
    print(timeit.timeit(
        lambda: fixed_array_stack.main(),
        number=100
    ))
    
    print("Dynamic Heap Array:")
    print(timeit.timeit(
        lambda: dynamic_array_heap.main(),
        number=100
    ))

if __name__ == "__main__":
    run_benchmarks()