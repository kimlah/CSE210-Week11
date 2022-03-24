""" imports """
from game.casting.actor import Actor

class Asteroid(Actor):
    """An object that inherits from Actor. A Object that holds the methods and varibles in charge of 
    movement, color, messages and values for game play.  

    Attributes:
        Inherited from Actor:
            _text (string): The text to display
            _font_size (int): The font size to use.
            _color (Color): The color of the text.
            _position (Point): The screen coordinates.
            _velocity (Point): The speed and direction.
        Added on Artifact class:
            _message (string): Holds the message that can be displayed to the banner.
            _value (int): The point value of the artifact.

    """

    def __init__(self, body, points, debug = False):
        """Constructs a new Brick.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        # self._animation = animation
        self._points = points
        
    # def get_animation(self):
    #     """Gets the brick's image.
        
    #     Returns:
    #         An instance of Image.
    #     """
    #     return self._animation

    def get_body(self):
        """Gets the brick's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_points(self):
        """Gets the brick's points.
        
        Returns:
            A number representing the brick's points.
        """
        return self._points