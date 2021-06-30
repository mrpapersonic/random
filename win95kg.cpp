/* Windows 95 Keygen - 11/24/20
   By Paper
   not sure if this will work fully, but from what i've seen it works well enough

   going back on this a few months later, wew this code sucks ass
   fixed the OEM key generation, the medium article i read was wrong about it
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
            std::cout << std::setw(5) << std::setfill('0') << d();
            std::cout << "-OEM-";
            std::cout << std::setw(7) << std::setfill('0') << e() << "-";
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
    int num = rand() % 1000;
    while ((num == 333) || (num == 444) || (num == 555) || (num == 666) || (num == 777) || (num == 888) || (num == 999)) {
        num = rand() % 1000;
    }
    while ((num % 3) != 0) {
        num = num + 1;
    }
    return num;
}

int b() {
    int first_digits;
    int last_digit;
    int second_segment = 5;
    while (second_segment % 7 != 0) {
        first_digits = rand() % 1000000;
        last_digit = rand() % 10;
        while ((last_digit == 0) || (last_digit >= 8)) {
            last_digit = rand() % 10;
        }
        second_segment = std::stoi(std::to_string(first_digits) + std::to_string(last_digit));
    }
    return second_segment;
}

int c() {
    int new_site = rand() % 1000;
    int ez_pwned = new_site % 10 + 1;
    while (ez_pwned >= 10) {
        ez_pwned = ez_pwned - 10;
    }
    return std::stoi(std::to_string(new_site) + std::to_string(ez_pwned));
}

int d() {
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
    return std::stoi(std::to_string((rand() % 366) + 1) + year);
}

int e() {
    int first_digits;
    int last_digit;
    int second_segment = 5;
    int sum = 1;
    while (sum % 7 != 0) {
        sum = 0;
        first_digits = rand() % 10000;
        last_digit = rand() % 10;
        while ((last_digit == 0) || (last_digit >= 8)) {
            last_digit = rand() % 10;
        }
        std::string second_segment_p1 = (std::to_string(first_digits) + std::to_string(last_digit));
        second_segment = std::stoi(second_segment_p1);
        for(char &c :second_segment_p1) {
            sum += c - '0';
        }
    }
    return second_segment;
}
