#include <iostream>
using namespace std;

int main() {
   int nilai;
   int totalTidakLulus = 0;
   int totalLulus = 0;

   for (int i = 1; i <= 5; i++){
      cout << "masukkan nilai siswa : ";
      cin >> nilai;

      if (nilai >= 75) {
         cout << "siswa dinyatakan lulus"<<endl;
         totalLulus += 1;
      } else {
         cout << "siswa dinyatakan tidak lulus"<<endl;
         totalTidakLulus += 1;
      }
   }
   cout << "jumlah siswa yang lulus       : "<<totalLulus<<endl;
   cout << "jumlah siswa yang tidak lulus : "<<totalTidakLulus<<endl;
   return 0;
}