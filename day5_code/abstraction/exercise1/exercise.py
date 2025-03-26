import random

class CommandPrompt:
    """
    Trida na interakci uzivatele s Forex trzistem.
    Podle uzivatelskeho vstupu muzeme prodavat/nakupovat/cekat.
    Jedna se o konverzi mezi PLN/USD.
    """
    def __init__(self, buy_commands, sell_commands, wait_commands):
        self.buy_commands = buy_commands
        self.sell_commands = sell_commands
        self.wait_commands = wait_commands

    def ask(self):
        users_choice = input("Enter command: buy/sell/wait")
        if users_choice in self.buy_commands:
            return "buy"
        elif users_choice in self.sell_commands:
            return "sell"
        elif users_choice in self.wait_commands:
            return "wait"
        else:
            print(f"Invalid choice: {users_choice}")
            return None

class Wallet:
    def __init__(self, initial_pln, initial_usd):
        if isinstance(initial_pln, float):
            self.pln = initial_pln
        if isinstance(initial_usd, float):
            self.usd = initial_usd

    def convert_pln_to_usd(self, usdpln_rate):
        pln_converted_to_usd = self.pln * (1/usdpln_rate)
        self.usd += pln_converted_to_usd
        self.pln = 0

    def convert_usd_to_pln(self, usdpln_rate):
        usd_converted_to_pln = self.usd * usdpln_rate
        self.pln += usd_converted_to_pln
        self.usd = 0


random_usdpln_rates = [3.5]
for _ in range(50):
    random_usdpln_rates.append(round(random_usdpln_rates[-1] + random.random() * 0.2 - 0.1, 2))

cm = CommandPrompt(
    buy_commands=("b", "buy"),
    sell_commands=("s", "sell"),
    wait_commands=("w", "wait")
)

def main(usdpln_rates):
    wallet = Wallet(
        initial_pln=100.0,
        initial_usd=0.0
    )

    for usdpln_rate in usdpln_rates:
        print(f'Balance: {round(wallet.pln, 2)} PLN, ${round(wallet.usd, 2)}, rate {usdpln_rate}')

        while True:
            user_command = cm.ask()
            # metoda ask nam vrati -> "buy" \ "sell" \ "wait" \ None
            #if user_command is not None: # (user_command == None)
            if user_command: # bool(user_command)
                break

        if user_command in ('b', 'buy'):
            wallet.convert_pln_to_usd(usdpln_rate)

        elif user_command in ('s', 'sell'):
            wallet.convert_usd_to_pln(usdpln_rate)

    wallet.convert_usd_to_pln(usdpln_rate)
    # wallet.pln += wallet.usd * usdpln_rate
    # wallet.usd = 0
    print(f'Your result: {wallet.pln} PLN!')


if __name__ == '__main__':
    main(random_usdpln_rates)