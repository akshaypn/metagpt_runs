"""
import React from 'react';

const Calendar = ({ expenses }) => {
  const handleClickDay = (date) => {
    console.log(`Clicked on ${date}`);
  };

  return (
    <div>
      <h2>Calendar</h2>
      <table>
        <thead>
          <tr>
            <th>Sun</th>
            <th>Mon</th>
            <th>Tue</th>
            <th>Wed</th>
            <th>Thu</th>
            <th>Fri</th>
            <th>Sat</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td onClick={() => handleClickDay('2022-01-01')}>1</td>
            <td onClick={() => handleClickDay('2022-01-02')}>2</td>
            <td onClick={() => handleClickDay('2022-01-03')}>3</td>
            <td onClick={() => handleClickDay('2022-01-04')}>4</td>
            <td onClick={() => handleClickDay('2022-01-05')}>5</td>
            <td onClick={() => handleClickDay('2022-01-06')}>6</td>
            <td onClick={() => handleClickDay('2022-01-07')}>7</td>
          </tr>
          <tr>
            <td onClick={() => handleClickDay('2022-01-08')}>8</td>
            <td onClick={() => handleClickDay('2022-01-09')}>9</td>
            <td onClick={() => handleClickDay('2022-01-10')}>10</td>
            <td onClick={() => handleClickDay('2022-01-11')}>11</td>
            <td onClick={() => handleClickDay('2022-01-12')}>12</td>
            <td onClick={() => handleClickDay('2022-01-13')}>13</td>
            <td onClick={() => handleClickDay('2022-01-14')}>14</td>
          </tr>
          {/* Repeat for other weeks */}
        </tbody>
      </table>
    </div>
  );
};

export default Calendar;
"""
