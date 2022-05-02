// TestExamples.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "MyString.h"
#include <vector>
#include <algorithm>

using namespace strings;

bool cmp(MyString str1, MyString str2)
{
	char* p1 = str1.GetP();
	char* p2 = str2.GetP();
	int len1 = str1.GetLength();
	int len2 = str2.GetLength();
	if (len2==0) {return false;}
	if (len1==0) {return true;}
	int i=0;
	while ((i<len1) && (i<len2))
	{
		if (p1[i]<p2[i]) {return true;}
		if (p1[i]>p2[i]) {return false;}
		++i;
	}
	if ((len1==len2) || (i==len2)) {return false;}
	else {return true;}
}

std::vector<MyString> MySort(std::vector<MyString> strlist)
{
	std::sort(strlist.begin(),strlist.end(), cmp);
	return strlist;
}

int _tmain(int argc, _TCHAR* argv[])
{
	std::cout<<"Testing the strings:"<<'\n';
	char* p = "Hallo!";
	MyString mystr(6,p);
	try
	{
	std::cout<<mystr<<'\n';

	MyString m4; m4=mystr;
	std::cout<<m4<<'\n';

	MyString m2(m4);
	m4.~MyString();
	m2=m2;
	std::cout<<m2<<'\n';
	MyString m5=m2;
	std::cout<<m5<<'\n';
	m5 = MyString(3,"123");
	std::cout<<m5<<'\n';
	m5 = MyString(10,"0123456789");
	std::cout<<m5<<'\n';
	std::cout<<m4 + m2 + m4<<'\n';
	m4 = MyString(16,"qwertyqwerty qwerty");
	m4 = m4 + m4;
	std::cout<<m4<<'\n';
	m4.~MyString();
	std::cout<<m4<<'\n';
	}
	catch(MyStringEmpty obj)
	{std::cerr<<'\n'<<obj.GetVar()<<'\n';}
	catch(MyStringFull obj)
	{std::cerr<<'\n'<<obj.GetVar()<<'\n';}
	catch(...)
	{std::cerr<<'\n'<<"Unknown error!"<<'\n';}

	std::cout<<'\n'<<"Before sorting:"<<'\n';
	std::vector<MyString> strlist;
	strlist.push_back(MyString(7,"wswswsw"));
	strlist.push_back(MyString(5,"axcel"));
	strlist.push_back(MyString(6,"axcel3"));
	strlist.push_back(MyString(5,"basis"));
	strlist.push_back(MyString(5,"feria"));
	strlist.push_back(MyString(7,"Venezia"));
	strlist.push_back(MyString(4,"Roma"));
	strlist.push_back(MyString(3,"Ple"));
	strlist.push_back(MyString(4,"ATVO"));
	strlist.push_back(MyString(7,"viaggia"));
	strlist.push_back(MyString(4,"1150"));
	strlist.push_back(MyString(5,"Marco"));
	strlist.push_back(MyString(7,"Shuttle"));
	strlist.push_back(MyString(6,"Hallo!"));
	strlist.push_back(MyString(7,"Shuttle"));
	strlist.push_back(MyString(6,"Hallo!"));
	strlist.push_back(MyString(10,"Hallo  hallo!"));

	for (std::vector<MyString>::const_iterator iter = strlist.begin(); iter!= strlist.end(); ++iter)
	{
		std::cout<<'\n'<<*iter;
	}

	strlist = MySort(strlist);
	std::cout<<'\n'<<"SORTING:"<<'\n';

	for (std::vector<MyString>::const_iterator iter = strlist.begin(); iter!= strlist.end(); ++iter)
	{
		std::cout<<'\n'<<*iter;
	}

	std::cout<<'\n'<<"Press ENTER to exit the program!"<<'\n';
	getchar();

	return 0;
}