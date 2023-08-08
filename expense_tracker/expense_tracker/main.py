"""
main.py
Main entry point of the application
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense.db'
db = SQLAlchemy(app)

class Expense(db.Model):
    """
    Expense model
    """
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    date = db.Column(db.Date, nullable=False)
    account = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Expense(id={self.id}, amount={self.amount}, category={self.category}, description={self.description}, date={self.date}, account={self.account})"

@app.route('/api/v1/expenses/', methods=['GET'])
def get_expenses():
    """
    Get all expenses
    """
    expenses = Expense.query.all()
    expense_list = []
    for expense in expenses:
        expense_dict = {
            'id': expense.id,
            'amount': expense.amount,
            'category': expense.category,
            'description': expense.description,
            'date': expense.date.strftime('%Y-%m-%d'),
            'account': expense.account
        }
        expense_list.append(expense_dict)
    return jsonify(expense_list)

@app.route('/api/v1/expenses/', methods=['POST'])
def create_expense():
    """
    Create a new expense
    """
    expense_data = request.get_json()
    amount = expense_data.get('amount')
    category = expense_data.get('category')
    description = expense_data.get('description')
    date = expense_data.get('date')
    account = expense_data.get('account')

    expense = Expense(amount=amount, category=category, description=description, date=date, account=account)
    db.session.add(expense)
    db.session.commit()

    return jsonify({
        'id': expense.id,
        'amount': expense.amount,
        'category': expense.category,
        'description': expense.description,
        'date': expense.date.strftime('%Y-%m-%d'),
        'account': expense.account
    }), 201

@app.route('/api/v1/expenses/<int:expense_id>/', methods=['DELETE'])
def delete_expense(expense_id):
    """
    Delete an expense
    """
    expense = Expense.query.get(expense_id)
    if expense:
        db.session.delete(expense)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Expense not found'}), 404

if __name__ == '__main__':
    db.create_all()
    app.run()
