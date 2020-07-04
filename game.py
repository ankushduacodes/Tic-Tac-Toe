#!/usr/local/bin/python3

from random import randint
import os


class Player():

    def __init__(self, name='', marker=''):

        self.name = name
        self.marker = marker


board_list = [' '] * 10


def toss():
    return randint(1, 3)


def pick_marker(p1, p2):
    """ [Takes in two players of Player class as parameter
    and assigns marker attritute of each player to either X or O]
    """

    marker = input(f'{p1.name}, Please choose from X or O: ').upper()

    while marker not in ['O', 'X']:
        marker = input('Please give valid input(either X or O): ').upper()

    if marker == 'O':
        p1.marker = marker
        p2.marker = 'X'
    else:
        p1.marker = marker
        p2.marker = 'O'

    # p1.marker = marker
    # p2.marker = ({'X', 'O'} - set(marker)).pop()


def update_board(position, marker):
    """[Update the board list index at position parameter with marker]

    Args:
        position ([int]): [position index in the board list]
        marker ([str])
    """

    board_list[position] = marker


def is_pos_empty(position):
    """ [Takes in position on the board and check if it is already filled or not
    and returns True or False]
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
        [bool]
    """

    return (
        # first row
        board_list[1] == board_list[2] == board_list[3] == marker or
        # second row
        board_list[4] == board_list[5] == board_list[6] == marker or
        # third row
        board_list[7] == board_list[8] == board_list[9] == marker or
        # first column
        board_list[1] == board_list[4] == board_list[7] == marker or
        # second column
        board_list[2] == board_list[5] == board_list[8] == marker or
        # third column
        board_list[3] == board_list[6] == board_list[9] == marker or
        # first diagonal
        board_list[1] == board_list[5] == board_list[9] == marker or
        # second diagonal
        board_list[3] == board_list[5] == board_list[7] == marker
    )


def generate_board():
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


def play():

    player1 = Player()
    player2 = Player()

    player1.name = input('Player1, Please enter your name: ')
    player2.name = input('Player2, Please enter your name: ')

    pick_marker(player1, player2)

    while True:
        os.system('clear')
        generate_board()
        position = int(input(
            f'{player1.name}, Please choose your position(from 1-9): '))
        while position not in range(1, 10) or not is_pos_empty(position):
            position = int(input(
                f'{player1.name}, Selected position is already full or is an invalid position, please choose another: '))

        update_board(position, player1.marker)

        if has_won(player1.marker):
            os.system('clear')
            generate_board()
            print(f'Congratulations! {player1.name} has won')
            return

        if is_board_full():
            generate_board()
            print('The match was a tie')
            return

        os.system('clear')
        generate_board()
        position = int(input(
            f'{player2.name}, Please choose your position(from 1-9): '))
        while position not in range(1, 10) or not is_pos_empty(position):
            position = int(input(
                f'{player2.name}, Selected position is already full or is an invalid position, please choose another: '))

        update_board(position, player2.marker)

        if has_won(player2.marker):
            generate_board()
            print(f'Congratulations! {player2.name} has won!...')
            return

        if is_board_full():
            generate_board()
            print('The match was a tie')
            return



def main():

    play()

    if replay():
        global board_list
        board_list = [' '] * 10
        play()


if __name__ == "__main__":
    os.system('clear')
    main()
