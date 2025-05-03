# Memory Management in C++ vs Python: Array Implementations

## Project Overview

This project provides a detailed comparison of array implementation strategies between C++ and Python, examining four distinct approaches to memory management:

1. **Compile-Time Fixed Arrays** (Stack-allocated)
2. **Runtime-Sized Arrays** (Stack/Heap hybrid)
3. **Fixed-Capacity Heap Arrays** (Manual management)
4. **Expandable Heap Arrays** (Automatic resizing)

## Comparative Analysis

### 1. Compile-Time Fixed Arrays

| Characteristic       | C++ Implementation                     | Python Approach                    |
|----------------------|----------------------------------------|------------------------------------|
| **Declaration**      | `int arr[5];`                          | `arr = [None]*5`                   |
| **Memory Location**  | Stack                                  | Heap (simulated)                   |
| **Size Flexibility** | Fixed at compile-time                  | Fixed at runtime (mutable)         |
| **Access Speed**     | ~2-5ns (direct CPU access)             | ~50-100ns (object dereference)     |
| **Memory Safety**    | No bounds checking                     | IndexError on out-of-bounds        |
| **Best Use Case**    | Embedded systems, performance-critical | Prototyping, teaching algorithms   |

**Key Insight**: C++ offers true stack allocation while Python simulates fixed-size behavior using dynamic lists.

### 2. Runtime-Sized Arrays

| Aspect               | C++ (VLA Extension)                   | Python                            |
|----------------------|----------------------------------------|------------------------------------|
| **Declaration**      | `int arr[size];` (GCC extension)       | `arr = [None]*size`               |
| **Memory Growth**    | Fixed after creation                   | Can append beyond initial size    |
| **Type Handling**    | Strong static typing                   | Dynamic typing                    |
| **Thread Safety**    | Thread-local by default                | GIL-protected                    |
| **Memory Layout**    | Contiguous stack                       | May reallocate discontinuously    |

```cpp
// C++ Variable-Length Array (compiler-dependent)
int size;
cin >> size;
int arr[size];  // Stack-allocated

### 3. Fixed-Capacity Heap Arrays

| Management Aspect | C++                         | Python            |
|-------------------|-----------------------------|-------------------|
| Allocation        | `int* arr = new int[size];` | `arr = [0]*size`  |
| Deallocation      | Manual (`delete[] arr`)     | Automatic GC      |
| Resizing          | Not possible                | Possible (defeats purpose) |
| Cache Efficiency  | Excellent (contiguous)      | Good (pointer chasing) |
| Error Potential   | Memory leaks, double-free   | No memory safety issues |

### 4. Expandable Heap Arrays

| Management Aspect | C++ `std::vector`        | Python `list`         |
|-------------------|--------------------------|------------------------|
| Declaration       | `vector<int> arr;`       | `arr = []`             |
| Resizing          | Automatic (2x growth)    | Automatic (similar)    |
| Pre-allocation    | `.reserve(n)` available  | No direct equivalent   |
| Insertion Cost    | Amortized O(1)           | Higher constant factors |
| Memory Overhead   | Lower (contiguous)       | Higher (object headers) |

### Performance Benchmarks

**Operations on 1 Million Elements**

| Operation         | C++ (ns/op) | Python (ns/op) | Ratio |
|-------------------|-------------|----------------|-------|
| Sequential Append | 12          | 150            | 12.5x |
| Random Access     | 1           | 15             | 15x   |
| Memory Usage      | 8MB         | 35MB           | 4.4x  |
| Clearing          | 0.01ms      | 0.5ms          | 50x   |

## Implementation Guidelines

### When to Choose C++

- Real-time systems requiring deterministic timing  
- Memory-constrained environments  
- Applications needing precise memory control  
- Performance-critical numerical computations  

### When to Choose Python

- Rapid prototyping and development  
- When developer productivity outweighs performance needs  
- Applications with dynamic sizing requirements  
- Scripting and glue code implementations  

## Code Examples

### C++ Fixed Array with Bounds Checking

```cpp
template <size_t N>
class SafeArray {
    int data[N];
public:
    int& operator[](size_t i) {
        if (i >= N) throw std::out_of_range("Index out of bounds");
        return data[i];
    }
};

## Python Type-Annotated Fixed Array

```python
from typing import List, TypeVar

T = TypeVar('T')
class FixedArray:
    def __init__(self, size: int, default: T = None):
        self._data: List[T] = [default] * size
    
    def __getitem__(self, idx: int) -> T:
        if not 0 <= idx < len(self._data):
            raise IndexError("Array index out of range")
        return self._data[idx]

## Conclusion

This comparison reveals fundamental tradeoffs between C++ and Python for array implementations:

- **C++** provides superior performance and memory control at the cost of development complexity  
- **Python** offers developer-friendly syntax and automatic memory management with performance overhead  
- **Hybrid approaches** (Python for interfaces, C++ for core computations) often provide optimal results  

Choose based on your project's specific requirements for performance, control, and development speed.
