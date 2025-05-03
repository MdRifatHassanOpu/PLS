#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> arr;
    cout << "Enter elements (enter -1 to stop):\n";
    
    int val;
    while (cin >> val && val != -1) {
        arr.push_back(val);
    }

    cout << "Dynamic Heap Array Contents:\n";
    for (size_t i = 0; i < arr.size(); i++) {
        cout << "arr[" << i << "] = " << arr[i] << endl;
    }

    cout << "Current capacity: " << arr.capacity() << endl;
    return 0;
}