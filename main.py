import re


class MainProgramm:
    @staticmethod
    def search_in_string(text):
        return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
