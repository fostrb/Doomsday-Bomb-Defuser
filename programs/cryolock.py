from core import Program
import random
import re
import estoBomb
import core
import os

class cryolock(Program):
    def __init__(self, name="cryolock", brief="Bomb Disarmer | System Bricker", programType="Hacking Utilities"):
        super(cryolock, self).__init__(name=name, brief=brief, programType=programType)
        self.alias = ["cryo"]
        self.cryoBanner = """
 ██████╗██████╗ ██╗   ██╗ ██████╗ ██╗      ██████╗  ██████╗██╗  ██╗
██╔════╝██╔══██╗╚██╗ ██╔╝██╔═══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝
██║     ██████╔╝ ╚████╔╝ ██║   ██║██║     ██║   ██║██║     █████╔╝
██║     ██╔══██╗  ╚██╔╝  ██║   ██║██║     ██║   ██║██║     ██╔═██╗
╚██████╗██║  ██║   ██║   ╚██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗
 ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
                                        -SYSTEM BRICKER-
        """

    def runcmd(self, args):
        if args:
            if args[0] == "help":
                print(self.brief)
                print("Stabilizes or Locks the currently hard-wired device.")
        else:
            if estoBomb.crypto_lock1 or estoBomb.crypto_lock2:
                print("ESTO BOMB Cryptographic locks 1 and 2 must be unlocked prior to running this utility.")
                return
            if not estoBomb.armed:
                print("ESTO BOMB is not currently armed.")
                return
            passcode = ''
            while passcode.lower() != "ef45a2":
                passcode = input("PASSCODE:")
                if passcode.lower() != "ef45a2":
                    print(core.pullACard)
                    return

            rows = 10
            columns = 10
            difficulty = .1
            m = Minesweeper(rows, columns, difficulty)

            while True:
                try:
                    os.system("clear")
                    print(self.cryoBanner)
                    m.print_board()
                    first_guess = input('INITIAL:').split(' ')
                    if "!" in first_guess:
                        return
                    if len(first_guess) is not 2:
                        raise ValueError
                    print('')
                    m._first_guess(int(first_guess[0]), int(first_guess[1]))
                    break
                except ValueError:
                    print("INVALID FORMAT")
                except OutOfBoundsError:
                    print('OUT OF BOUNDS')

            while not m.won() and not m.lost():
                os.system("clear")
                print(self.cryoBanner)
                m.print_board()
                print('')
                try:
                    usr_input = input('GUESS: (%s data bombs left): ' %m.mines_left())
                    if "!" in usr_input:
                        return
                    guesses = usr_input.split(';')
                    for guess in guesses:
                        guess = re.sub(r' +', ' ', guess).strip(' ').split(' ')
                        if len(guess) is 2:
                            m.guess(int(guess[-2]), int(guess[-1]))
                        elif len(guess) is 3:
                            func = None
                            if guess[0] == 'g':
                                func = m.guess
                            elif guess[0] == 'f':
                                func = m.flag
                            elif guess[0] == 'u':
                                func = m.unflag
                            elif guess[0] == 's':
                                func = m.guess_surrounding
                            else:
                                raise ValueError
                            xs = guess[-2].lstrip('(').rstrip(')').split(',')
                            ys = guess[-1].lstrip('(').rstrip(')').split(',')

                            apply_ranges(xs)
                            apply_ranges(ys)
                            for x in xs:
                                for y in ys:
                                    func(int(x),int(y))
                        else:
                            raise ValueError
                except ValueError:
                    print('INVALID FORMAT')
                except OutOfBoundsError:
                    print('OUT OF BOUNDS')

            print('')
            os.system("clear")
            print(self.cryoBanner)
            if m.won():
                m.print_board()
                estoBomb.armed = False
                estoBomb.locked = True
                print("BOMB DISARMED")
                print('BOMB CRYOLOCKED')
                print("BOMB STABLE")
            elif m.lost():
                m.corrected_board()
                print(core.pullACard)
            else:
                print('HUH?')




class COLOR:
    END = '\033[0m'
    RED = '\033[0;31m'
    BLACK = '\033[0;30m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;37m'
    BACK_RED = '\033[41m'
    BACK_YELLOW = '\033[43m'
    BACK_BLUE = '\033[44m'

