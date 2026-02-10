import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [difficulty, setDifficulty] = useState('all');

  useEffect(() => {
    // TODO: Fetch workout suggestions from API
    // For now, using sample data
    setWorkouts([
      {
        id: 1,
        title: '30-Minute Cardio Blast',
        description: 'High-intensity cardio workout to boost your metabolism',
        category: 'cardio',
        difficulty: 'intermediate',
        duration: 30,
        calories_estimate: 300
      },
      {
        id: 2,
        title: 'Beginner Strength Training',
        description: 'Build foundational strength with basic exercises',
        category: 'strength',
        difficulty: 'beginner',
        duration: 45,
        calories_estimate: 250
      }
    ]);
  }, [difficulty]);

  const filteredWorkouts = difficulty === 'all' 
    ? workouts 
    : workouts.filter(w => w.difficulty === difficulty);

  return (
    <div className="workouts">
      <h2>Workout Suggestions</h2>
      
      <div className="mb-3">
        <label className="form-label">Filter by Difficulty:</label>
        <select 
          className="form-select" 
          value={difficulty} 
          onChange={(e) => setDifficulty(e.target.value)}
        >
          <option value="all">All Levels</option>
          <option value="beginner">Beginner</option>
          <option value="intermediate">Intermediate</option>
          <option value="advanced">Advanced</option>
        </select>
      </div>

      <div className="row">
        {filteredWorkouts.length === 0 ? (
          <div className="col-12">
            <p className="text-center">No workouts available for this difficulty level.</p>
          </div>
        ) : (
          filteredWorkouts.map(workout => (
            <div key={workout.id} className="col-md-6 mb-3">
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">{workout.title}</h5>
                  <p className="card-text">{workout.description}</p>
                  <div className="d-flex justify-content-between align-items-center">
                    <div>
                      <span className="badge bg-primary me-2">{workout.category}</span>
                      <span className="badge bg-secondary">{workout.difficulty}</span>
                    </div>
                    <div className="text-muted">
                      <small>{workout.duration} min | {workout.calories_estimate} cal</small>
                    </div>
                  </div>
                  <button className="btn btn-sm btn-success mt-3">Start Workout</button>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default Workouts;
