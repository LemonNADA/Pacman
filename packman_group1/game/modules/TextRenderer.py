import pyray as rl

class TextRenderer:
    def __init__(self):
        self.color = rl.WHITE  # Цвет текста по умолчанию

    def set_color(self, color):
        self.color = color

    def render(self, text, position):
        rl.draw_text(text, int(position.x), int(position.y), 20, self.color)


# Пример

# def main():
#     rl.init_window(450, 600, "Text Renderer Example")
#     rl.set_target_fps(60)

#     text_renderer = TextRenderer()

#     while not rl.window_should_close():
#         rl.begin_drawing()
#         rl.clear_background(rl.BLACK)

#         text_renderer.render("Hello, World!", rl.Vector2(100, 100))  # Вывод текста

#         rl.end_drawing()

#     rl.close_window()

# if __name__ == "__main__":
#     main()