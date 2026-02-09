import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchLeaderboard();
  }, []);

  const fetchLeaderboard = async () => {
    try {
      const codespace = process.env.REACT_APP_CODESPACE_NAME;
      const baseUrl = codespace 
        ? `https://${codespace}-8000.app.github.dev`
        : 'http://localhost:8000';
      const apiUrl = `${baseUrl}/api/leaderboard/`;
      
      console.log('Fetching leaderboard from:', apiUrl);
      
      const response = await fetch(apiUrl);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      console.log('Leaderboard data received:', data);
      
      // Handle both paginated (.results) and plain array responses
      const leaderboardArray = data.results || data;
      setLeaderboard(leaderboardArray);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching leaderboard:', error);
      setError(error.message);
      setLoading(false);
    }
  };

  const getRankBadge = (rank) => {
    if (rank === 1) return 'bg-warning text-dark';
    if (rank === 2) return 'bg-secondary';
    if (rank === 3) return 'bg-danger';
    return 'bg-primary';
  };

  if (loading) return <div className="text-center mt-5"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div></div>;
  if (error) return <div className="alert alert-danger" role="alert">Error: {error}</div>;

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Leaderboard</h2>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead className="table-dark">
            <tr>
              <th>Rank</th>
              <th>User Name</th>
              <th>Team</th>
              <th>Total Points</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.map((entry) => (
              <tr key={entry.id}>
                <td>
                  <span className={`badge ${getRankBadge(entry.rank)} fs-6`}>
                    #{entry.rank}
                  </span>
                </td>
                <td>{entry.user_name}</td>
                <td><span className="badge bg-info">{entry.team_name}</span></td>
                <td><span className="badge bg-success fs-6">{entry.total_points}</span></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;
