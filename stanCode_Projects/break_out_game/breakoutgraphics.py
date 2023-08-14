"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle (milestone1)
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        paddle_x = (self.window.width - self.paddle.width)/2  # set paddle's center at the window's horizontal center
        self.paddle_y = (self.window.height - paddle_offset - self.paddle.height)  # paddle's offset has the special distance, this used by reset_paddle_position
        self.paddle.filled = True
        self.window.add(self.paddle, x=paddle_x, y=self.paddle_y)

        # Center a filled ball in the graphical window (milestone1)
        self.ball_radius = ball_radius
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball_width = 2 * ball_radius
        self.ball_x = self.window.width/2 - ball_radius  # set ball's center at the window's horizontal center
        self.ball_y = self.window.height/2 - ball_radius  # set ball's center at the window's vertical center
        self.ball.filled = True
        self.window.add(self.ball, x=self.ball_x, y=self.ball_y)

        # Default initial velocity for the ball (milestone1 skip) (milestone2)
        self.__dx = 0
        self.__dy = 0
        self.switch = False  # set the switch is close (milestone2)
        # Initialize our mouse listeners (milestone1 write the name without functions)
        onmousemoved(self.reset_paddle_position)  # (milestone2)
        onmouseclicked(self.ball_start)  # (milestone2)

        # Draw bricks (milestone1)
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.bricks = GRect(width=brick_width, height=brick_height)
                bricks_x = i * (brick_spacing + brick_width)
                bricks_y = brick_offset + j * (brick_spacing + brick_height)
                self.bricks.filled = True
                self.bricks_color = random.randint(1, 5)  # set colorful bricks in random
                if j >= 8:
                    self.bricks.fill_color = 'blue'
                elif j >= 6:
                    self.bricks.fill_color = 'green'
                elif j >= 4:
                    self.bricks.fill_color = 'yellow'
                elif j >= 2:
                    self.bricks.fill_color = 'orange'
                elif j >= 0:
                    self.bricks.fill_color = 'red'

                self.window.add(self.bricks, x=bricks_x, y=bricks_y)

    def reset_paddle_position(self, mouse):
        if self.paddle.width/2 < mouse.x < self.window.width - self.paddle.width/2:
            self.paddle.x = mouse.x - self.paddle.width / 2
        elif mouse.x < self.paddle.width/2:
            self.paddle.x = 0
        else:
            self.paddle.x = self.window.width - self.paddle.width

    def ball_start(self, _):  # mouse isn't used in this function, so replace the mouse to _
        # if the ball at original place, set the switch is open
        if self.ball_x == self.window.width/2 - self.ball_radius and self.ball_y == self.window.height/2 - self.ball_radius:
            self.switch = True

    def get_vx(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:  # when ball start choose the left/right
            self.__dx = -self.__dx
        return self.__dx

    def get_vy(self):
        self.__dy = INITIAL_Y_SPEED
        return self.__dy
