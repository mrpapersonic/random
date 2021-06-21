import os
import argparse
import sys


def main(argv):
    global outputfile
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-o', '--output', help="output file, defaults to urls.txt",
        metavar='<output>', required=True)
    args = parser.parse_args()
    if args.output:
        outputfile = args.output
    a = ["257892", "226942", "236297", "216039", "221711", "267371", "235905",
         "266808", "262036", "206069", "245304", "166174", "175220", "244327",
         "191049", "147577", "188940", "240543", "165264", "267384", "220882",
         "244859", "227446", "259322", "259862", "267372", "234932", "247540",
         "253687", "259569", "259758", "259555", "242505", "255388", "262042",
         "231290", "250827", "247175", "258728", "264370", "146718", "202230",
         "259668", "259848", "259542", "266772", "267243", "264901", "263960",
         "262771", "259420", "188717", "259727", "257889", "259904", "247703",
         "244427", "242070", "238845", "228510", "258136", "259906", "259986",
         "216926", "197648", "228426", "225259", "229779", "228922", "103383",
         "232854", "156069", "122984", "260026", "259634", "160556", "100094",
         "169468", "204746", "219077", "259610", "259348", "258669", "256097",
         "118282", "269329", "173023", "186446", "229948", "256088", "260028",
         "260058", "259557", "259497", "122220", "269582", "270455", "256776",
         "238651", "242543", "260111", "260088", "259880", "258977", "260097",
         "263329", "127727", "256789", "256787", "217410", "259765", "259359",
         "260138", "259617", "107965", "269413", "268926", "208174", "211112",
         "225664", "197255", "260276", "260209", "260210", "260203", "266834",
         "196341", "267924", "258212", "248769", "191360", "191390", "248933",
         "257567", "227913", "219077", "204746", "204066", "007693", "007695",
         "211648", "210240", "260626", "259622", "257991", "017131", "130602",
         "172787", "043168", "050856", "213966", "260623", "149112", "252168",
         "198203", "056657", "064707", "162677", "079712", "167450", "114783",
         "220958", "244387", "243734", "223315", "102346", "183783", "114427",
         "119726", "142154", "118069", "136188", "260686", "241777", "260912",
         "152889", "186055", "204746", "270536", "270528", "142154", "119298",
         "261174", "258301", "256808", "270415", "270393", "270240", "269871",
         "269834", "169134", "220354", "260271", "261725", "261378", "269821",
         "269740", "269721", "269672", "269649", "252174", "261928", "114427",
         "187003", "147572", "269638", "269434", "269279", "256302", "242517",
         "249458", "157767", "224316", "175294", "258450", "212347", "268820",
         "268306", "266301", "265066", "233864", "236128", "261162", "174036",
         "187205", "270424", "269374", "269067", "268742", "267859", "210873",
         "193318", "110232", "199310", "193816", "270629", "270628", "270517",
         "270435", "270174", "220376", "193814", "193815", "219068", "220386",
         "269064", "269653", "279474", "269366", "268487", "177642", "188269",
         "181837", "220377", "119293", "268328", "268423", "267935", "265575",
         "265453", "257528", "258926", "262384", "105951", "259904", "265002",
         "265085", "270559", "270347", "266882", "208174", "249229", "245644",
         "262538", "234818", "266442", "264901", "263960", "262771", "262326",
         "216845", "149212", "134442", "135927", "262447", "261539", "269370",
         "258301", "256785", "256808", "261811", "261650", "261225", "261226",
         "260761", "255351", "253306", "242070", "235763", "230437", "250327",
         "192327", "167801", "150309", "123554", "233736", "260606", "253099",
         "236707", "231576"]
    if os.path.exists(outputfile):
        answer = ""
        while answer not in ["y", "n", "yes", "no"]:
            print(f"{outputfile} still exists. Delete it? [y/n]: ", end="")
            answer = input().lower()
        if answer in ["y", "yes"]:
            os.remove(outputfile)
        else:
            sys.exit()
    for i in a:
        myfile = open(outputfile, "a")
        myfile.write(f"https://nhentai.org/g/{i}\n")
        myfile.close()
    print("URLs successfully written!")


if __name__ == "__main__":
    main(sys.argv[1:])
