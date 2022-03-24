from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Space Shooter"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "space_shooter/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
GAME_OVER = "space_shooter/assets/sounds/game_over.mp3"
LASER_HIT = "space_shooter/assets/sounds/laser_hit.mp3"
LASER_SHOOT = "space_shooter/assets/sounds/laser_shoot.mp3"
SHIP_CRASH = "space_shooter/assets/soundsship_crash.mp3"
SPACE_MUSIC = "space_shooter/assets/sounds/space_music.mp3"

# SHIP
SHIP_GROUP = "ships"
SHIP_IMAGE = "space_shooter/assets/images/ship.png"
SHIP_WIDTH = 28
SHIP_HEIGHT = 39
SHIP_RATE = 6
SHIP_VELOCITY = 7

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
GREEN = Color(8, 160, 69)
ORANGE = Color(255, 136, 17)
PINK = Color = (219, 48, 105)
# PURPLE = Color(255, 0, 255)
# RED = Color(255, 27, 28)
# SKYBLUE = Color(66, 202, 253)
# TURQUOISE = Color(115, 238, 220)
# YELLOW = Color(255, 177, 0)
# WHITE = Color(255, 255, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# ASTEROID
ASTEROIDS_GROUP = "asteroid"
ASTEROID_IMAGE1 = "space_shooter/assets/images/asteroid1.png"
ASTEROID_IMAGE2 = "space_shooter/assets/images/asteroid2.png"
ASTEROID_IMAGE3 = "space_shooter/assets/images/asteroid3.png"

DEFAULT_ASTEROIDS = 20
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40

ASTEROID_WIDTH = 20
ASTEROID_HEIGHT = 10
ASTEROID_DELAY = 0.5
ASTEROID_RATE = 4
ASTEROID_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"