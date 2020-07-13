#!/usr/local/bin/python3

from random import randint
import os


class Player():

    def __init__(self, name='', marker=''):

        self.name = name
        self.marker = marker


board_list = [' '] * 10


def toss():
    return randint(1, 2)


def assign_markers(p1, p2, toss_result, marker):
    if toss_result == 1:
        p1.marker = marker
        p2.marker = ({'X', 'O'} - set(marker)).pop()

    else:
        p2.marker = marker
        p1.marker = ({'X', 'O'} - set(marker)).pop()


def pick_marker(p1, p2):
    """ [Takes in two players of Player class as parameter
    and assigns marker attritute of each player to either X or O all according to toss result]
    """

    toss_result = toss()

    if toss_result == 1:
        marker = input(f'{p1.name}, Please choose from X or O: ').upper()
    else:
        marker = input(f'{p2.name}, Please choose from X or O: ').upper()

    while marker not in ['O', 'X']:
        marker = input('Please give valid input(either X or O): ').upper()

    assign_markers(p1, p2, toss_result, marker)


def update_board(position, marker):
    """[Update the board list index at position parameter with marker]

    Args:
        position ([int]): [position index in the board list]
        marker ([str]): [Either X or O]
    """

    board_list[position] = marker


def is_pos_empty(position):
    """ [Takes in position on the board and check if it is already filled or not
    and returns True or False]

    Args:
        position ([int]): [position index in the board list]

    Returns:
        [bool]
    """

    return board_list[position] == ' '


def is_board_full():
    """[Checks if the board is full or not]
    """

    for position in range(1, 10):
        if is_pos_empty(position):
            return False
    else:
        return True


def has_won(marker):
    """[Checking if player with marker (either X or O) has won or not]

    Args:
        marker ([str]): [either X or O]

    Returns:
        [bool] or [None]
    """

    match_pos_list = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    
    for match in match_pos_list:
        if board_list[match[0]] == board_list[match[1]] == board_list[match[2]] == marker:
            return True
    return False


def generate_board():
    os.system('clear')
    print('     |     |     ')
    print(f'  {board_list[1]}  |  {board_list[2]}  |  {board_list[3]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {board_list[4]}  |  {board_list[5]}  |  {board_list[6]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {board_list[7]}  |  {board_list[8]}  |  {board_list[9]}  ')
    print('     |     |     ')


def replay():
    replay_input = input('Do you want to play again(y or n): ').upper()
    while replay_input not in ['Y', 'N']:
        replay_input = input('Please enter a valid input(y or n): ').upper()

    return replay_input == 'Y'


def player_turn(player):
    """
        Args:
            player ([class Player])

        Returns:
            [bool]
    """

    generate_board()
    while True:
        try:
            position = int(input(
                f'{player.name}, Please choose your position(from 1-9): '))
            while position not in range(1, 10) or not is_pos_empty(position):
                position = int(input(
                    f'{player.name}, Selected position is already full or is an invalid position, please choose another: '))

        except ValueError:
            print('Oops!.. you entered an invalid input')
        except Exception:
            print("Something went wrong")
        else:
            update_board(position, player.marker)
            break

    if has_won(player.marker):
        generate_board()
        print(f'Congratulations! {player.name} has won')
        return True

    if is_board_full():
        generate_board()
        print('The match was a tie')
        return True
    
    return False


def play():

    player1 = Player()
    player2 = Player()

    player1.name = input('Player1, Please enter your name: ')
    player2.name = input('Player2, Please enter your name: ')

    pick_marker(player1, player2)

    toss_result = toss()

    player1_go = False

    if toss_result == 1:
        player_turn(player1)
        player1_go = True
    else:
        player_turn(player2)
        player1_go = False

    while True:
        if player1_go:
            if player_turn(player2):
                break
            player1_go = False
        else:
            if player_turn(player1):
                break
            player1_go = True


def main():

    play()

    while replay():
        global board_list
        board_list = [' '] * 10
        play()


if __name__ == "__main__":
    os.system('clear')
    main()
