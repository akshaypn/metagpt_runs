"""
serializers.py
Contains the Expense, ExpenseSerializer, and ExpenseList classes for managing expenses.
"""

from datetime import date
from typing import List


class Expense:
    """
    Expense model class.
    """

    def __init__(self, id: int, amount: float, category: str, description: str, date: date, account: str):
        self.id = id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
        self.account = account


class ExpenseSerializer:
    """
    Serializer class for Expense objects.
    """

    def __init__(self, expense: Expense):
        self.id = expense.id
        self.amount = expense.amount
        self.category = expense.category
        self.description = expense.description
        self.date = expense.date
        self.account = expense.account


class ExpenseList:
    """
    Class for managing a list of expenses.
    """

    def __init__(self):
        self.expenses = []

    def add_expense(self, expense: Expense) -> None:
        """
        Add an expense to the list.
        """
        self.expenses.append(expense)

    def delete_expense(self, expense_id: int) -> None:
        """
        Delete an expense from the list by ID.
        """
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]

    def get_expenses(self) -> List[Expense]:
        """
        Get all expenses in the list.
        """
        return self.expenses
