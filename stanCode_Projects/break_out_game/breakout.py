"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    death = 0
    graphics = BreakoutGraphics()
    vx = graphics.get_vx()
    vy = graphics.get_vy()
    total_bricks = graphics.brick_rows * graphics.brick_cols
    while True:
        # UPDATE
        if graphics.switch:
            graphics.ball.move(vx, vy)
            # CHECK
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball_width >= graphics.window.width:
                vx *= -1
            if graphics.ball.y <= 0:
                vy *= -1
            elif graphics.ball.y + graphics.ball_width >= graphics.window.height:
                graphics.window.remove(graphics.ball)
                graphics.window.add(graphics.ball, graphics.ball_x, graphics.ball_y)
                graphics.switch = False
                death += 1
                vx = graphics.get_vx()
                vy = graphics.get_vy()
            # after move, check ball whether touch the object
            ball_corner_1_x = graphics.ball.x
            ball_corner_1_y = graphics.ball.y
            ball_corner_2_x = graphics.ball.x + graphics.ball_radius*2
            ball_corner_2_y = graphics.ball.y
            ball_corner_3_x = graphics.ball.x
            ball_corner_3_y = graphics.ball.y + graphics.ball_radius*2
            ball_corner_4_x = graphics.ball.x + graphics.ball_radius*2
            ball_corner_4_y = graphics.ball.y + graphics.ball_radius*2
            maybe_object_1 = graphics.window.get_object_at(ball_corner_1_x, ball_corner_1_y)
            maybe_object_2 = graphics.window.get_object_at(ball_corner_2_x, ball_corner_2_y)
            maybe_object_3 = graphics.window.get_object_at(ball_corner_3_x, ball_corner_3_y)
            maybe_object_4 = graphics.window.get_object_at(ball_corner_4_x, ball_corner_4_y)
            if maybe_object_1 is not None:
                if maybe_object_1 is graphics.paddle:
                    if vy > 0:  # bounce if down
                        vy *= -1
                else:  # bricks only can identify the last one, so put the condition at last
                    graphics.window.remove(maybe_object_1)
                    vy *= -1
                    total_bricks -= 1
                    if total_bricks == 0:
                        break
            elif maybe_object_2 is not None:
                if maybe_object_2 is graphics.paddle:
                    if vy > 0:  # bounce if down
                        vy *= -1
                else:  # bricks only can identify the last one, so put the condition at last
                    graphics.window.remove(maybe_object_2)
                    vy *= -1
                    total_bricks -= 1
                    if total_bricks == 0:
                        break
            elif maybe_object_3 is not None:
                if maybe_object_3 is graphics.paddle:
                    if vy > 0:  # bounce if down
                        vy *= -1
                else:  # bricks only can identify the last one, so put the condition at last
                    graphics.window.remove(maybe_object_3)
                    vy *= -1
                    total_bricks -= 1
                    if total_bricks == 0:
                        break
            elif maybe_object_4 is not None:
                if maybe_object_4 is graphics.paddle:
                    if vy > 0:  # bounce if down
                        vy *= -1
                else:  # bricks only can identify the last one, so put the condition at last
                    graphics.window.remove(maybe_object_4)
                    vy *= -1
                    total_bricks -= 1
                    if total_bricks == 0:
                        break
        # PAUSE
        pause(FRAME_RATE)
        if death == NUM_LIVES:
            break


if __name__ == '__main__':
    main()
