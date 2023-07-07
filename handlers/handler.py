# импортируем библиотеку abc для реализации абстрактных классов
from abc import ABCMeta, abstractmethod
# импортируем разметку клавиатуры и клавиш
from markup.markup import Keyboards
# импортируем класс-менеджер для работы с библиотекой
from data_base.dbalchemy import DBManager


class Handler(metaclass=ABCMeta):

    def __init__(self, bot):
        # получаем объект бота
        self.bot = bot
        # инициализируем разметку кнопок
        self.keybords = Keyboards()
        # инициализируем менеджер для работы с БД
        self.BD = DBManager()

    @abstractmethod
    def handle(self):
        pass
