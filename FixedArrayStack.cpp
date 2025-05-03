#include <iostream>
using namespace std;

const int MAX_SIZE = 100; // Compile-time fixed size

int main() {
    int arr[MAX_SIZE];
    int current_size = 0;
    
    cout << "Enter elements (max " << MAX_SIZE << "), enter -1 to stop:\n";
    int val;
    while (current_size < MAX_SIZE && (cin >> val) && val != -1) {
        arr[current_size++] = val;
    }

    cout << "Fixed Stack Array Contents:\n";
    for (int i = 0; i < current_size; i++) {
        cout << "arr[" << i << "] = " << arr[i] << endl;
    }

    return 0;
}