import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchWorkouts();
  }, []);

  const fetchWorkouts = async () => {
    try {
      const codespace = process.env.REACT_APP_CODESPACE_NAME;
      const baseUrl = codespace 
        ? `https://${codespace}-8000.app.github.dev`
        : 'http://localhost:8000';
      const apiUrl = `${baseUrl}/api/workouts/`;
      
      console.log('Fetching workouts from:', apiUrl);
      
      const response = await fetch(apiUrl);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      console.log('Workouts data received:', data);
      
      // Handle both paginated (.results) and plain array responses
      const workoutsArray = data.results || data;
      setWorkouts(workoutsArray);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching workouts:', error);
      setError(error.message);
      setLoading(false);
    }
  };

  const getDifficultyBadge = (difficulty) => {
    switch (difficulty.toLowerCase()) {
      case 'easy': return 'bg-success';
      case 'medium': return 'bg-warning text-dark';
      case 'hard': return 'bg-danger';
      default: return 'bg-secondary';
    }
  };

  if (loading) return <div className="text-center mt-5"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div></div>;
  if (error) return <div className="alert alert-danger" role="alert">Error: {error}</div>;

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Workouts</h2>
      <div className="row">
        {workouts.map((workout) => (
          <div className="col-md-6 col-lg-4 mb-4" key={workout.id}>
            <div className="card h-100">
              <div className="card-header bg-dark text-white">
                <h5 className="card-title mb-0">{workout.name}</h5>
              </div>
              <div className="card-body">
                <p className="card-text">{workout.description}</p>
                <div className="mb-2">
                  <span className={`badge ${getDifficultyBadge(workout.difficulty_level)} me-2`}>
                    {workout.difficulty_level}
                  </span>
                  <span className="badge bg-info me-2">
                    {workout.estimated_duration} min
                  </span>
                  <span className="badge bg-primary">
                    {workout.points_value} pts
                  </span>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Workouts;
