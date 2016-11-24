
#include <bits/stdc++.h>

using namespace std;

string name[10] = {"john", "matt", "ben", "rich", "james", 
	               "suzanne", "chris", "lindsey", "shakira", "annie"};
string sport[3] = {"fight", "team_game", "versus"};
string lesson[3] = {"logic", "art", "humanities"};
string color[3] = {"red", "green", "blue"};
string animal[4] = {"mammal", "fish", "bird", "reptile"};
string Friend[2] = {"yes", "no"};

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
		cout << lesson[x] << " ";
		x = rand() % 3;
		cout << color[x] << " ";
		x = rand() % 4;
		cout << animal[x] << " ";
		x = rand() % 2;
		cout << Friend[x] << "\n";		
	}
	return 0;
}
