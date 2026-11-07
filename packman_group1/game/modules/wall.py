import pyray as rl

class Walldraw:
    """_summary_
    """
    def __init__(self, wall_map, cell_size, texture_of_wall):
        """_summary_

        :param wall_map: разметка, там где должны быть стены в виде таблицы
        :type wall_map: *args
        :param cell_size: размер единичной стенки
        :type cell_size: int
        :param texture_of_wall: текстура стенки
        :type texture_of_wall: str
        """
        self.wall_map = wall_map
        self.cell_size = cell_size
        self.texture = texture_of_wall
        
        

    def draw(self):
        """
        Рисует стены
        """
        for y, row in enumerate(self.wall_map):
            for x, tile in enumerate(row):
                if tile == 1:
                    pos_x = x * self.cell_size
                    pos_y = y * self.cell_size

                    # Отрисовка стены с текстурой
                    rl.draw_texture_pro(
                        self.texture,
                        rl.Rectangle(0, 0, self.texture.width, self.texture.height),  # Исходный прямоугольник текстуры
                        rl.Rectangle(pos_x, pos_y, self.cell_size, self.cell_size),  # Прямоугольник стены
                        rl.Vector2(0, 0),  # Смещение 
                        0,
                        rl.WHITE  # Цвет отрисовки (белый)
                    )



# Пример реализации класса
def main():
    # Инициализация окна
    rl.init_window(800, 600, "Walls")
    rl.set_target_fps(60)

    # Загрузка текстуры
    texture = rl.load_texture("texture.jpg")

    # Параметры отрисовки
    cell_size = 48  # Размер клетки

    # Пример карты (12x9)
    wall_map = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    # Создаем обеъкт класса Walldraw
    renderer = Walldraw(wall_map, cell_size, texture)

    while not rl.window_should_close():
        rl.begin_drawing()
        rl.clear_background(rl.BLACK)
        renderer.draw()
        rl.end_drawing()

    # Выгрузка текстуры и закрытие окна
    rl.unload_texture(texture)
    rl.close_window()


