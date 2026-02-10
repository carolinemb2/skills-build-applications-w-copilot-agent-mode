import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    // TODO: Fetch teams from API
    // For now, using sample data
    setTeams([
      {
        id: 1,
        name: 'Morning Warriors',
        description: 'Early morning workout enthusiasts',
        member_count: 15,
        created_at: '2024-01-15T00:00:00Z'
      }
    ]);
  }, []);

  return (
    <div className="teams">
      <h2>Fitness Teams</h2>
      <button className="btn btn-primary mb-3">Create New Team</button>
      
      <div className="row">
        {teams.length === 0 ? (
          <div className="col-12">
            <p className="text-center">No teams available. Create your first team!</p>
          </div>
        ) : (
          teams.map(team => (
            <div key={team.id} className="col-md-6 mb-3">
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">{team.name}</h5>
                  <p className="card-text">{team.description}</p>
                  <p className="text-muted">
                    <small>{team.member_count} members</small>
                  </p>
                  <button className="btn btn-sm btn-primary">Join Team</button>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default Teams;
