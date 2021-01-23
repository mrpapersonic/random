// requires libcurl
#include <curl/curl.h>
#include <iostream>
#include <string.h>
#include <fstream>

int main(int argc, char * argv[]) {
    if (argc != 3) {
        std::cout << "usage: " << argv[0] << " <input> <output>";
        return 0;
    }
    std::string encoded;
    CURL * curl = curl_easy_init();
    char somedata[256];
    std::ifstream in (argv[1], std::ios:: in | std::ios::binary);
    if (in) {
        in .seekg(0, std::ios::end);
        encoded.resize( in .tellg()); in .seekg(0, std::ios::beg); in .read( & encoded[0], encoded.size()); in .close();
    }
    int outlength;
    char * cres = curl_easy_unescape(curl, encoded.c_str(), encoded.length(), & outlength);
    std::string res(cres, cres + outlength);
    curl_free(cres);
    curl_easy_cleanup(curl);
    std::ofstream myfile2;
    myfile2.open(argv[2]);
    myfile2 << res;
    myfile2.close();
    return 0;
}
