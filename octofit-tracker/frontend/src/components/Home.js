import React from 'react';

function Home() {
  return (
    <div className="home">
      <div className="jumbotron bg-light p-5 rounded">
        <h1 className="display-4">Welcome to OctoFit Tracker!</h1>
        <p className="lead">
          Track your fitness activities, compete with friends, and achieve your wellness goals.
        </p>
        <hr className="my-4" />
        <p>
          OctoFit Tracker helps students and fitness enthusiasts log workouts, join teams, 
          and climb the leaderboard. Get started by logging your first activity!
        </p>
        <a className="btn btn-primary btn-lg" href="/activities" role="button">
          Log Activity
        </a>
      </div>

      <div className="row mt-5">
        <div className="col-md-4">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">📊 Track Activities</h5>
              <p className="card-text">
                Log running, walking, cycling, swimming, strength training, and more.
                Track your progress over time.
              </p>
            </div>
          </div>
        </div>
        <div className="col-md-4">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">👥 Join Teams</h5>
              <p className="card-text">
                Create or join teams to compete together. Work as a group to climb 
                the leaderboard and achieve collective goals.
              </p>
            </div>
          </div>
        </div>
        <div className="col-md-4">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">🏆 Compete</h5>
              <p className="card-text">
                Earn points for your activities and see how you rank against others. 
                Friendly competition makes fitness fun!
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
