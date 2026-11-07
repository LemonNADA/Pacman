import sys, abc, pyray
from raylib import colors

sys.path.append('./game/modules')
sys.path.append('./game/scenes')
from button import Button, Action
from scene import Scene

class TextureLoader(abc.ABC):
    @abc.abstractmethod
    def load_textures(self) -> None:
        pass
    
    @abc.abstractmethod
    def unload_textures(self) -> None:
        pass


class MenuTextures(TextureLoader):
    def __init__(self):
        self.__pacman_path = "game/assets/images/pacman_image.png"
        self.__pacman_line_path = "game/assets/images/pacman_line.png"
    
    def load_textures(self):
        pacman = pyray.load_image(self.__pacman_path)
        pacman_line_image = pyray.load_image(self.__pacman_line_path)

        self.pacman_texture = pyray.load_texture_from_image(pacman)
        self.pacman_line_texture = pyray.load_texture_from_image(pacman_line_image)

    def unload_textures(self):
        pyray.unload_texture(self.pacman_texture)
        pyray.unload_texture(self.pacman_line_texture)



#------------Buttons---------------

class Start_button(Action):
    """Действие кнопки старта"""

    def execute(self):
        pass


class Exit_button(Action):
    """Действие кнопки выхода"""

    def execute(self):
        pyray.closeWindow()

#----------------------------------

class Menu:
    def __init__(self, textures: MenuTextures):
        self.textures = textures
        self.textures.load_textures()

        buttons_size = [150, 50]
        button_start_position = [pyray.get_screen_width()//2, 225]
        button_exit_position = [pyray.get_screen_width()//2, 325]

        self.button_start = Button("Start", button_start_position, buttons_size, Start_button())
        self.button_exit = Button("Exit", button_exit_position, buttons_size, Exit_button())
    
    def draw(self):
        self.button_start.draw()
        self.button_exit.draw()

        line_pos_x = pyray.get_screen_width() // 2 - self.textures.pacman_line_texture.width // 2
        line_pos_y = pyray.get_screen_height() // 4 - self.textures.pacman_line_texture.height
        pyray.draw_texture(self.textures.pacman_line_texture, line_pos_x, line_pos_y, colors.WHITE)

        pacman_pos_x = pyray.get_screen_width() // 3
        pacman_pos_y = 200
        pyray.draw_texture(
            self.textures.pacman_texture, pacman_pos_x, pacman_pos_y, colors.WHITE
        )


class MenuScene(Scene):
    def __init__(self):
        textures = MenuTextures()
        self.menu = Menu(textures)
    
    def draw(self):
        self.menu.draw()
    

def main() -> None:
    pyray.init_window(800, 600, "Menu")
    menu = MenuScene()

    while not pyray.window_should_close():
        pyray.begin_drawing()
        menu.draw()
        pyray.end_drawing()
    pyray.close_window()
        

if __name__ == "__main__":
    main()