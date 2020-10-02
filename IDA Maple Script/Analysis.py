# @author Brandon Nguyen
# A Script that pulls packet structure from given Maplestory IDA Pseudocode
# Script is assuming you have named all/most the decodes functions needed in your function you want to analyze
# IDA Python can make use of Hex to do the same thing
import os
import time
from KeyWords import KEYWORDS, KEYWORDS_PRINT

FUNC_DIR = "Functions"
FUNC_OUTPUT_DIR = "FuncOutput"
PRINT = False # True to allow the program to print analysis in real time

# Technically more accurate when searched this way, but False to have it neatly put
GET_ALL_DECODES = False # When turned to true, it will search for all words with "decode" in them rather than the array in KeyWords.py

def is_decode_func(func_name):
    for key in KEYWORDS:
        if key in func_name:
            return True
    return False

def print_dbg(msg):
    if PRINT == True:
        print(msg)

def check_keyword_and_print(word):
    for key in KEYWORDS:
        if key in word.lower():
            if key != "if" and key != "else":
                print_dbg(f"{KEYWORDS_PRINT[KEYWORDS.index(key)]}")
        elif key not in word.lower() and "decode" in word.lower() and GET_ALL_DECODES: # just incase our keywords array doesn't have that decode already set
            print_dbg(word)
        return True
    return False

def check_keyword_and_return(word):
    for key in KEYWORDS:
        if key in word.lower():
            if key != "if" and key != "else":
                return KEYWORDS_PRINT[KEYWORDS.index(key)]
        elif key not in word.lower() and "decode" in word.lower() and GET_ALL_DECODES:
            return word # just in case our keywords array doesn't already have that Decode saved
    return "";

def get_func_list():
	print("Here is a list of functions that can be processed:")
	print("--------------------------------------------------")
	listOfEntries = [] # read contents of dir using os.scandir() from Python 3.6
	for num, entry in enumerate(sorted(os.scandir(FUNC_DIR), key = lambda e: e.name), start = 1):
		# print all entries that are files
		if entry.is_file():
			listOfEntries.append(entry.name[:-4])
			print(f"{num}. {listOfEntries[num-1]}") #strip file extension via string splice
	print("--------------------------------------------------")
	return listOfEntries

def get_func_to_write():
	listOfEntries = get_func_list()
	choice = int(input("What function would you like to analyze? (Enter number without the period): \n"))
	print(f" You have selected: {listOfEntries[choice-1]} \n")
	print("--------------------------------------------------")
	return listOfEntries[choice-1]

def write_func_output(packet_struct, func_name):
    """
        Writes a txt file with the packet structure of the given IDA function
        packet_struct: String
    """
    f = open(f"{FUNC_OUTPUT_DIR}/{func_name}Out.txt", "w")
    f.write(packet_struct)
    f.close()

def analyze_packet_structure(function):
    """
        Pulls key words from the given function and writes them only showing Decodes in order
        function : String
    """
    packet_struct = ""
    start_time = time.time()
    func_name = get_func_name(function)

    in_if_statement = False

    arr_index = 0 # file starts at 0 cause its an array
    packet_struct += func_name
    print_dbg("Packet Anaylzer, @author Brandon Nguyen")
    print_dbg("Analyzing Packet Structure, this may take a while....\n")
    f = open(f"{FUNC_DIR}/{function}.txt", "r")
    file = f.readlines()
    print_dbg(func_name)
    for line in file:

        decodes_in_if = []
        if_or_else = ""
        # It would prob be easier to print the line like it is in the txt file as it is already spaced
        if KEYWORDS[5] in line or KEYWORDS[6] in line: # check if we are at an if / else statement
            if KEYWORDS[5] in line:
                if_or_else += "if " + check_keyword_and_return(line) + ":"
            if KEYWORDS[6] in line:
                if_or_else += "else:"
            check_next_line = file[arr_index + 1] == "  {\n" # check if its a non nested if
            if is_decode_func(file[arr_index + 1]): # if the if statement is a one liner condition, we have to check if that one line is a decode
                print_dbg(check_keyword_and_return(file[arr_index + 1]))
            if check_next_line: # if we are in the scope of an if, find when it ends
                i = 1
                while file[arr_index + i] != "  }\n":
                    decodes_in_if = add_decode_to_list(decodes_in_if, file[arr_index + i])
                    i += 1
            in_if_statement = check_next_line

        if len(decodes_in_if) > 0 and in_if_statement:
            print_dbg(if_or_else)
            packet_struct += if_or_else + "\n"
            for decode in decodes_in_if:
                print_dbg(f"  {decode}")
                packet_struct += "  " + decode + "\n"
        elif check_keyword_and_print(line): # if we aren't in an if statement print out the decodes normally
            packet_struct += check_keyword_and_return(line) + "\n"

        arr_index += 1

    end_time = time.time()
    print_dbg(f"\nFinished analysis in {end_time - start_time} seconds!")
    f.close()
    return packet_struct

def get_func_name(txt_file_name):
    f = open(f"{FUNC_DIR}/{function}.txt", "r")
    func_name = f.readline() # The func name is always gonna be at the top
    f.close()
    return func_name

def add_decode_to_list(list, word):
    for key in KEYWORDS:
        if key in word.lower():
            if key != "if" and key != "else":
                list.append(KEYWORDS_PRINT[KEYWORDS.index(key)])
    return list

def beautify(file_name):
    f = open(file_name)
    file_list = f.readlines()
    f.close()
    return [s.rstrip('\n') for s in file_list]

if __name__ == '__main__':
    function = get_func_to_write()
    packet_struct = analyze_packet_structure(function)

    print(f"Saving down packet structure to {function.upper()}out.txt")

    write_func_output(packet_struct, function) # write the txt file so we can beautify it
    packet_struct_arr = beautify(f"{FUNC_OUTPUT_DIR}/{function.upper()}out.txt") # removes all the newlines from the txt file we just created

    write_output = ""

    for word in packet_struct_arr: # re adds all the strings to make it cleaner
        if word != '':
            write_output += f"{word}\n"

    beautified_arr = write_output.split("\n")

    clean_output = ""
    beautified_len = len(beautified_arr)

    for i in range(beautified_len): # removes all empty do while() with no decodes inside them
        if beautified_arr[i] == "do:" and beautified_arr[i + 1] == "while()":
            beautified_arr[i] = ''
            beautified_arr[i + 1] = ''
        if beautified_arr[i] == "  do:" and beautified_arr[i + 1] == "  while()":
            beautified_arr[i] = ''
            beautified_arr[i + 1] = ''

    for i in range(beautified_len): # checking for any contents inside a do while loop and spacing them out for visual aesthetics
        if beautified_arr[i] == "do:":
            j = i + 1
            while beautified_arr[j] != "while()":
                beautified_arr[j] = f"  {beautified_arr[j]}"
                j += 1
        # some functions, this will cause an index out of range error (comment out this part if so)
        try:
            if beautified_arr[i] == "  do:":
                j = i + 1
                while beautified_arr[j] != "  while()":
                    beautified_arr[j] = f"   {beautified_arr[j]}"
                    j += 1
        except Exception as e:
            print("Some error occured, but it shouldn't affect the decodes() just has to do with aesthetics")

    for word in beautified_arr: # re adds all the strings after removing do while()
        if word != '':
            clean_output += f"{word}\n"

    print(clean_output)
    write_func_output(clean_output, function) # save it to an output file
