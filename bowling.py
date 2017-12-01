SPARE = '/'
STRIKE = 'x'
GUTTER = '-'


def score(game, result=0, frame=1, in_first_half=True):
    '''
    A scoring algorhythm for a game of bowling.

    Args:
        game: a string of characters with numbers, and
              symbols for spare (/), strike (x), and gutter(-)

    Optional args:
        result: the base score to start with (integer)
        frame: the base frame to start with (integer)
        in_first_half: the base roll to start with (boolean)

    Returns:
        the result of the game, integer
    '''
    for i in range(len(game)):
        current = game[i]
        next_value = get_value(game[(i + 1) % len(game)])
        prev_value = get_value(game[i - 1])

        if current == SPARE:
            result += 10 - prev_value
        else:
            result += get_value(current)

        if frame < 10 and get_value(current) == 10:    # if character is x or /, and not last round
            if current == SPARE:
                result += next_value
            elif current.lower() == STRIKE:
                result += next_value
                if game[i + 2] == SPARE:
                    result += 10 - next_value
                else:
                    result += get_value(game[i + 2])

        if current.lower() == STRIKE:
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
    if char.lower() == STRIKE or char == SPARE:
        return 10
    elif char == GUTTER:
        return 0
    else:
        try:
            return int(char)
        except ValueError:
            pass
    raise ValueError("{} is not a valid score in bowling.".format(char.upper()))
