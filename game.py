from random import randint


class Player():

    def __init__(self, name='', marker=''):

        self.name = name
        self.marker = marker


def toss():
    return randint(1, 3)


def pick_marker(p1, p2):
    """ Takes in two players of Player class and assigns
    marker attritute of each player to either X or O
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


board_list = [' '] * 10


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
    board_update()


if __name__ == "__main__":
    main()
