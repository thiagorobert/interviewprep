// Implement a function void reverse(char *str) in C or C++ which reverses a null-terminated string.

#include <iostream>
#include <stdlib.h> //rand()
#include <string>

void reverse(const char *cin) {

  char * in = (char *) cin;
  char ch = in[0];
  int i = 0;
  for (; ch != NULL; i++) {
    ch = in[i];
    std::cout << ch;
  }

  std::cout << "\n";

  int length = i - 1;
  std::cout << "length: " << length << "\n";
  for (int j = 0, i = length - 1; j < length / 2; j++, i--) {
    char buf = in[j];
    in[j] = in[i];
    in[i] = buf;

  }

  for (int j = 0; j < length; j++) {
	  std::cout << in[j];
  }

  std::cout << "\n";
}

int main(int argc, char *argv[]) {
    std::string in = "groovy";
		std::cout << in << "\n";
		reverse(in.c_str());
    exit(0);

} //main
