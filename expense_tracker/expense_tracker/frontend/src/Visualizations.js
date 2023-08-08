import React from 'react';
import { Bar } from 'react-chartjs-2';

const Visualizations = ({ expenses }) => {
  const getExpenseByCategory = () => {
    const categories = {};
    expenses.forEach((expense) => {
      if (categories[expense.category]) {
        categories[expense.category] += expense.amount;
      } else {
        categories[expense.category] = expense.amount;
      }
    });
    return categories;
  };

  const generateVisualizations = () => {
    const categories = getExpenseByCategory();
    const labels = Object.keys(categories);
    const data = Object.values(categories);

    const chartData = {
      labels: labels,
      datasets: [
        {
          label: 'Expense Amount',
          data: data,
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1,
        },
      ],
    };

    const chartOptions = {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    };

    return (
      <div>
        <h2>Expense Visualization</h2>
        <Bar data={chartData} options={chartOptions} />
      </div>
    );
  };

  return generateVisualizations();
};

export default Visualizations;
