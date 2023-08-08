import React, { useState, useEffect } from 'react';
import Calendar from './Calendar';
import Visualizations from './Visualizations';
import Insights from './Insights';
import ExpenseForm from './ExpenseForm';
import ExpenseList from './ExpenseList';
import ExportButton from './ExportButton';
import ImportButton from './ImportButton';

const App = () => {
  const [expenses, setExpenses] = useState([]);

  useEffect(() => {
    fetchExpenses();
  }, []);

  const fetchExpenses = async () => {
    try {
      const response = await fetch('/api/v1/expenses/');
      const data = await response.json();
      setExpenses(data);
    } catch (error) {
      console.error('Error fetching expenses:', error);
    }
  };

  const addExpense = async (expense) => {
    try {
      const response = await fetch('/api/v1/expenses/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(expense),
      });
      const data = await response.json();
      setExpenses([...expenses, data]);
    } catch (error) {
      console.error('Error adding expense:', error);
    }
  };

  const deleteExpense = async (expenseId) => {
    try {
      await fetch(`/api/v1/expenses/${expenseId}/`, {
        method: 'DELETE',
      });
      setExpenses(expenses.filter((expense) => expense.id !== expenseId));
    } catch (error) {
      console.error('Error deleting expense:', error);
    }
  };

  return (
    <div>
      <h1>Expense Tracker</h1>
      <Calendar expenses={expenses} />
      <Visualizations expenses={expenses} />
      <Insights expenses={expenses} />
      <ExpenseForm addExpense={addExpense} />
      <ExpenseList expenses={expenses} deleteExpense={deleteExpense} />
      <ExportButton expenses={expenses} />
      <ImportButton addExpense={addExpense} />
    </div>
  );
};

export default App;
