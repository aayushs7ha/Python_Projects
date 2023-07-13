import datetime

class DailyCashInOutApp:
    def __init__(self):
        self.balance = 20000
        self.daily_balance = {}
        self.current_date = datetime.date.today()

    def cash_in(self, amount):
        if amount > 0:
            self.balance += amount
            self._update_daily_balance(amount)
            print(f"Cash in: Rs {amount}")
        else:
            print("Invalid amount. Cash in failed.")

    def cash_out(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self._update_daily_balance(-amount)
            print(f"Cash out: Rs {amount}")
        else:
            print("Invalid amount. Cash out failed.")

    def display_balance(self):
        print(f"Current balance: Rs {self.balance}")

    def display_daily_balance(self, date):
        if date in self.daily_balance:
            balance = self.daily_balance[date]
            print(f"Balance on {date}: Rs {balance}")
        else:
            print("No record found for the given date.")

    def _update_daily_balance(self, amount):
        if self.current_date in self.daily_balance:
            self.daily_balance[self.current_date] += amount
        else:
            self.daily_balance[self.current_date] = self.balance


def main():
    app = DailyCashInOutApp()

    while True:
        print("Daily Cash-In/Cash-Out App")
        print("1. Cash in")
        print("2. Cash out")
        print("3. Display current balance")
        print("4. Display daily balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter the amount to cash in: Rs "))
            app.cash_in(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to cash out: Rs "))
            app.cash_out(amount)
        elif choice == '3':
            app.display_balance()
        elif choice == '4':
            date_str = input("Enter the date (YYYY-MM-DD): ")
            try:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                app.display_daily_balance(date)
            except ValueError:
                print("Invalid date format. Please try again.")
        elif choice == '5':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
