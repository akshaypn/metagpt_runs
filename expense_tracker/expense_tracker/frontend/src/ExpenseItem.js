import React from 'react';

const ExpenseItem = ({ expense, deleteExpense }) => {
  const handleDelete = () => {
    deleteExpense(expense.id);
  };

  return (
    <div>
      <h3>{expense.category}</h3>
      <p>Amount: ${expense.amount.toFixed(2)}</p>
      <p>Description: {expense.description}</p>
      <p>Date: {expense.date}</p>
      <p>Account: {expense.account}</p>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
};

export default ExpenseItem;
