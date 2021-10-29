class ExpenseReport:

    def show_expense_report(self, categories: list):
        total = 0

        # get total balance of all categories
        for category in categories:
            total += category.get_expenses()
        for category in categories:
            percentage = category.get_expenses() / total
            print(f"{category.category_name:<20}|" + ("o" * int(percentage * 100)) + f"({percentage * 100:.2f}%)")

        print(f"{' |':>21}", end="")
        for _ in range(10):
            print("-" * 9, end="")
            print("+", end="")
        print()
        print(f"{' ':<20} " * 9, end="")
        for i in range(10,110, 10):

            print(f"{i:<10}", end="")
