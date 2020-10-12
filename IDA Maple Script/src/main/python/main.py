# Main function/Scripting Sequence
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__))))))

from src.main.python.base.child.Analysis import PacketAnalysis
from src.main.python.base.child.InHeaderAnalyze import InHeader
from src.main.python.enum.AnalysisType import AnalysisType
from src.main.python.util.Utility import Util


def main():

    analysis_type = Util.get_analysis_type()
    function = Util.get_func_to_write()

    if analysis_type == AnalysisType.PacketStruct:
        packet_analyzer = PacketAnalysis(function)
        packet_analyzer.run()
    elif analysis_type == AnalysisType.InHeaderAnalysis:
        inheader_analyzer = InHeader(function)
        inheader_analyzer.run()


if __name__ == "__main__":
    main()
