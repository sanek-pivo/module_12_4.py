import logging # импортируем библиотеку
import rt_with_exceptions as runner_ # скачиваем исходный код и импортируем из него runner
from unittest import TestCase #  импортируем класс TestCase из модуля unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='UTF-8', format='%(levelname)s , %(message)s')
# Начинаем настройку логирования через basicConfig, в ней указываем ошибку, извлечения имени файла, запись, кодировку

class RunnerTest(TestCase): # создаем класс наследованный от TestCase

    def test_walk(self):
        try: # делаем блок для ошибки
            runner = runner_.Runner('Вася', -10)
            for i in range(10):  # перебираем циклом этого объекта 10 раз
                runner.walk()  # вызываем метод walk у этого объекта 10 раз
            self.assertEqual(runner.distance, 50) # методом assertEqual сравнивается значение
            logging.info(f'"test_walk" выполнен успешно')
        except: # создаем блок ошибки предупреждения
            logging.warning(f'Неверная скорость для Runner')  # выводим информацию в лог

    def test_run(self):
        try: # делаем блок для ошибки
            runner = runner_.Runner(1, 2)
            for i in range(10):  # перебираем циклом этого объекта 10 раз
                runner.run() # вызываем метод run у этого объекта 10 раз
            self.assertEqual(runner.distance, 100)  # методом assertEqual сравнивается значение
            logging.info(f'"test_run" выполнен успешно')
        except: # создаем блок ошибки предупреждения
            logging.warning(f'Неверный тип данных для объекта Runner') # выводим информацию в лог


RunnerTest()