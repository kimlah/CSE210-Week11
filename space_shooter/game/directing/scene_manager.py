import random
import csv
from constants import *

from game.casting.point import Point
from game.casting.body import Body
from game.casting.asteroid import Asteroid
from game.casting.image import Image
from game.casting.label import Label

from game.casting.stats import Stats
from game.casting.text import Text 

from game.scripting.draw_hud_action import DrawHudAction

from game.scripting.play_sound_action import PlaySoundAction

from game.scripting.unload_assets_action import UnloadAssetsAction
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

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
 
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        # self._add_level(cast)
        # self._add_lives(cast)
        # self._add_score(cast)
        # self._add_ball(cast)
        self._add_asteroids(cast)
        # self._add_racket(cast)
        # self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        # # script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        # self._add_output_script(script)
        # self._add_unload_script(script)
        # self._add_release_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _add_asteroids(self, cast):
        cast.clear_actors(ASTEROIDS_GROUP)
        # stats = cast.get_first_actor(STATS_GROUP)
        # level = stats.get_level() % BASE_LEVELS
        for n in range(DEFAULT_ASTEROIDS):

            # message = random.choice([ASTEROID_IMAGE1, ASTEROID_IMAGE2, ASTEROID_IMAGE3])
            x = random.randint(1, FIELD_RIGHT - 1)
            y = random.randint(1, FIELD_BOTTOM - 1)
            # position = Point(x, y)
            # position = position.scale(CELL_SIZE)

            # x = FIELD_LEFT + c * ASTEROID_WIDTH
            # y = FIELD_TOP + r * ASTEROID_HEIGHT
            # color = column[0]
            # frames = int(column[1])
            points = ASTEROID_POINTS 
            
            # if frames == 1:
            #     points *= 2
            
            position = Point(x, y)
            size = Point(ASTEROID_WIDTH, ASTEROID_HEIGHT)
            velocity = Point(0, 0)
            images = random.choice([ASTEROID_IMAGE1, ASTEROID_IMAGE2, ASTEROID_IMAGE3])
            print(position, size, velocity)
            body = Body(position, size, velocity)
            image = Image(images)

            asteroid = Asteroid(body, points) # the parameter images that I removed used to be animation !!!!!!
            cast.add_actor(ASTEROIDS_GROUP, asteroid)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    
    # def _add_initialize_script(self, script):
    #     script.clear_actions(INITIALIZE)
    #     script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    # def _add_load_script(self, script):
    #     script.clear_actions(LOAD)
    #     script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    # def _add_output_script(self, script):
    #     script.clear_actions(OUTPUT)
    #     script.add_action(OUTPUT, self.START_DRAWING_ACTION)
    #     script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
    #     script.add_action(OUTPUT, self.DRAW_BALL_ACTION)
    #     script.add_action(OUTPUT, self.DRAW_BRICKS_ACTION)
    #     script.add_action(OUTPUT, self.DRAW_RACKET_ACTION)
    #     script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
    #     script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    # def _add_release_script(self, script):
    #     script.clear_actions(RELEASE)
    #     script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    # def _add_unload_script(self, script):
    #     script.clear_actions(UNLOAD)
    #     script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    # def _add_update_script(self, script):
    #     script.clear_actions(UPDATE)
    #     script.add_action(UPDATE, self.MOVE_BALL_ACTION)
    #     script.add_action(UPDATE, self.MOVE_RACKET_ACTION)
    #     script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
    #     script.add_action(UPDATE, self.COLLIDE_BRICKS_ACTION)
    #     script.add_action(UPDATE, self.COLLIDE_RACKET_ACTION)
    #     script.add_action(UPDATE, self.MOVE_RACKET_ACTION)
    #     script.add_action(UPDATE, self.CHECK_OVER_ACTION)