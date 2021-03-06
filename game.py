#!/usr/local/bin/python3

from random import randint
import os


class PositionAlreadyFullError(Exception):
    def init(self):
        pass


class BadChoiceError(Exception):
    def __init__(self):
        pass


class Player():

    def __init__(self, name='', marker=''):

        self.name = name
        self.marker = marker


board = [' '] * 10


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
    """[Takes in two players of Player class as parameter 
    and assigns marker attritute of each player to either X or O all 
    according to toss result]

    Args:
        p1 ([Player class object])
        p2 ([player class object])

    Raises:
        BadChoiceError: [Raised if the given input does not match the criteria of what the program wants]
    """
    toss_result = toss()    #

    while True:
        try:
            if toss_result == 1:
                marker = input(
                    f'{p1.name}, Please choose from X or O: ').upper()
                if marker not in ['X', 'O']:
                    raise BadChoiceError
            elif toss_result == 2:
                marker = input(
                    f'{p2.name}, Please choose from X or O: ').upper()
                if marker not in ['X', 'O']:
                    raise BadChoiceError
            break
        except BadChoiceError:
            print('Invalid input')

    assign_markers(p1, p2, toss_result, marker)


def update_board(position, marker):
    """[Update the board list index at position parameter with marker]

    Args:
        position ([int]): [position index in the board list]
        marker ([str]): [Either X or O]
    """

    board[position] = marker


def is_pos_empty(position):
    """ [Takes in position on the board and check if it is already filled or not
    and returns True or False]

    Args:
        position ([int]): [position index in the board list]

    Returns:
        [bool]: [return True if position is empty space else False]
    """

    return board[position] == ' '


def is_board_full():
    """[Checks if the board is full or not]
    """

    for position in range(1, 10):
        if is_pos_empty(position):
            return False
    return True


def has_won(marker):
    """[Checking if player with [marker] (either X or O) has won or not]

    Args:
        marker ([str]): [either X or O]

    Returns:
        [bool]: [return True if a player with [marker] has won else False]
    """

    winning_positions_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [
        1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for winning_positions in winning_positions_list:
        if board[winning_positions[0]] == board[winning_positions[1]] == board[winning_positions[2]] == marker:
            return True
    return False


def generate_board():
    """[Generates board for the players to be seen]
    """

    os.system('clear')
    print('     |     |     ')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print('     |     |     ')


# fix it with try except if possible
def replay():
    """[Asks player if they want to play again]

    Returns:
        [bool]
    """
    replay_input = input('Do you want to play again(y or n): ').upper()
    while replay_input not in ['Y', 'N']:
        replay_input = input('Please enter a valid input(y or n): ').upper()

    return replay_input == 'Y'


def player_turn(player):
    """[Updates the board with player's marker]

    Args:
        player ([class Player])

    Raises:
        IndexError: [Raised if the entered position is not in range of 1 to 9 (including 9)]
        PositionAlreadyFullError: [Raised if the entered poisition is already filled with a marker(either X or O)]

    Returns:
        [bool]: [returns True if a player has won or the board is full else False]
    """

    generate_board()
    while True:
        try:
            position = int(input(
                f'{player.name}, Please choose your position(from 1-9): '))
            if position not in range(1, 10):
                raise IndexError
            if not is_pos_empty(position):
                raise PositionAlreadyFullError

        except PositionAlreadyFullError:
            print(
                'The position is already full, Please choose another position')
        except ValueError:
            print('Oops!.. you entered an invalid input')
        except IndexError:
            print('Oops!.. you entered an invalid Position')
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
    """[handles the logic of turns of each player]
    """
    player1 = Player()
    player2 = Player()

    player1.name = input('Player1, Please enter your name: ')
    player2.name = input('Player2, Please enter your name: ')

    pick_marker(player1, player2)

    toss_result = toss()

    # boolean flag which is set to true when player1 makes its turn and set to false when player2 makes its turn
    player1_go = False

    if toss_result == 1:
        player_turn(player1)
        player1_go = not player1_go
    else:
        player_turn(player2)

    while True:
        if player1_go:
            if player_turn(player2):
                break
            player1_go = not player1_go
        else:
            if player_turn(player1):
                break
            player1_go = not player1_go


def main():

    play()

    while replay():
        global board
        board = [' '] * 10
        play()


if __name__ == "__main__":
    os.system('clear')
    main()
