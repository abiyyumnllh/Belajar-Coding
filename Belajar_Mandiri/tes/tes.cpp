#include <iostream>
using namespace std;

int main() {
    int pilihan;
    int total = 0;

    while (pilihan != 0){
        cout << "masukkan bilangan bulat : ";
        cin >> pilihan;

        total += pilihan;

    }
    cout << "total penjumlahan dari semua bilangan bulat adalah "<<total<<endl;

    return 0;
}