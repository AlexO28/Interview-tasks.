// BST.cpp: определяет точку входа для консольного приложения.
//

// BST.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <iostream>
#include <cstdlib>

struct TNode {
	TNode* Parent;  // Pointer to the parent node
	TNode* Left;  // Pointer to the left child node
	TNode* Right;  // Pointer to the right child node
	int Key;  // Some data
};
TNode* AddElement(TNode* pnode, int Key0) {
	TNode* temppnode = pnode;
	TNode* pparentnode = NULL;
	int choice = 0;
	while (temppnode != NULL) {
		pparentnode = temppnode;
		if (Key0 <= temppnode->Key) {
			temppnode = temppnode->Left;
			choice = -1;
		}
		else {
			temppnode = temppnode->Right;
			choice = 1;
		}
	}
	temppnode = new TNode;
	if (choice < 0) {
		pparentnode->Left = temppnode;
	}
	else if (choice > 0) {
		pparentnode->Right = temppnode;
	}
	else {
		pnode = temppnode;
	}
	temppnode->Key = Key0;
	temppnode->Parent = pparentnode;
	temppnode->Left = NULL;
	temppnode->Right = NULL;
	return(pnode);
}
void Display(TNode* pnode) {
	if (pnode != NULL) {
		std::cout<<pnode->Key<<'\n';
		if (pnode->Parent != NULL) {
			std::cout<<"Has parent";
			std::cout << (pnode->Parent)->Key << '\n';
		}
		if (pnode->Left != NULL) {
			std::cout << "Left neighbor";
			Display(pnode->Left);
		}
		if (pnode->Right != NULL) {
			std::cout << "Right neighbor";
			Display(pnode->Right);
		}
	}
	else {
		std::cout << "Tree is empty";
	}
}
void DeleteAll(TNode* pnode) {
	if (pnode != NULL) {
		DeleteAll(pnode->Left);
		DeleteAll(pnode->Right);
		delete(pnode->Left);
		delete(pnode->Right);
		pnode->Parent = NULL;
    }
}
int GetKthLargestElement(TNode* pnode, int k) {
	std::cout<<"GetKthLargestEleemnt"<<'\n';
	int num = 0;
	TNode* temppnode = pnode;
	bool upmode = false;
	while (num < k) {
		if (!upmode) {
			if (temppnode->Right) {
				++num;
			}
    		while (temppnode->Right) {
	    		temppnode = temppnode->Right;
		    }
			std::cout<<num<<"for"<<temppnode->Key<<'\n';
		}
		if (num >= k) {break;}
		if (temppnode->Left) {
			upmode = false;
			temppnode = temppnode->Left;
			++num;
			std::cout<<num<<"for"<<temppnode->Key<<'\n';
		} else {
			if (!(temppnode->Parent)) {
				std::cout<<"Not enough elements!"<<'\n';
			}
			temppnode = temppnode->Parent;
			upmode = true;
			++num;
			std::cout<<num<<"for"<<temppnode->Key<<'\n';
		}
	}
	std::cout<<"End of function"<<'\n';
	return(k);
}
int main()
{
	const int minval = -100;
	const int maxval = 100;
	const int len = 10;
	int numarr[len];
	TNode* pnode = NULL;
	for (int i = 0; i < len; ++i) {
		numarr[i] = std::rand() % (maxval - minval + 1) + minval;
		pnode = AddElement(pnode, numarr[i]);
		std::cout << numarr[i] << " ";
	}
	GetKthLargestElement(pnode, 2);
	Display(pnode);
	DeleteAll(pnode);
	char ch;
	std::cin>>ch;
    return 0;
}