# Budget-app
Python budget application: a Category class to track expenses and income by category, featuring inter-category transfers and an ASCII bar chart showing the percentage of spending per category.

## Description

The module defines a `Category` class that models a single budget
category as a simple ledger of deposits and withdrawals, plus a
`create_spend_chart` function that compares spending across several
categories.

### `Category`

- `Category(name)` — creates a category with an empty `ledger` list.
- `deposit(amount, description="")` — adds a positive entry to the ledger.
- `withdraw(amount, description="")` — adds a negative entry if there are
  enough funds; returns `True` on success, `False` otherwise.
- `get_balance()` — returns the current balance (sum of the ledger).
- `transfer(amount, other_category)` — withdraws from this category and
  deposits into `other_category`, labeling both entries automatically;
  returns `True`/`False` for success.
- `check_funds(amount)` — returns whether the category can cover
  `amount`; used internally by `withdraw` and `transfer`.
- `__str__` — pretty-prints the category as a centered title, one line
  per ledger entry (description left-aligned, amount right-aligned),
  and a `Total:` line.

### `create_spend_chart(categories)`

Builds a bar chart (as a string) showing what percentage of total
spending (withdrawals only) came from each category, rounded down to
the nearest 10%, with category names spelled out vertically beneath
their bars.

## Usage

```python
from budget import Category, create_spend_chart

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing]))
```
