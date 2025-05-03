#!/bin/bash

echo "Running C++ benchmarks..."
g++ -O3 cpp_implementations/FixedArrayStack.cpp -o fixed_stack
g++ -O3 cpp_implementations/DynamicArrayHeap.cpp -o dynamic_heap

echo "Fixed Stack Array:"
time ./fixed_stack < test_input.txt > /dev/null

echo "Dynamic Heap Array:"
time ./dynamic_heap < test_input.txt > /dev/null

rm fixed_stack dynamic_heap