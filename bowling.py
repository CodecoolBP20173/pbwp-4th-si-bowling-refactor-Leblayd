SPARE = '/'
STRIKE = 'x'
GUTTER = '-'


def score(game, result=0, frame=1, in_first_half=True):
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - get_value(game[i - 1])
        else:
            result += get_value(game[i])

        if frame < 10 and get_value(game[i]) == 10:    # if character is x or /, and not last round
            if game[i] == '/':
                result += get_value(game[i + 1])
            elif game[i].lower() == 'x':
                result += get_value(game[i + 1])
                if game[i + 2] == '/':
                    result += 10 - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])

        if game[i].lower() == 'x':
            in_first_half = True
            frame += 1
        elif in_first_half:
            in_first_half = False
        else:
            frame += 1
            in_first_half = True

    return result


def get_value(char):
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
