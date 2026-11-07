import pyray as rl


class SoundManager:
    """
    Класс для звуков
    """
    def __init__(self , game_start_sound , eat_pellet_sound , game_over_sound ):
        """_summary_

        :param game_start_sound: Звук начала игры
        :type game_start_sound: str
        :param eat_pellet_sound: Звук поедания зерна
        :type eat_pellet_sound: str
        :param game_over_sound: Звук проигрыша
        :type game_over_sound: str
        """
        self.game_start_sound = rl.load_sound(game_start_sound) 
        self.eat_pellet_sound = rl.load_sound(eat_pellet_sound)  
        self.game_over_sound = rl.load_sound(game_over_sound) 

    def play_game_start(self):
        """
        Воспроизводит звук запуска игры.
        """

        rl.play_sound(self.game_start_sound)

    def play_eat_pellet(self):
        """
        Воспроизводит звук поедания зерна.
        """
        rl.play_sound(self.eat_pellet_sound)

    def play_game_over(self):
        """
        Воспроизводит звук проигрыша.
        """
        rl.play_sound(self.game_over_sound)

    def set_volume(self, volume):
        """
        Устанавливает громкость для всех звуковых эффектов.

        :param volume: Громкость (от 0.0 до 1.0)
        """
        rl.set_sound_volume(self.game_start_sound, volume)
        rl.set_sound_volume(self.eat_pellet_sound, volume)
        rl.set_sound_volume(self.game_over_sound, volume)


    def unload_sounds(self):
        """
        Выгружает звуковые эффекты из памяти.
        """
        rl.unload_sound(self.game_start_sound)
        rl.unload_sound(self.eat_pellet_sound)
        rl.unload_sound(self.game_over_sound) 

#пример использования класса
def main():
    rl.init_window(500, 500, "TEST")
    rl.init_audio_device()
    # Создаем экземпляр SoundManager один раз
    sound_manager = SoundManager("sounds/start.mp3", "sounds/um.mp3", "sounds/death.mp3")
    sound_manager.set_volume(0.5)

    sound_manager.play_game_start()
    
    while not rl.window_should_close():
        rl.begin_drawing()
        # Вызываем методы правильно:
        rl.end_drawing()

    sound_manager.unload_sounds()
    rl.close_window()

if __name__ == "__main__":
    main()