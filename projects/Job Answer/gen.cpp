
#include <bits/stdc++.h>

using namespace std;

string name[10] = {"rich", "ben", "matthew", "noah", "jacob", 
	               "annie", "camielle", "madlen", "romanova", "paige"};
string sport[5] = {"bachelor", "magister", "doctor"};
string lesson[5] = {"yes", "no"};
string color[5] = {"elementary", "intermediate", "advanced"};
string animal[5] = {"low", "medium", "high"};
string Friend[5] = {"accepted", "rejected"};

int main() {
	freopen ("out.txt", "w", stdout);
	srand(time(0));
	for (int i = 0; i < 100; ++i) {
		int x;
		x = rand() % 10;
		cout << name[x] << " ";
		x = rand() % 3;
		cout << sport[x] << " ";
		x = rand() % 2;
		cout << lesson[x] << " ";
		x = rand() % 3;
		cout << color[x] << " ";
		x = rand() % 3;
		cout << animal[x] << " ";
		x = rand() % 2;
		cout << Friend[x] << "\n";		
	}
	return 0;
}
