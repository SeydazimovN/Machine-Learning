
#include <bits/stdc++.h>

using namespace std;

string name[10] = {"viper", "elantra", "allante", "XLR", "testarossa", 
	               "ascari", "acecra", "lindsey", "atlantic", "roadster"};
string sport[3] = {"small", "medium", "big"};
string country[3] = {"germany", "japan", "russia"};
string color[3] = {"2.7", "3.5", "4.7"};
string animal[4] = {"mercedes", "toyota", "mitsubishi"};
string Friend[2] = {"good", "bad"};

int main() {
	freopen ("out.txt", "w", stdout);
	srand(time(0));
	for (int i = 0; i < 100; ++i) {
		int x;
		x = rand() % 10;
		cout << name[x] << " ";
		x = rand() % 3;
		cout << sport[x] << " ";
		x = rand() % 3;
		cout << country[x] << " ";
		x = rand() % 3;
		cout << color[x] << " ";
		x = rand() % 3;
		cout << animal[x] << " ";
		int cost = rand() % 50;
		int qual = rand() % 50;
		x = rand() % 2;
		cout << cost << " " << qual << " ";
		cout << Friend[x] << "\n";		
	}
	return 0;
}
