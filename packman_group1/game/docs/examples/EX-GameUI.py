import pyray

class GameUI:
    def __init__(self, font_size=20, font_color=pyray.WHITE) -> None:
        """Конструктор для применения нужных параметров текста

        :param font_size: Размер текста
        :type font_size: int
        :param font_color: Цвет текста
        :type font_color: pyray.ЦВЕТ
        """
        self.font_size = font_size
        self.font_color = font_color
    
    def draw_text(self, text, position):
        """Вывод какого-либо текста

        :param text: Текст для отображения
        :type text: str
        :param position: Позиция текста (x, y)
        :type position: list[int]
        """
        pyray.draw_text(text, position[0], position[1], self.font_size, self.font_color)
    
    def update_score(self, score, position):
        """Оображение количества очков

        :param score: Количество очков
        :type score: int
        :param position: Позиция текста очков (x, y)
        :type position: list[int]
        """
        score_text = f"Score: {score}"
        self.draw_text(score_text, position)
    
    def update_lives(self, lives, position):
        """Отображение количества жизней

        :param lives: Количество жизней
        :type lives: int
        :param position: Позиция текста жизней (x, y)
        :type position: list[int]
        """
        lives_text = f"Lives: {lives}"
        self.draw_text(lives_text, position)

def main() -> None:
    pyray.init_window(800, 600, "Game UI Example")
    pyray.set_target_fps(60)

    ui = GameUI(font_size=30, font_color=pyray.YELLOW)

    score = 0
    lives = 3

    while not pyray.window_should_close():
        score += 1
        if score % 100 == 0:
            lives -= 1
        
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        
        ui.update_score(score, [20, 20])
        ui.update_lives(lives, [20, 60])
        
        pyray.end_drawing()
    
    pyray.close_window()

if __name__ == "__main__":
    main()
