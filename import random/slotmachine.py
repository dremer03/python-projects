import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A':2,
    'B':4,
    'C':6,
    'D': 8
}

symbol_values = {
    'A':5,
    'B':4,
    'C':3,
    'D': 2
}


def check_win(columns, lines, bet, values):
    winning = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += values[symbol] * bet
            winning_line.append(line + 1)

    return winning, winning_line


def get_number_of_symbols(rows, cols, symbols):
    all_symbols = []
    for symbol,symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, value in enumerate(columns):
            if i != len(columns) - 1:
                print(value[row], end=" | ")
            else:
                print(value[row], end="")

        print()


def deposit():
    while True:
        amount = input("How much money do you want to play with: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Bet should be greater than 0")
        else:
            print("Bet should be a number!")
    return amount


def get_lines():
    while True:
        lines = input("Number of lines bet on: (1-" + str(MAX_LINES) + ") ?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines should be greater than 0")
        else:
            print("Lines should be a number!")
    return lines

def get_bet():
    while True:
        bet = input("How much money bet on each lines: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between {MIN_BET}$ - {MAX_BET}$")
        else:
            print("Bet should be a number!")
    return bet

def spin_game(balance):
    line = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * line
        if total_bet > balance:
            print(f"You have not enough money to bet. Your balance: {balance}$")
        else:
            break

    print(f"You are betting {bet}$ on {line} lines. Your total betting is equal to: {total_bet}$")

    slots = get_number_of_symbols(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnigs, winning_line = check_win(slots, line, bet, symbol_values)
    print(f"You won {winnigs}$")
    print(f"You won on line:", *winning_line)
    return winnigs - total_bet


def start_machine():
    balance = deposit()
    while True:
        print(f"Your current balance is: {balance}$")
        spin = input("Press enter to spin(q to quit).")
        if spin == 'q':
            break
        balance += spin_game(balance)

    print(f"You leave with {balance}$")
    print('Goodbye!')


start_machine()




