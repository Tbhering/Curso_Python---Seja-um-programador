
import os 
os.add_dll_directory('C:\\Program Files\\VideoLAN\\VLC\\plugins')

import vlc
import time

def get_video_duration(file_path):

    vlc_instance = vlc.Instance()

    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new_path(file_path)
    player.set_media(media)

    player.play()
    time.sleep(0.5)  # Aguarda um pouco para garantir que o player comece a tocar
    duration = player.get_length()
    print(f'Duração: {duration} ms')

get_video_duration('c:\\Users\\thbg1\\anaconda3\\pkgs\\spyder-5.5.1-py312haa95532_0\\Lib\\site-packages\\spyder\\plugins\\help\\utils\\js\\mathjax\\extensions\\a11y\\invalid_keypress.mp3')
