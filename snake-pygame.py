import random
import pygame

pygame

def snake_random_food():
    x_position = 10*random.random()
    y_position = 10*random.random()
    return(x_position, y_position)


def snake_movements():
    key = 0
    while key != ord('q'):
        x, y = 0, 0
        key = input()
        if key == curses.KEY_RIGHT:
            (dx, dy) = ([1, 0])
            x += dx
            y += dy

        elif key == curses.KEY_LEFT:
            (dx, dy) = ([-1, 0])
            x += dx
            y += dy

        elif key == curses.KEY_UP:
            (dx, dy) = ([0, 1])
            x += dx
            y += dy

        elif key == curses.KEY_DOWN:
            (dx, dy) = ([0, -1])
            x += dx
            y += dy

        else:
            pass

    return (x, y)


print(snake_movements())
