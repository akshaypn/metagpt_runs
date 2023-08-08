import React, { useState } from 'react';

const ImportButton = ({ addExpense }) => {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const importExpenses = () => {
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const csvData = e.target.result;
        const expenses = parseCSV(csvData);
        expenses.forEach((expense) => addExpense(expense));
      };
      reader.readAsText(file);
    }
  };

  const parseCSV = (csvData) => {
    const rows = csvData.split('\n');
    const headers = rows[0].split(',');
    const expenses = [];
    for (let i = 1; i < rows.length; i++) {
      const row = rows[i].split(',');
      const expense = {};
      for (let j = 0; j < headers.length; j++) {
        expense[headers[j]] = row[j];
      }
      expenses.push(expense);
    }
    return expenses;
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={importExpenses}>Import Expenses</button>
    </div>
  );
};

export default ImportButton;
