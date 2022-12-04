#!/usr/bin/env python3

def read_file(file_path):
    result = []
    with open(file_path, "r") as f:
        for line in f:
            result.append(line.replace('\n',''))
    return result


def lookup_win(them):
    return lookup_result(then, 'win')

def lookup_draw(them):
    return lookup_result(them, 'draw')

def lookup_lose(them):
    return lookup_result(them, 'lose')

def lookup_result(them, expected):
    me = ''
    if expected == 'win':
        if them == 'A':
            me = 'Y'
        elif them == 'B':
            me = 'Z'
        else:
            me = 'X'

    elif expected == 'draw':
        if them == 'A':
            me = 'X'
        elif them == 'B':
            me = 'Y'
        else:
            me = 'Z'
    else:
        if them =='A':
            me ='Z'
        elif them =='B':
            me = 'X'
        else:
            me = 'Y'
    print(me)
    return me

def calc_outcome(them, me):
    
    win=''
    lose=''
    draw=''
    points = 0

    if (them == 'A'):
        win = 'Y'
        draw = 'X'
        lose = 'Z'
    elif(them == 'B'):
        win = 'Z'
        draw = 'Y'
        lose = 'X'
    else:
        win = 'X'
        draw = 'Z'
        lose = 'Y'

    if me == win:
       points = 6
    elif me == draw:
        points = 3
    else:
        points = 0

    return points


    # their choice
    #what would win
    # what would draw
    # what would lose

def calc_gamed_outcome(them, result):
    points = 0
    
    win = 'Z'
    draw = 'Y'
    lose = 'X'

    if result == win:
        points = calc_outcome(them, lookup_win(them))
    if result == draw:
        points = calc_outcome(them, lookup_draw(them))
    else:
        points = calc_outcome(them, lookup_lose(them))

    

    return points


def calc_result(game):
    # if i pick rock 1 , paper i get 2 , scissors i get 3 
    # if i win add 6 , if i draw add 3 if lose add none 
    # game[2] == my turn
    # game[0] == their turn 
    points = 0

    their_turn = game[0]
    desired_result = game[2]


    points = points + calc_gamed_outcome(their_turn, desired_result)
    return points




def main():
    running_score = 0
    results = read_file('test')
    for game in results:
        running_score = running_score + calc_result(game)
        print(calc_result(game))

    print(f"The total score is {running_score}")

if __name__ == "__main__":
    main()
