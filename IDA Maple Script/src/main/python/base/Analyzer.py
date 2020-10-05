from src.main.python.constants.DirectoryConstants import FUNC_DIR


class Analyzer:
    """
    Base class for any Analysis Class
    Provides basic functionality like having getting functions names
    and setting function name
    """
    def __init__(self, txt_file_name=None):
        self._txt_file_name = txt_file_name

    def get_func_name(self):
        f = open(f"{FUNC_DIR}/{self._txt_file_name}.txt", "r")
        func_name = f.readline()  # The func name is always gonna be at the top
        f.close()
        return func_name

    @property
    def txt_file_name(self):
        return self._txt_file_name

    @txt_file_name.setter
    def txt_file_name(self, file):
        self._txt_file_name = file
