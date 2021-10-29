from category import Category
from expensereport import ExpenseReport

if __name__ == '__main__':
    salary = Category("Salary")
    food = Category("Food")
    clothing = Category("Clothing")
    auto = Category("Auto")
    grocery = Category("Grocery")
    savings = Category("Savings")
    # Transactions
    salary.add_revenue(5000, "Salary from FIT")
    salary.add_expense(488, "Rent")
    salary.transfer_money(1000, food)
    salary.transfer_money(500, clothing)
    salary.transfer_money(200, auto)
    salary.transfer_money(500, savings)
    food.add_expense(15.89, "Mangestu Restaurant")
    clothing.add_expense(25.55, "H&M")
    clothing.add_expense(100, "Macy’s")
    auto.add_revenue(1000, "Sold my bike")
    auto.add_expense(15, "Tyre Change")
    # Transfer Between Categories
    food.transfer_money(50, grocery)
    grocery.add_expense(30.72, "Chili’s")
    grocery.add_expense(10.15, "Walmart")
    # Test Transaction For Categories
    print(grocery, end="\n\n")
    print(clothing, end="\n\n")
    print(food, end="\n\n")

    # Display an Expense Report as a Text -based Barchart
    expense_report = ExpenseReport()
    categories = [food, clothing, grocery]
    expense_report.show_expense_report(categories)