BLOCK = u"\u2588"
FLAG = u"\u2690"
INCORRECT_FLAG = 'i'

COLOR_DICT = {
    0: " ", #COLOR.WHITE + '0' + COLOR.END,
    1: COLOR.BLUE + '1' + COLOR.END,
    2: COLOR.GREEN + '2' + COLOR.END,
    3: COLOR.RED + '3' + COLOR.END,
    4: COLOR.PURPLE + '4' + COLOR.END,
    5: COLOR.YELLOW + '5' + COLOR.END,
    6: COLOR.CYAN + '6' + COLOR.END,
    7: COLOR.CYAN + '7' + COLOR.END,
    8: COLOR.CYAN + '8' + COLOR.END,
    BLOCK: BLOCK,
    FLAG: COLOR.BLACK + COLOR.BACK_YELLOW + FLAG + COLOR.END,
    'x': COLOR.BLACK + COLOR.BACK_RED + 'x' + COLOR.END,
    'i': COLOR.BLACK + COLOR.BACK_BLUE + FLAG + COLOR.END,
    }

class Minesweeper(object):

    def __init__(self, rows, cols, difficulty):
        """Creates a minesweeper board, ensuring that the first guess is a box
        with no surrounding mines.
        """
        self._generate_board(rows, cols, difficulty)
        self.difficulty = difficulty
        self.viewable_board = list(list(BLOCK for x in range(self.cols)) for x in range(self.rows))

    def _first_guess(self, r, c):
        self._validate(r, c)
        while self.values[r][c] is not 0 or self.values == 'x':
            self._generate_board(self.rows, self.cols, self.difficulty)
        self.guess(r,c)

    def _generate_board(self, rows, cols, difficulty):
        """Helper to generate the board and calculate the appropriate values
        for the board.
        """
        self.rows = rows
        self.cols = cols
        self.board = board = list(list(False for x in range(cols)) for y in range(rows))
        self.values = values = list(list(-1 for x in range(cols)) for y in range(rows))

        self.flags_marked = 0
        self.num_mines = int(rows*cols*difficulty)
        if self.num_mines >= rows*cols/2:
            self.num_mines = rows*cols/2

        for x in range(int(self.num_mines)):
            box = self._random_box()
            while board[box[0]][box[1]]:
                box = self._random_box()
            board[box[0]][box[1]] = True

        for r in range(rows):
            for c in range(cols):
                if board[r][c]:
                    self.values[r][c] = 'x'
                else:
                    count = 0
                    if r > 0 and c > 0 and board[r-1][c-1]: count += 1
                    if r > 0 and board[r-1][c]: count += 1
                    if r > 0 and c < cols-1 and board[r-1][c+1]: count += 1
                    if c > 0 and board[r][c-1]: count += 1
                    if c < cols-1 and board[r][c+1]: count += 1
                    if r < rows-1 and c > 0 and board[r+1][c-1]: count += 1
                    if r < rows-1 and board[r+1][c]: count += 1
                    if r < rows-1 and c < cols-1 and board[r+1][c+1]: count += 1
                    self.values[r][c] = count

    def _random_box(self):
        """Select a random box in the grid"""
        return (random.randint(0, self.rows-1), random.randint(0, self.cols-1))

    def _print_board(self, data):
        """Helper method to print the visible board or the full answers"""
        print("OPTIONS:")
        print("f : FLAG")
        print("u : UNFLAG")
        print("s : SWEEP SURROUNDING\n")
        print(" ",end=' ')
        for x in range(self.rows):
            print(x % 10, end=' ')
        print("")

        y = 0
        for row in data:
            print(y % 10, end=' ')
            for item in row:
                print('%s' %COLOR_DICT[item],end=' ')
            print(y % 10)
            y += 1

        print(" ",end=' ')
        for x in range(self.rows):
            print(x % 10,end = ' ')
        print("")

    def print_board(self):
        """Print what has been guessed by the user"""
        self._print_board(self.viewable_board)

    def corrected_board(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if (self.viewable_board[r][c] == FLAG and
                    self.values[r][c] != 'x'):
                    self.viewable_board[r][c] = INCORRECT_FLAG
        self.print_board()

    def _answers(self):
        self._print_board(self.values)

    def consistent(self):
        count = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col]:
                    count += 1
        return (count is self.num_mines, count, self.num_mines)

    def _validate(self, r, c):
        if r >= self.rows or r < 0 or c >= self.cols or c < 0:
            raise OutOfBoundsError

    def guess(self, r, c):
        self._validate(r, c)
        if self.viewable_board[r][c] == FLAG:
            return
        board = self.board
        value = self.values[r][c]
        self.viewable_board[r][c] = value

        if value is 0:
            self.guess_surrounding(r,c)

    def guess_surrounding(self, r, c):
        self._validate(r, c)
        if type(self.viewable_board[r][c]) is not int:
            print ('You may only use the sweep function on boxes you '
                   'have unconvered')
            return
        rows = self.rows
        cols = self.cols
        if (r > 0 and c > 0 and
            self.viewable_board[r-1][c-1] == BLOCK):
            self.viewable_board[r-1][c-1] = self.values[r-1][c-1]
            if self.values[r-1][c-1] is 0:
                self.guess_surrounding(r-1, c-1)
        if (r > 0 and
            self.viewable_board[r-1][c] == BLOCK):
            self.viewable_board[r-1][c] = self.values[r-1][c]
            if self.values[r-1][c] is 0:
                self.guess_surrounding(r-1, c)
        if (r > 0 and c < cols-1 and
            self.viewable_board[r-1][c+1] == BLOCK):
            self.viewable_board[r-1][c+1] = self.values[r-1][c+1]
            if self.values[r-1][c+1] is 0:
                self.guess_surrounding(r-1, c+1)
        if (c > 0 and
            self.viewable_board[r][c-1] == BLOCK):
            self.viewable_board[r][c-1] = self.values[r][c-1]
            if self.values[r][c-1] is 0:
                self.guess_surrounding(r, c-1)
        if (c < cols-1 and
            self.viewable_board[r][c+1] == BLOCK):
            self.viewable_board[r][c+1] = self.values[r][c+1]
            if self.values[r][c+1] is 0:
                self.guess_surrounding(r, c+1)
        if (r < rows-1 and c > 0 and
            self.viewable_board[r+1][c-1] == BLOCK):
            self.viewable_board[r+1][c-1] = self.values[r+1][c-1]
            if self.values[r+1][c-1] is 0:
                self.guess_surrounding(r+1, c-1)
        if (r < rows-1 and
            self.viewable_board[r+1][c] == BLOCK):
            self.viewable_board[r+1][c] = self.values[r+1][c]
            if self.values[r+1][c] is 0:
                self.guess_surrounding(r+1, c)
        if (r < rows-1 and c < cols-1 and
            self.viewable_board[r+1][c+1] == BLOCK):
            self.viewable_board[r+1][c+1] = self.values[r+1][c+1]
            if self.values[r+1][c+1] is 0:
                self.guess_surrounding(r+1, c+1)

    def flag(self, r, c):
        self._validate(r, c)
        if self.viewable_board[r][c] == BLOCK:
            self.viewable_board[r][c] = FLAG
            self.flags_marked += 1
        #self.print_board()

    def unflag(self, r, c):
        self._validate(r, c)
        if self.viewable_board[r][c] == FLAG:
            self.viewable_board[r][c] = BLOCK
            self.flags_marked -= 1

    def won(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if (self.viewable_board[r][c] == BLOCK and
                    self.values[r][c] != 'x'):
                    return False
                elif (self.viewable_board[r][c] == FLAG and
                      self.values[r][c] != 'x'):
                    return False
        return True

    def mines_left(self):
        return self.num_mines - self.flags_marked

    def lost(self):
        for row in self.viewable_board:
            for item in row:
                if item == 'x':
                    return True
        return False

class OutOfBoundsError(Exception):
    def __str__(self):
        return "OUT OF BOUNDS"


def apply_ranges(list):
    more = []
    for item in list:
        if re.match(r'\d*-\d*', item):
            list.remove(item)
            pieces = item.split('-')
            r = None
            if pieces[0] < pieces[1]:
                r = range(int(pieces[0]), int(pieces[1])+1)
            else:
                r = range(int(pieces[1]), int(pieces[0])-1, -1)
            for num in r:
                more.append(str(num))
    list.extend(more)