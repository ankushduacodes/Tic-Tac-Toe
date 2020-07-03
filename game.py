from random import randint


class Player():

    def __init__(self, name='', marker=''):

        self.name = name
        self.marker = marker


board_list = ['X'] * 10


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
    """[Checking if player with marker (Either X or O) has won or not]

    Args:
        marker ([str]): [E ither X or O]

    Returns:
        [bool]
    """

    return (board_list[1] == board_list[2] == board_list[3] or  # first row
            board_list[4] == board_list[5] == board_list[6] or  # second row
            board_list[7] == board_list[8] == board_list[9] or  # third row
            board_list[1] == board_list[4] == board_list[7] or  # first column
            board_list[2] == board_list[5] == board_list[8] or  # second column
            board_list[3] == board_list[6] == board_list[9] or  # third column
            # first diagonal
            board_list[1] == board_list[5] == board_list[9] or
            # second diagonal
            board_list[3] == board_list[5] == board_list[7]
            == marker
            )


def board_update():
    print('     |     |     ')
    print(f'  {board_list[1]}  |  {board_list[2]}  |  {board_list[3]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {board_list[4]}  |  {board_list[5]}  |  {board_list[6]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {board_list[7]}  |  {board_list[8]}  |  {board_list[9]}  ')
    print('     |     |     ')


def main():

    player1 = Player()
    player2 = Player()

    player1.name = input('Player1, Please enter your name: ')
    player2.name = input('Player2, Please enter your name: ')

    pick_marker(player1, player2)


if __name__ == "__main__":
    main()
