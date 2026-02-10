import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [period, setPeriod] = useState('weekly');
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    // TODO: Fetch leaderboard from API
    // For now, using sample data
    setEntries([
      {
        id: 1,
        user_username: 'fitness_pro',
        rank: 1,
        total_activities: 25,
        total_duration: 1500,
        total_distance: 125.5,
        total_calories: 15000
      },
      {
        id: 2,
        user_username: 'runner_jane',
        rank: 2,
        total_activities: 20,
        total_duration: 1200,
        total_distance: 100.0,
        total_calories: 12000
      }
    ]);
  }, [period]);

  return (
    <div className="leaderboard">
      <h2>Leaderboard</h2>
      
      <div className="btn-group mb-3" role="group">
        <button 
          className={`btn ${period === 'daily' ? 'btn-primary' : 'btn-outline-primary'}`}
          onClick={() => setPeriod('daily')}
        >
          Daily
        </button>
        <button 
          className={`btn ${period === 'weekly' ? 'btn-primary' : 'btn-outline-primary'}`}
          onClick={() => setPeriod('weekly')}
        >
          Weekly
        </button>
        <button 
          className={`btn ${period === 'monthly' ? 'btn-primary' : 'btn-outline-primary'}`}
          onClick={() => setPeriod('monthly')}
        >
          Monthly
        </button>
      </div>

      <div className="table-responsive">
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Rank</th>
              <th>User</th>
              <th>Activities</th>
              <th>Duration (min)</th>
              <th>Distance (km)</th>
              <th>Calories</th>
            </tr>
          </thead>
          <tbody>
            {entries.length === 0 ? (
              <tr>
                <td colSpan="6" className="text-center">
                  No leaderboard data available for this period.
                </td>
              </tr>
            ) : (
              entries.map(entry => (
                <tr key={entry.id}>
                  <td>
                    {entry.rank === 1 && '🥇'}
                    {entry.rank === 2 && '🥈'}
                    {entry.rank === 3 && '🥉'}
                    {entry.rank > 3 && entry.rank}
                  </td>
                  <td>{entry.user_username}</td>
                  <td>{entry.total_activities}</td>
                  <td>{entry.total_duration}</td>
                  <td>{entry.total_distance}</td>
                  <td>{entry.total_calories}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;
