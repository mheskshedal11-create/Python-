# python slot machine 
# import random
# def spin_row():
#     symbols=['🍉','🍎','🍊','🍋','⭐','🔔']

#     return[random.choice(symbols) for _ in range(3)]



# def print_row(row):
#     print('*************')
#     print('|'.join(row))
#     print('*************')

# def get_payout(row,bet):
#     if row[0]==row[1]==row[2]:
#         if row[0]=='🍉':
#             return bet *3
#         elif row[0]=='🍎':
#             return bet *4
#         elif row[0]=='🍊':
#             return bet * 5
#         elif row[0]=='🍋':
#             return bet * 6
#         elif row[0]=='⭐':
#             return bet * 7
#         elif row[0]=='🔔':
#             return bet *8
#     return 0
    

# def main():
#     balance=100
#     print('*****************************')
#     print('Welcome to pyton slots')
#     print('Symbols: 🍉🍎🍊🍋⭐🔔')
#     print('*****************************')
#     while balance>0:
#         print(f'current balance : ${balance}')

#         bet= input('Place your bet amount: ')

#         if not bet.isdigit():
#             print('Print Enter a valid number: ')
#             continue

#         bet = int(bet)

#         if bet >balance:
#             print(f'Insufficient Funds: ')
#             continue

#         if bet<=0:
#             print('bet must be greater than zero')
#             continue

#         balance -=bet

#         row = spin_row()
#         print('Spinning.........\n')
#         print_row(row)

#         payout= get_payout(row,bet)
#         if payout>0:
#             print(f' you own ${payout}')
#         else:
#             print('sorry you lost this round ')
        

#         balance +=payout

#         play_again= input('Do you wnat to spin again? (Y?N): ').upper()
#         if play_again !='Y':
#             break
#     print('*****************************')


# if __name__=='__main__':
#     main()




# =======================================

import random
import time

# Symbol weights (rarer symbols = higher payouts)
SYMBOLS = {
    "🍉": {"multiplier": 3, "weight": 6},
    "🍎": {"multiplier": 4, "weight": 5},
    "🍊": {"multiplier": 5, "weight": 4},
    "🍋": {"multiplier": 6, "weight": 3},
    "⭐": {"multiplier": 8, "weight": 2},
    "🔔": {"multiplier": 12, "weight": 1},  # Jackpot symbol
}


def spin_row():
    pool = []
    for symbol, data in SYMBOLS.items():
        pool.extend([symbol] * data["weight"])

    return [random.choice(pool) for _ in range(3)]


def print_row(row):
    print("\n🎰 Spinning...")
    time.sleep(0.5)
    print("************************")
    print(" | ".join(row))
    print("************************")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        multiplier = SYMBOLS[row[0]]["multiplier"]
        return bet * multiplier
    return 0


def get_bet(balance):
    while True:
        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("❌ Please enter a valid number.")
            continue

        bet = int(bet)

        if bet <= 0:
            print("❌ Bet must be greater than zero.")
        elif bet > balance:
            print("❌ Insufficient balance.")
        else:
            return bet


def main():
    balance = 100
    total_spins = 0
    total_wins = 0

    print("=================================")
    print("🎰 Welcome to Python Slot Machine")
    print("Symbols:", " ".join(SYMBOLS.keys()))
    print("=================================")

    while balance > 0:
        print(f"\n💰 Current balance: ${balance}")
        bet = get_bet(balance)

        balance -= bet
        total_spins += 1

        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"🎉 You WON ${payout}!")
            balance += payout
            total_wins += 1
        else:
            print("😢 You lost this round.")

        play_again = input("\nPlay again? (Y/N): ").upper()
        if play_again != "Y":
            break

    print("\n=========== GAME OVER ===========")
    print(f"Final balance: ${balance}")
    print(f"Total spins: {total_spins}")
    print(f"Total wins: {total_wins}")
    print("Thanks for playing! 🎰")


if __name__ == "__main__":
    main()