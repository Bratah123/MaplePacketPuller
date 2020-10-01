# @author Brandon Nguyen
# Simple script that finds InHeader ops
import os
from Analysis import FUNC_DIR

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
	print(f" You have selected: {listOfEntries[choice]} \n")
	print("--------------------------------------------------")
	return listOfEntries[choice]

def get_func_name(txt_file_name):
    f = open(f"{FUNC_DIR}\{txt_file_name}.txt", "r")
    func_name = f.readline() # The func name is always gonna be at the top
    return func_name

def get_inheader_ops(function):
    """
        Just reads all the lines looking for coutpacket::coutpacket

        :Return: String[]
    """
    f = open(f"{FUNC_DIR}\{function}.txt", "r")
    file = f.readlines()
    total_ops = []
    print(get_func_name(function))
    for line in file:
        if "coutpacket::coutpacket" in line.lower():
            print(line.strip())
            total_ops.append(line)
    return total_ops

def main():
    function = get_func_to_write()
    opcodes = get_inheader_ops(function)
    if len(opcodes) < 1:
        print("No InHeaders were found for this function.")

if __name__ == "__main__":
    main()
