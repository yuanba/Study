#include <iostream>
#include <cstring> 
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

char data[100005];
int t;
int status;

int main() {
	int t;
	scanf("%d",&t);
	getchar(); //Inorder to eat the character which belong to the scanf function!
	while (t--) {
		gets(data);
		status = 0;
		int i, j;
		//Eat the sapce which is in the head and the tail!
		for (i = 0; i < strlen(data); i++) if (data[i] != ' ') break;
		for (j = strlen(data) - 1; j >= 0;j--) if (data[j] != ' ') break;
		//End!
		//In the DFA Graph to hold the status!
		for (int k = i; k <= j; k++) 
		{
			compile(data[k]);
			if(status == -1) break;
		}
		if (status == 2 || status == 3 || status == 4 || status == 7 || status == -1) printf("ILLEGAL\n");
		else printf("LEGAL\n");
	}
	return 0;
}


void compile(char c) {
	switch(status) 
	{
		case 0:
			if (c >= '0'&&c <= '9') status = 1;
			else if (c == '+' || c == '-') status = 2;
			else if (c == 'e' || c == 'E') status = 3;
			else status = -1;
			break;
		case 1:
			if (c >= '0'&&c <= '9') status = 1;
			else if (c == 'e' || c == 'E') status = 3;
			else if (c == '.') status = 4;
			else status = -1;
			break;
		case 2:
			if (c >= '0'&&c <= '9') status = 1;
			else status = -1;
			break;
		case 3:
			if (c >= '0'&&c <= '9') status = 6;
			else if (c == '+' || c == '-') status = 7;
			else status = -1;
			break;
		case 4:
			if (c >= '0'&&c <= '9') status = 5;
			else status = -1;
			break;
		case 5:
			if (c >= '0'&&c <= '9') status = 5;
			else if (c == 'e' || c == 'E') status = 3;
			else status = -1;
			break;
		case 6:
			if (c >= '0'&&c <= '9') status = 6;
			else status = -1;
			break;
		case 7:
			if (c >= '0'&&c <= '9') status = 6;
			else status = -1;
			break;
		}
}	
