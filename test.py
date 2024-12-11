import unittest
from main import MainProgramm


class TestCheckAll(unittest.TestCase):

    def setUp(self):
        """Setup данных"""
        self.program = MainProgramm()
        self.correct_values = ["egor.kaduba@mail.ru", "kadubaegor05@gmail.com", "kadubaegor@yandex.com"]
        self.incorrect_values = ["egor.kaduba@", "kadubaegor05", ""]

    def test_search_in_string(self):
        """Тест функции проверки строки на валидных данных"""
        self.assertEqual(self.program.search_in_string(" ".join(self.correct_values)),
                         ["egor.kaduba@mail.ru", "kadubaegor05@gmail.com", "kadubaegor@yandex.com"])

    def test_search_in_string2(self):
        """Тест функции проверки строки на не валидных данных"""
        self.assertEqual(self.program.search_in_string(" ".join(self.incorrect_values)), [])

    def test_search_in_file(self):
        """Тест функции проверки строки на тестовом файле"""
        self.assertEqual(self.program.search_in_file("test.txt"),
                         ["egor.kaduba@mail.ru", "kadubaegor05@gmail.com", "egorkaduba@yandex.com"])

    def test_search_in_url(self):
        """Тест функции проверки сайта на тестовом html-коде"""
        example_url = "https://otvet.mail.ru/question/40591335"
        self.assertEqual(self.program.search_in_url(example_url),
                         ['nikita@mail.ru', 'nnatali-puh@mail.ru', 'sofiya-puhc@mail.ru', 'garri.topor@mail.ru',
                          'dadw@mail.ru', 'dawdaw@yandex.ru', 'dwdaw@gmail.ru', 'dawdaw@yahoo.com',
                          'oceandv2010@inbox.ru', 'AlexSuper@mail.ru', 'Miss@mail.ru', '12345@mail.ru',
                          'Polina_537@mail.ru', 'nikita@mail.ru', 'gylunin@mail.ru', 'soglaev2001@mail.ru',
                          'soglaev2001@mail.ru', 'nikita@mail.ru', 'nnatali-puh@mail.ru', 'sofiya-puhc@mail.ru',
                          'garri.topor@mail.ru', 'dadw@mail.ru', 'dawdaw@yandex.ru', 'dwdaw@gmail.ru',
                          'dawdaw@yahoo.com', 'oceandv2010@inbox.ru', 'AlexSuper@mail.ru', 'Miss@mail.ru',
                          '12345@mail.ru', 'Polina_537@mail.ru', 'nikita@mail.ru', 'gylunin@mail.ru',
                          'soglaev2001@mail.ru', 'soglaev2001@mail.ru', 'soglaev2001@mail.ru', 'nikita@mail.ru',
                          'natali-puh@mail.ru', 'sofiya-puhc@mail.ru', 'garri.topor@mail.ru', 'dadw@mail.ru',
                          'dawdaw@yandex.ru', 'dwdaw@gmail.ru', 'dawdaw@yahoo.com', 'oceandv2010@inbox.ru',
                          'AlexSuper@mail.ru', 'Miss@mail.ru', '12345@mail.ru', 'Polina_537@mail.ru', 'nikita@mail.ru',
                          'gylunin@mail.ru', 'Rating@Mail.ru', 'Rating@Mail.ru'])


if __name__ == "__main__":
    unittest.main()
