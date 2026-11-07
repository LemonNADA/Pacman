import abc, sys
import pyray as rl
from raylib import colors

sys.path.append('./game/scenes')
sys.path.append('./game/modules')

from scene import Scene

from menu import MenuScene
from game import GameScene

#----------------INTERFACE----------------
class IScenesController(abc.ABC):
    def __init__(self, start_scene: str):
        pass

    @abc.abstractmethod
    def draw() -> None:
        pass

    @abc.abstractmethod
    def change_scene(self, scene: Scene):
        pass

    @abc.abstractmethod
    def status_changed(self) -> bool:
        pass

#------------------------------------------

class ScenesController(IScenesController):
    def __init__(self, start_scene: str):
        self.Scenes = {
            "menu": MenuScene(),
            "game": GameScene()
        }
        self.__current_scene: str = start_scene
        self.__scenes_changed: bool = True

    def change_scene(self, scene_name: str):
        rl.clear_background(colors.BLACK)
        self.__scenes_changed = False
        self.Scenes[scene_name].draw()
    
    def draw(self):
        self.Scenes[self.__current_scene].draw()
    
    def status_changed(self) -> bool:
        return self.__scenes_changed
    
    def get_current_scene(self) -> Scene:
        return self.__current_scene