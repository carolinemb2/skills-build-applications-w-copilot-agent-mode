import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchTeams();
  }, []);

  const fetchTeams = async () => {
    try {
      const codespace = process.env.REACT_APP_CODESPACE_NAME;
      const baseUrl = codespace 
        ? `https://${codespace}-8000.app.github.dev`
        : 'http://localhost:8000';
      const apiUrl = `${baseUrl}/api/teams/`;
      
      console.log('Fetching teams from:', apiUrl);
      
      const response = await fetch(apiUrl);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      console.log('Teams data received:', data);
      
      // Handle both paginated (.results) and plain array responses
      const teamsArray = data.results || data;
      setTeams(teamsArray);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching teams:', error);
      setError(error.message);
      setLoading(false);
    }
  };

  if (loading) return <div className="text-center mt-5"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div></div>;
  if (error) return <div className="alert alert-danger" role="alert">Error: {error}</div>;

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Teams</h2>
      <div className="row">
        {teams.map((team) => (
          <div className="col-md-6 mb-4" key={team.id}>
            <div className="card">
              <div className="card-header bg-primary text-white">
                <h5 className="card-title mb-0">{team.name}</h5>
              </div>
              <div className="card-body">
                <p className="card-text">{team.description}</p>
                <div className="d-flex justify-content-between align-items-center">
                  <span className="badge bg-success fs-6">
                    Total Points: {team.total_points}
                  </span>
                  <small className="text-muted">
                    Created: {new Date(team.created_at).toLocaleDateString()}
                  </small>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Teams;
