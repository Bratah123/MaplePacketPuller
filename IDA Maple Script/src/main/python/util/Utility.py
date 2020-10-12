import os

from src.main.python.constants.DirectoryConstants import PRINT, FUNC_DIR, GET_ALL_DECODES
from src.main.python.constants.KeyWords import KEYWORDS, KEYWORDS_PRINT
from src.main.python.enum.AnalysisType import AnalysisType


class Util:

    @staticmethod
    def is_decode_func(func_name):
        for key in KEYWORDS:
            if key in func_name:
                return True
        return False

    @staticmethod
    def print_dbg(msg):
        if PRINT:
            print(msg)

    @staticmethod
    def get_func_list():
        print("Here is a list of functions that can be processed:")
        print("--------------------------------------------------")
        listOfEntries = []  # read contents of dir using os.scandir() from Python 3.6
        for num, entry in enumerate(sorted(os.scandir(FUNC_DIR), key=lambda e: e.name), start=1):
            # print all entries that are files
            if entry.is_file():
                listOfEntries.append(entry.name[:-4])
                print(f"{num}. {listOfEntries[num - 1]}")  # strip file extension via string splice
        print("--------------------------------------------------")
        return listOfEntries

    @staticmethod
    def get_func_to_write():
        listOfEntries = Util.get_func_list()
        choice = int(input("What function would you like to analyze? (Enter number without the period): \n"))
        print(f" You have selected: {listOfEntries[choice - 1]} \n")
        print("--------------------------------------------------")
        return listOfEntries[choice - 1]

    @staticmethod
    def check_keyword_and_print(keyword):
        for key in KEYWORDS:
            if key in keyword.lower():
                if key != "if" and key != "else":
                    Util.print_dbg(f"{KEYWORDS_PRINT[KEYWORDS.index(key)]}")
            elif key not in keyword.lower() and "decode" in keyword.lower() and GET_ALL_DECODES:  # just incase our keywords array doesn't have that decode already set
                Util.print_dbg(keyword)
            return True
        return False

    @staticmethod
    def check_keyword_and_return(keyword):
        for key in KEYWORDS:
            if key in keyword.lower():
                if key != "if" and key != "else":
                    return KEYWORDS_PRINT[KEYWORDS.index(key)]
            elif key not in keyword.lower() and "decode" in keyword.lower() and GET_ALL_DECODES:
                return keyword  # just in case our keywords array doesn't already have that Decode saved
        return ""

    @staticmethod
    def add_decode_to_list(list, keyword):
        for key in KEYWORDS:
            if key in keyword.lower():
                if key != "if" and key != "else":
                    list.append(KEYWORDS_PRINT[KEYWORDS.index(key)])
        return list

    @staticmethod
    def return_analysis_types():
        print("1.Packet Structure Analysis\n2.InHeader Opcode Analysis\n")

    @staticmethod
    def get_analysis_type():
        Util.return_analysis_types()
        choice = int(input("Which type of Analysis would you like to do?\nPlease input a number without the period.\n"))
        if choice == 1:
            return AnalysisType.PacketStruct
        elif choice == 2:
            return AnalysisType.InHeaderAnalysis
