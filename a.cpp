
#include <string>
#include <iostream>
#include <vector>
#include <fstream>
#include <stdio.h>
#include <std.cpp>

#include "/home/unity/Workspace/Voxel-2.0/libc/helloworld/helloworld.cpp"
int add(int x, int y) {
return x+y;
}
int main(char argv[], int argc) { 
std::string from = "aeiou";
std::string to = "12345";
const auto translate = maketrans(from, to);
std::string str = "hello Mike!";;
std::cout << translate(str) << std::endl;;
return add(2,3);
}
