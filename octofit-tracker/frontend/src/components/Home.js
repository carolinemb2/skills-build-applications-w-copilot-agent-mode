import React from 'react';

function Home() {
  return (
    <div className="home">
      <div className="jumbotron bg-light p-5 rounded">
        <h1 className="display-4">Welcome to OctoFit Tracker!</h1>
        <p className="lead">
          Your comprehensive fitness tracking companion. Track activities, join teams, 
          compete on leaderboards, and get personalized workout suggestions.
        </p>
        <hr className="my-4" />
        <p>
          Get started by logging your first activity or exploring workout suggestions 
          tailored to your fitness level.
        </p>
      </div>

      <div className="row mt-5">
        <div className="col-md-3">
          <div className="card text-center">
            <div className="card-body">
              <h5 className="card-title">🏃 Activities</h5>
              <p className="card-text">Log and track your fitness activities</p>
            </div>
          </div>
        </div>
        <div className="col-md-3">
          <div className="card text-center">
            <div className="card-body">
              <h5 className="card-title">👥 Teams</h5>
              <p className="card-text">Create or join fitness teams</p>
            </div>
          </div>
        </div>
        <div className="col-md-3">
          <div className="card text-center">
            <div className="card-body">
              <h5 className="card-title">🏆 Leaderboard</h5>
              <p className="card-text">Compete with others and track progress</p>
            </div>
          </div>
        </div>
        <div className="col-md-3">
          <div className="card text-center">
            <div className="card-body">
              <h5 className="card-title">💪 Workouts</h5>
              <p className="card-text">Get personalized workout suggestions</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
