import re
import requests


class MainProgramm:
    @staticmethod
    def search_in_string(text: str) -> list:
        """
        Поиск адреса электронной почты в строке


        [a-zA-Z0-9._%+-]+ - одна или более букв (включая верхний и нижний регистры), цифр и специальных символов
        (точка, нижнее подчеркивание, процент, плюс и дефис).

        @ - обязательный символ '@' в адресе электронной почты.

        [a-zA-Z0-9.-]+ - одна или более букв и цифр или символов точки и дефиса
        (это соответствует доменному имени, например, example.com).

        \. - символ точки, который разделяет домен и его расширение.

        [a-zA-Z]{2,} - верхний или нижний регистр в доменном расширении (например, com, net), состоящее минимум
        из 2-х букв.
        """
        return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

    def search_in_file(self, path: str) -> list:
        """Функция проверки файла"""
        try:
            with open(path, encoding="utf-8") as file:
                return self.search_in_string(file.read())
        except Exception as error_msg:
            print(f"Ошибка открытия файла: {error_msg}")
            return list()

    def search_in_url(self, url: str) -> list:
        """Функция проверки сайта"""
        try:
            response = requests.get(url)
            response.raise_for_status()
            return self.search_in_string(response.text)
        except Exception as error_msg:
            print(f"Ошибка чтения страницы: {error_msg}")
            return list()

    def main_console(self) -> None:
        """Запуск программы"""
        t = 1
        while t:
            try:
                t = int(input("Что вы хотите проверить?\n1 - строку\n2 - файл\n3 - url\n0 - Выход\n"))
                if t == 1:
                    print(self.search_in_string(str(input("Введите строку: "))))
                elif t == 2:
                    print(self.search_in_file(str(input("Введите путь к файлу: "))))
                elif t == 3:
                    print(self.search_in_url(str(input("Введите url: "))))
            except Exception as error_msg:
                print(error_msg)
                return


if __name__ == "__main__":
    solution = MainProgramm()
    solution.main_console()
