import sys
import pyray as rl

sys.path.append('./game/modules')
sys.path.append('./game/scenes')
sys.path.append('./game/controller')

from audio import SoundManager
from ScenesController import ScenesController

#---------------------------------------

def main():

    # Инициализация окна
    window_width = 800
    window_height = 600

    rl.init_window(window_width, window_height, 'Hello, raylib')
    rl.init_audio_device()
    scenes = ScenesController('menu')
    audio_contoller = SoundManager("game/assets/sounds/start.mp3", "game/assets/sounds/um.mp3", "game/assets/sounds/death.mp3")

    audio_contoller.set_volume(0.5)
    rl.set_exit_key(rl.KeyboardKey.KEY_F8)
    rl.set_target_fps(120)

    while not rl.window_should_close():
        rl.begin_drawing() #START

        if scenes.status_changed():
            scenes.change_scene(scenes.get_current_scene())
        
        if rl.is_key_pressed(rl.KeyboardKey.KEY_SPACE):
            scenes.change_scene("game")
            audio_contoller.play_game_start()

        scenes.draw()
        rl.end_drawing() #END

    audio_contoller.unload_sounds()
    
    rl.close_audio_device()
    rl.close_window()



if __name__ == '__main__':
    main()