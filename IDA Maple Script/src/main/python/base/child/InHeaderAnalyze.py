# @author Brandon Nguyen
# Simple Class that finds InHeader ops
from src.main.python.base.child.Analysis import FUNC_DIR
from src.main.python.base.Analyzer import Analyzer


class InHeader(Analyzer):
    """
    Extends Analyzer Base Class
    Gets InHeader Ops
    """

    def __init__(self, txt_file_name):
        super().__init__(txt_file_name)

    def get_inheader_ops(self):
        """
            Just reads all the lines looking for coutpacket::coutpacket

            :Return: String[]
        """
        f = open(f"{FUNC_DIR}/{self.txt_file_name}.txt", "r")
        file = f.readlines()
        f.close()
        total_ops = []
        print(self.get_func_name())
        for line in file:
            if "coutpacket::coutpacket" in line.lower():
                print(line.strip())
                total_ops.append(line)
        return total_ops

    def run(self):
        opcodes = self.get_inheader_ops()
        if len(opcodes) < 1:
            print("No InHeaders were found for this function.")
        raise SystemExit("Analysis complete. Results written to the FuncOutput folder. \n Process will now terminate!")
