import random
import curses
import time

screen = curses.initscr()
h, w = screen.getmaxyx()
win = curses.newwin(h, w)
win.keypad(1)
curses.curs_set(0)

snake_head = [10, 15]
snake_corpse = [[15, 10], [14, 10], [13, 10]]
food_position = [20, 20]
score = 0

win.addch(food_position[0], food_position[1], curses.ACS_DIAMOND)

prev_button_direction = 1
button_direction = 1
key = curses.KEY_RIGHT


def new_food(score):
    food_position = [random.randint(1, h - 2), random.randint(1, w - 2)]
    score += 1
    return score, food_position


def snake_collision_borders(snake_head):
    condition_1 = snake_head[0] >= (h - 1)
    condition_2 = snake_head[0] <= 0
    condition_3 = snake_head[1] >= (w - 1)
    condition_4 = snake_head[1] <= 0
    if condition_1 or condition_2 or condition_3 or condition_4:
        return 1
    else:
        return 0


def snake_collision_itself(snake_corpse):
    snake_head = snake_corpse[0]
    if snake_head in snake_corpse[1:]:
        return 1
    else:
        return 0


a = []
while True:
    win.border(0)
    win.timeout(100)

    next_key = win.getch()
    if next_key == -1:
        key = key
    else:
        key = next_key

    # 0 = LEFT, 1 = RIGHT, 3 = UP, 2 = DOWN
    if key == curses.KEY_LEFT and prev_button_direction != 1:
        button_direction = 0
    elif key == curses.KEY_RIGHT and prev_button_direction != 0:
        button_direction = 1
    elif key == curses.KEY_UP and prev_button_direction != 2:
        button_direction = 3
    elif key == curses.KEY_DOWN and prev_button_direction != 2:
        button_direction = 2
    elif key == 'q':
        break
    else:
        pass

    prev_button_direction = button_direction

    if button_direction == 1:
        snake_head[1] += 1
    elif button_direction == 0:
        snake_head[1] -= 1
    elif button_direction == 2:
        snake_head[0] += 1
    elif button_direction == 3:
        snake_head[0] -= 1

    if snake_head == food_position:
        score, food_position = new_food(score)
        snake_corpse.insert(0, list(snake_head))
        a.append(food_position)
        win.addch(food_position[0], food_position[1], curses.ACS_DIAMOND)

    else:
        snake_corpse.insert(0, list(snake_head))
        last = snake_corpse.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake_corpse[0][0], snake_corpse[0][1], '#')

    if snake_collision_borders(snake_head) == 1 or snake_collision_itself(snake_corpse) == 1:
        break

screen.addstr(10, 30, 'Your Score is:  '+str(score))
screen.refresh()
time.sleep(2)
curses.endwin()
print(a)
print(w, h)
