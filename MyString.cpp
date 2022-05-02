#include "stdafx.h"
#include "MyString.h"
#include <climits>

namespace strings
{
inline void MyString::MakeCopy(const MyString& mystr)
{
	int len0=mystr.len;
	if (len0>0)
	{
		p = new char[len0];
		std::copy(mystr.p, mystr.p+len0, p);
	}
	len = len0;
}
inline MyString::MyString(const unsigned short int len0, const char* p0)
{
	len = len0;
	if (len>0)
	{
		p = new char[len];
		std::copy(p0, p0+len0, p);
	}
}
MyString& MyString::operator=(const MyString& mystr)
{
	if (this!=&mystr) 
	{
//hesitated, but decided not to use the temporary variable to save the data
//		char* q;
		if (len>0)
		{
//			q = new char[len];
//			std::copy(p,p+len,q);
			delete[] p;
		}
		MakeCopy(mystr);
//		delete[] q;
	}
	return *this;
}


MyString operator+(const MyString& mystr1, const MyString& mystr2)
{
	unsigned short int len;
	char* p;
	unsigned short int len1 = mystr1.len;
	unsigned short int len2 = mystr2.len;
	if (len1+len2>USHRT_MAX)
	{
		throw MyStringFull();
//decided to throw exception if the resulting string is too long
/*
		len = USHRT_MAX;
		p = new char[USHRT_MAX];
		std::copy(mystr1.p, mystr1.p+len1, p);
		std::copy(mystr2.p, mystr2.p+(len-len2), p+len1);*/
	}
	else
	{
		len = len1 + len2;
		p = new char[len];
		std::copy(mystr1.p, mystr1.p + len1, p);
		std::copy(mystr2.p, mystr2.p + len2, p + len1);
	}

	return MyString(len, const_cast<const char*>(p));
}

std::ostream& operator<<(std::ostream&os, const MyString& mystr)
{
	if (mystr.len>0)
	{
		for (int i=0; i<mystr.len; ++i)
		{
			os<<mystr.p[i];
		}
	}
	else
	{
//hesitated, but decided to throw exception in this case
		throw MyStringEmpty();
	}
	return os;
}
}