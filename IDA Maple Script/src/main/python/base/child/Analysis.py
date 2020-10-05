# @author Brandon Nguyen
# A Script that pulls packet structure from given Maplestory IDA Pseudocode
# Script is assuming you have named all/most the decodes functions needed in your function you want to analyze
# IDA Python can make use of Hex to do the same thing
import time

from src.main.python.base.Analyzer import Analyzer
from src.main.python.constants.DirectoryConstants import FUNC_DIR, FUNC_OUTPUT_DIR
from src.main.python.constants.KeyWords import KEYWORDS
from src.main.python.util.Utility import Util


class PacketAnalysis(Analyzer):
    """
    Extends Analyzer Base Class
    This class is for analyzing packet structure
    """

    def __init__(self, txt_file_name):
        super().__init__(txt_file_name)
        self._packet_struct = ""

    def write_func_output(self):
        """
            Writes a txt file with the packet structure of the given IDA function
            packet_struct: String
        """
        f = open(f"{FUNC_OUTPUT_DIR}/{self.txt_file_name}Out.txt", "w")
        f.write(self.packet_struct)
        f.close()

    def analyze_packet_structure(self):
        """
            Pulls key words from the given function and writes
            them only showing Decodes in order
            function : String
        """
        packet_struct = ""
        start_time = time.time()
        func_name = self.get_func_name()

        in_if_statement = False

        arr_index = 0  # file starts at 0 cause its an array
        packet_struct += func_name
        Util.print_dbg("Packet Anaylzer, @author Brandon Nguyen")
        Util.print_dbg("Analyzing Packet Structure, this may take a while....\n")
        f = open(f"{FUNC_DIR}/{self.txt_file_name}.txt", "r")
        file = f.readlines()
        Util.print_dbg(func_name)
        for line in file:

            decodes_in_if = []
            if_or_else = ""
            # It would prob be easier to print the line like it is in the txt file as it is already spaced
            if KEYWORDS[5] in line or KEYWORDS[6] in line:  # check if we are at an if / else statement
                if KEYWORDS[5] in line:
                    if_or_else += "if " + Util.check_keyword_and_return(line) + ":"
                if KEYWORDS[6] in line:
                    if_or_else += "else:"
                check_next_line = file[arr_index + 1] == "  {\n"  # check if its a non nested if
                if Util.is_decode_func(file[
                                           arr_index + 1]):  # if the if statement is a one liner condition, we have to check if that one line is a decode
                    Util.print_dbg(Util.check_keyword_and_return(file[arr_index + 1]))
                if check_next_line:  # if we are in the scope of an if, find when it ends
                    i = 1
                    while file[arr_index + i] != "  }\n":
                        decodes_in_if = Util.add_decode_to_list(decodes_in_if, file[arr_index + i])
                        i += 1
                in_if_statement = check_next_line

            if len(decodes_in_if) > 0 and in_if_statement:
                Util.print_dbg(if_or_else)
                packet_struct += if_or_else + "\n"
                for decode in decodes_in_if:
                    Util.print_dbg(f"  {decode}")
                    packet_struct += "  " + decode + "\n"
            elif Util.check_keyword_and_print(line):  # if we aren't in an if statement print out the decodes normally
                packet_struct += Util.check_keyword_and_return(line) + "\n"

            arr_index += 1

        end_time = time.time()
        Util.print_dbg(f"\nFinished analysis in {end_time - start_time} seconds!")
        f.close()
        self.packet_struct = packet_struct
        return packet_struct

    def beautify(self):
        f = open(f"{FUNC_OUTPUT_DIR}/{self.txt_file_name}Out.txt")
        file_list = f.readlines()
        f.close()
        return [s.rstrip('\n') for s in file_list]

    @property
    def packet_struct(self):
        return self._packet_struct

    @packet_struct.setter
    def packet_struct(self, packet):
        self._packet_struct = packet

    def run(self):
        """
        Function that executes all steps needed
        to analyze these packets!
        """
        self.analyze_packet_structure()  # this will auto-assign the packet_struct property

        print(f"Saving down packet structure to {self.txt_file_name.upper()}out.txt \n")
        print("--------------------------------------------------")
        self.write_func_output()

        packet_struct_arr = self.beautify()

        write_output = ""
        for word in packet_struct_arr:  # re adds all the strings to make it cleaner
            if word != '':
                write_output += f"{word}\n"

        beautified_arr = write_output.split("\n")

        clean_output = ""
        beautified_len = len(beautified_arr)

        for i in range(beautified_len):  # removes all empty do while() with no decodes inside them
            if beautified_arr[i] == "do:" and beautified_arr[i + 1] == "while()":
                beautified_arr[i] = ''
                beautified_arr[i + 1] = ''
            if beautified_arr[i] == "  do:" and beautified_arr[i + 1] == "  while()":
                beautified_arr[i] = ''
                beautified_arr[i + 1] = ''

        for i in range(beautified_len):
            # checking for any contents inside a do while loop and spacing them out for visual aesthetics
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
                print("Some error occured, but it shouldn't affect the decodes() just has to do with aesthetics:", e)

        for word in beautified_arr:  # re adds all the strings after removing do while()
            if word != '':
                clean_output += f"{word}\n"

        self.packet_struct = clean_output # set packet_struct to the new clean output for the rewrite
        print("Cleaned-up packet structure: \n")
        print(clean_output)
        print("--------------------------------------------------")
        self.write_func_output()
        raise SystemExit("Analysis complete. Results written to the FuncOutput folder. \n Process will now "
                         "terminate!")

