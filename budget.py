class Category:
    """Represents a single budget category (e.g. Food, Clothing, Auto).

    Keeps a ledger of deposits/withdrawals and supports transferring
    funds between categories.
    """

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category_instance):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category_instance.name}")
            category_instance.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"

        items = ""
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}"[:7].rjust(7)
            items += f"{desc}{amt}\n"

        total = f"Total: {self.get_balance():.2f}"

        return title + items + total


def create_spend_chart(categories):
    # 1. Total withdrawals per category (deposits are ignored).
    spent_per_cat = []
    total_spent = 0
    for cat in categories:
        cat_spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spent_per_cat.append(cat_spent)
        total_spent += cat_spent

    percentages = [
        (spent / total_spent) * 100 if total_spent else 0
        for spent in spent_per_cat
    ]

    # 2. Bar chart, 100 down to 0 in steps of 10.
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for pct in percentages:
            chart += "o  " if pct >= i else "   "
        chart += "\n"

    # 3. Horizontal line, two characters past the final bar.
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 4. Category names written vertically below the bars.
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        chart += "     "
        for cat in categories:
            chart += cat.name[i] + "  " if i < len(cat.name) else "   "
        if i != max_len - 1:
            chart += "\n"

    return chart
