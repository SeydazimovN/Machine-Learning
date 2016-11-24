typedef vector <int> vint;
typedef vector < vint > vvint;

vvint A;

typedef vector <bool> bint;

void dfs(vvint temp, bint used) {
	float res = 0.0;
	int picked = -1;
	for (int col = 1; col <= 6; ++i) {
	  if (used[col]) continue;
	  float v = getEntropy(col);
	  if (v == 0) {
	    // stop
	    return;
	  }
	  if (v > res) {
	    res = v;
	    picked = col;	 
	  }
	} 
	FOR (i, 0, len[picked]) {
      vvint t[5];
      FOR (z, 0, sz(temp)) {
	    if (temp[picked])
	  }	  
	}
}
void getInput() {
	A.resize(128);
	FOR (i, 0, 128) {
		FOR (z, 0, 7) {
			A[i].push_back(x);	
		string name;
		cin >> name;	
	}
	FOR (i, 0, 7)
		used.push_back(false);
}
void solve() {
	getInput();
	dfs(A, used);
}


