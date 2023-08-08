import React from 'react';

const Insights = ({ expenses }) => {
  const generateInsights = () => {
    // Calculate total expenses
    const totalExpenses = expenses.reduce((total, expense) => total + expense.amount, 0);

    // Calculate average expense
    const averageExpense = totalExpenses / expenses.length;

    // Calculate highest expense
    const highestExpense = Math.max(...expenses.map((expense) => expense.amount));

    // Calculate lowest expense
    const lowestExpense = Math.min(...expenses.map((expense) => expense.amount));

    return (
      <div>
        <h2>Expense Insights</h2>
        <p>Total Expenses: ${totalExpenses.toFixed(2)}</p>
        <p>Average Expense: ${averageExpense.toFixed(2)}</p>
        <p>Highest Expense: ${highestExpense.toFixed(2)}</p>
        <p>Lowest Expense: ${lowestExpense.toFixed(2)}</p>
      </div>
    );
  };

  return generateInsights();
};

export default Insights;
