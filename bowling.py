SPARE = '/'
STRIKE = 'x'
GUTTER = '-'


def score(game, result=0, frame=1, in_first_half=True, frame_length=10):
    '''
    A scoring algorhythm for a game of bowling.
    The maximum lenght can be changed,
    but it doesn't matter if it's shorter.

    Args:\n
        game: a string of characters with numbers, and
              symbols for spare (/), strike (x), and gutter(-)

    Optional args:\n
        result: the base score to start with\t
        frame: the base frame to start with\t
        in_first_half: the base roll to start with\t
        frame_length: the number of frames\t

    Returns:\n
        the result of the game, integer
    '''
    for i in range(len(game)):
        current = game[i].lower()
        prev_value = get_value(game[i - 1])
        next_value = get_value(game[(i + 1) % len(game)])
        after_next = game[(i + 2) % len(game)]

        if current == SPARE:
            result += 10 - prev_value
        else:
            result += get_value(current)

        if frame < frame_length and get_value(current) == 10:
            if current == SPARE:
                result += next_value
            elif current == STRIKE:
                result += next_value
                if after_next == SPARE:
                    result += 10 - next_value
                else:
                    result += get_value(after_next)

        if current == STRIKE:
            in_first_half = True
            frame += 1
        elif in_first_half:
            in_first_half = False
        else:
            frame += 1
            in_first_half = True

    return result


def get_value(char):
    '''
    Converts the symbols in bowling to appropriate values from 1-10.

    Args:
        single character string to convert

    Returns:
        integer from 0-10
    '''
    char = char.lower()
    if char == STRIKE or char == SPARE:
        return 10
    elif char == GUTTER:
        return 0
    else:
        try:
            return int(char)
        except ValueError:
            pass
    raise ValueError("{} is not a valid score in bowling.".format(char.upper()))
