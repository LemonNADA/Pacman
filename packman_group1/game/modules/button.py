import pyray
import abc

class PyrayObject(abc.ABC):
    """Абстрактный класс простого объекта в библиотеке pyray"""

    def __init__(self, position: list, size: int | list):
        """Инициализация объекта pyray

        :param position: Позиция объекта
        :type position: list
        :param size: Размер объекта
        :type size: int | list[int, int]
        """
        super().__init__()
        self.position = position
        self.size = size

    @abc.abstractmethod
    def draw(self) -> None:
        """Функция отрисовки объекта"""
        pass

class Action(abc.ABC):
    """Абстрактный класс действия"""

    @abc.abstractmethod
    def execute(self):
        """Функция выполнения действия"""
        pass

class AbstractBaseButton(PyrayObject, abc.ABC):
    """Абстрактный класс базовой реализации Button"""

    def __init__(self, text, position, size, action: Action):
        """Инициализация объекта

        :param text: Текст кнопки
        :type text: str
        :param position: Позиция кнопки (x, y)
        :type position: list
        :param size: Размер кнопки (width, height)
        :type size: int | list[int, int]
        :param action: Событие кнопки
        :type action: Action
        """
        super().__init__(position, size)
        self.text = text
        self.action = action
    
    @abc.abstractmethod
    def press(self):
        """Функция, которая сработает при нажатии кнопки"""
        pass
    
    @abc.abstractmethod
    def draw(self) -> None:
        """Функция отрисовки кнопки в окне"""
        pass


class Button(AbstractBaseButton):
    """Класс кнопки"""

    def __init__(self, text, position, size, action):
        super().__init__(text, position, size, action)
    
    def press(self):
        self.action.execute()
    
    def draw(self) -> None:
        x,y = self.position
        width, height = self.size
        
        if (pyray.gui_button((pyray.Rectangle(int(x) - width // 2, int(y) - height // 2, width, height)), self.text)):
            self.press()