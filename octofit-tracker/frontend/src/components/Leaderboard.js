import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);

  const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

  useEffect(() => {
    fetchLeaderboard();
  }, []);

  const fetchLeaderboard = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/leaderboard/`);
      if (response.ok) {
        const data = await response.json();
        setLeaderboard(data);
      }
    } catch (error) {
      console.error('Error fetching leaderboard:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="leaderboard">
      <h2 className="mb-4">🏆 Leaderboard</h2>

      {loading ? (
        <div className="text-center">
          <div className="spinner-border" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      ) : (
        <div className="card">
          <div className="card-body">
            {leaderboard.length === 0 ? (
              <div className="alert alert-info">
                No users have logged activities yet. Be the first!
              </div>
            ) : (
              <div className="table-responsive">
                <table className="table table-striped">
                  <thead>
                    <tr>
                      <th>Rank</th>
                      <th>User</th>
                      <th>Fitness Level</th>
                      <th>Total Points</th>
                    </tr>
                  </thead>
                  <tbody>
                    {leaderboard.map((profile, index) => (
                      <tr key={profile.id}>
                        <td>
                          {index === 0 && '🥇'}
                          {index === 1 && '🥈'}
                          {index === 2 && '🥉'}
                          {index > 2 && `#${index + 1}`}
                        </td>
                        <td>{profile.username}</td>
                        <td>
                          <span className={`badge ${
                            profile.fitness_level === 'beginner' ? 'bg-info' :
                            profile.fitness_level === 'intermediate' ? 'bg-warning' :
                            'bg-danger'
                          }`}>
                            {profile.fitness_level.charAt(0).toUpperCase() + profile.fitness_level.slice(1)}
                          </span>
                        </td>
                        <td><strong>{profile.total_points}</strong> points</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default Leaderboard;
