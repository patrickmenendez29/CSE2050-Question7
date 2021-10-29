class Category:

    def __init__(self, category_name: str):
        self.wallet = []
        self.category_name = category_name.title()
        pass

    def add_revenue(self, amount, desc):
        self.wallet.append({"amount": amount, "description": desc})
        pass

    def add_expense(self, amount, desc=""):
        if self.check_category_balance(amount):
            return False
        self.wallet.append({"amount": -amount, "description": desc.title()})
        return True

    def transfer_money(self, amount, category):
        if self.check_category_balance(amount):
            return False
        self.wallet.append({"amount": -amount, "description":  f"Send to {category.category_name}"})
        category.add_revenue(amount, f"Send money from {self.category_name}")
        return True

    def get_balance(self):
        total = 0
        for item in self.wallet:
            total += float(item["amount"])

        return total

    def check_category_balance(self, amount):
        return self.get_balance() < amount

    def get_expenses(self):
        expenses = 0
        for item in self.wallet:
            amount = float(item["amount"])
            if amount < 0:
                expenses += amount
        return expenses

    def __str__(self):
        string_builder = f"{self.category_name:*^30}"

        for item in self.wallet:
            row = f"{item['description']:<25}{item['amount']:>10.2f}"
            string_builder += "\n" + row
        string_builder += "\n" + f"Total: {self.get_balance():.2f}"
        return string_builder
