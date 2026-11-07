import abc

class Scene(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass