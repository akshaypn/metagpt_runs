## frontend/src/ExportButton.js
import React from 'react';
import { saveAs } from 'file-saver';

const ExportButton = ({ expenses }) => {
  const exportExpenses = () => {
    const csvData = convertExpensesToCSV(expenses);
    const blob = new Blob([csvData], { type: 'text/csv;charset=utf-8' });
    saveAs(blob, 'expenses.csv');
  };

  const convertExpensesToCSV = (expenses) => {
    const headers = ['ID', 'Amount', 'Category', 'Description', 'Date', 'Account'];
    const rows = expenses.map((expense) => [
      expense.id,
      expense.amount,
      expense.category,
      expense.description,
      expense.date,
      expense.account,
    ]);
    const csvArray = [headers, ...rows];
    return csvArray.map((row) => row.join(',')).join('\n');
  };

  return (
    <div>
      <button onClick={exportExpenses}>Export Expenses</button>
    </div>
  );
};

export default ExportButton;
