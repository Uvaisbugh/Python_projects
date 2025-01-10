class ATM:
    def __init__(self):
        self.balance = 0.0

    def check_balance(self):
        """Return the current balance."""
        return self.balance

    def deposit(self, amount):
        """Deposit a positive amount into the ATM."""
        if amount <= 0:
            raise ValueError('Deposit amount must be positive.')
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw a positive amount from the ATM if sufficient funds are available."""
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive.')
        if amount > self.balance:
            raise ValueError('Insufficient funds.')
        self.balance -= amount


class ATMController:
    def __init__(self):
        self.atm = ATM()

    def get_number(self, prompt):
        """Prompt the user for a number and return it."""
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError:
                print('Please enter a valid number.')

    def display_menu(self):
        """Display the ATM menu options."""
        print('\nWelcome to the ATM!')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')

    def check_balance(self):
        """Check and display the current balance."""
        balance = self.atm.check_balance()
        print(f'Your current balance is: ${balance:.2f}')

    def deposit(self):
        """Handle the deposit process."""
        while True:
            try:
                amount = self.get_number('Enter the amount to deposit: ')
                self.atm.deposit(amount)
                print(f'Successfully deposited ${amount:.2f}.')
                break
            except ValueError as error:
                print(error)

    def withdraw(self):
        """Handle the withdrawal process."""
        while True:
            try:
                amount = self.get_number('Enter the amount to withdraw: ')
                self.atm.withdraw(amount)
                print(f'Successfully withdrew ${amount:.2f}.')
                break
            except ValueError as error:
                print(error)

    def run(self):
        """Run the ATM controller to handle user interactions."""
        while True:
            self.display_menu()
            choice = input('Please choose an option: ')
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print('Thank you for using the ATM. Goodbye!')
                break
            else:
                print('Invalid choice. Please try again.')


def main():
    """Main function to run the ATM application."""
    atm = ATMController()
    atm.run()


if __name__ == '__main__':
    main()