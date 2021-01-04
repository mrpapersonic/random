/* Windows 95 Keygen - 11/24/20
   By Paper
   not sure if this will work fully, but from what i've seen it works well enough
*/
#include <ctime>

#include <cstdlib>

#include <cstring>

#include <iomanip>

#include <iostream>

#include <string>

int a(), b(), c(), d(), e();
int main(int argc, char * argv[]) {
  int endpoint, startpoint, sadsong;
  srand((unsigned) time(NULL));
  if (argc >= 2) {
    if (strcmp(argv[1], "--office") == 0) {
      startpoint = c();
      sadsong = 4;
    } else if (strcmp(argv[1], "--oem") == 0) {
      int first = d(), third = e();
      std::cout << std::setw(5) << std::setfill('0') << first;
      std::cout << "-OEM-";
      std::cout << std::setw(7) << std::setfill('0') << third << "-";
      std::cout << std::setw(5) << std::setfill('0') << (rand() % 100000);
      return 0;
    } else if (strcmp(argv[1], "--normal") == 0) {
      startpoint = a();
      sadsong = 3;
    } else {
      std::cout << "usage: " << argv[0] << " [--normal] [--oem] [--office]";
      return 0;
    }
  } else {
    std::cout << "usage: " << argv[0] << " [--normal] [--oem] [--office]";
    return 0;
  }
  endpoint = b();
  std::cout << std::setw(sadsong) << std::setfill('0') << startpoint << "-";
  std::cout << std::setw(7) << std::setfill('0') << endpoint;
  return 0;
}
int a() {
  int num;
  num = rand() % 1000;
  while ((num == 333) and(num == 444) and(num == 555) and(num == 666) and(num == 777) and(num == 888) and(num == 999)) {
    num = rand() % 1000;
  }
  while ((num % 3) != 0) {
    num = num + 1;
  }
  return num;
}
int b() {
  int first_digits = rand() % 10000000;
  int last_digit = rand() % 10;
  while ((last_digit == 0) || (last_digit >= 8)) {
    last_digit = rand() % 10;
  }
  std::string thisis = std::to_string(first_digits);
  std::string veryfrustrating = std::to_string(last_digit);
  std::string second_segment_p1 = (std::string(thisis) + std::string(veryfrustrating));
  int second_segment = std::stoi(second_segment_p1);
  while (second_segment % 7 != 0) {
    first_digits = rand() % 10000000;
    last_digit = rand() % 10;
    while ((last_digit == 0) || (last_digit >= 8)) {
      last_digit = rand() % 10;
    }
    std::string thisis = std::to_string(first_digits);
    std::string veryfrustrating = std::to_string(last_digit);
    std::string second_segment_p1 = (std::string(thisis) + std::string(veryfrustrating));
    second_segment = std::stoi(second_segment_p1);
  }
  return second_segment;
}

int c() {
  int new_site = rand() % 1000;
  int ez_pwned = new_site % 10 + 1;
  while (ez_pwned >= 10) {
    ez_pwned = ez_pwned - 10;
  }
  std::string thisisstill = std::to_string(new_site);
  std::string prettyfrustrating = std::to_string(ez_pwned);
  std::string iamsocool = (std::string(thisisstill) + std::string(prettyfrustrating));
  int mysinusesareclogged = std::stoi(iamsocool);
  return mysinusesareclogged;
}

int d() {
  int day = (rand() % 366) + 1;
  const char * years[] = {
    "95",
    "96",
    "97",
    "98",
    "99",
    "00",
    "01",
    "02",
    "03"
  };
  int index = (rand() % 9);
  const char * year = years[index];
  std::string iamsotired = std::to_string(day);
  std::string ofdoingthis = year;
  std::string pleasehelp = (std::string(iamsotired) + std::string(ofdoingthis));
  int ohmygod = std::stoi(pleasehelp);
  return ohmygod;
}

int e() {
  int first_digits = rand() % 1000000;
  int last_digit = rand() % 10;
  while ((last_digit == 0) || (last_digit >= 8)) {
    last_digit = rand() % 10;
  }
  std::string thisis = std::to_string(first_digits);
  std::string veryfrustrating = std::to_string(last_digit);
  std::string second_segment_p1 = (std::string(thisis) + std::string(veryfrustrating));
  int second_segment = std::stoi(second_segment_p1);
  while (second_segment % 7 != 0) {
    first_digits = rand() % 10000000;
    last_digit = rand() % 10;
    while ((last_digit == 0) || (last_digit >= 8)) {
      last_digit = rand() % 10;
    }
    std::string thisis = std::to_string(first_digits);
    std::string veryfrustrating = std::to_string(last_digit);
    std::string second_segment_p1 = (std::string(thisis) + std::string(veryfrustrating));
    second_segment = std::stoi(second_segment_p1);
  }
  return second_segment;
}
