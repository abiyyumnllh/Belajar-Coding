#include <iostream>
using namespace std;

int main()
{
    int nilai;

    do {
        cout << "masukkan nilai siswa : ";
        cin >> nilai;

    } while (nilai > 100 || nilai < 0 );

    if (nilai >= 90){
        cout << "siswa mendapatkan grade A"<<endl;
    } else if (nilai >= 75){
        cout << "siswa mendapatkan grade B"<<endl;
    } else if (nilai >= 60){
        cout << "siswa mendapatkan grade C"<<endl;
    } else {
        cout << "siswa mendapatkan grade D"<<endl;
    }

    return 0;
}