import csv
from constants import *

from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point

from game.casting.stats import Stats
from game.casting.text import Text 

from game.scripting.draw_hud_action import DrawHudAction

from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.draw_ship_action import DrawShipAction
from game.scripting.move_ship_action import MoveShipAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    DRAW_SHIP_ACTION= DrawShipAction(VIDEO_SERVICE)
    MOVE_SHIP_ACTION = MoveShipAction()



    def __init__(self):
        pass

 
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
