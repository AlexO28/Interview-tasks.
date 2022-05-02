#ifndef MYSTRING_H
#define MYSTRING_H
#include <iostream>

namespace strings
{
class MyString
{
private:
	char* p;
	unsigned short int len;
	void MakeCopy(const MyString& mystr);

public:
	MyString()
	{
		len=0; p=0;
	}
	MyString(const unsigned short int len0, const char* p0);
	~MyString()
	{
		if (len>0) {len=0; delete[] p;}
	}
	MyString(const MyString& mystr)
	{
		if (this!=&mystr)
		{
			MakeCopy(mystr);
		}
	}
	MyString& operator=(const MyString& mystr);
	unsigned short int GetLength() {return len;}
	char* GetP() {return p;}
	friend MyString operator+(const MyString& mystr1, const MyString& mystr2);
	friend std::ostream& operator<<(std::ostream& os, const MyString& mystr);
};
//two exception classes
class MyStringFull 
{
private: 
	char* errmess;
public:
	MyStringFull() {errmess = "Concatenation error: sum of two strings is too long!";}
	const char* GetVar() {return errmess;}
};

class MyStringEmpty
{
private:
	char* errmess;
public:
	MyStringEmpty() {errmess = "Output error: the string is empty!";}
	const char* GetVar() {return errmess;}
};
}
#endif