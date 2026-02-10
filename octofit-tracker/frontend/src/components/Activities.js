import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    // TODO: Fetch activities from API
    // For now, using sample data
    setActivities([
      {
        id: 1,
        activity_type: 'running',
        duration: 30,
        distance: 5.0,
        calories: 300,
        activity_date: '2024-02-10T08:00:00Z',
        notes: 'Morning run'
      }
    ]);
  }, []);

  return (
    <div className="activities">
      <h2>My Activities</h2>
      <button className="btn btn-primary mb-3">Log New Activity</button>
      
      <div className="table-responsive">
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Type</th>
              <th>Duration (min)</th>
              <th>Distance (km)</th>
              <th>Calories</th>
              <th>Date</th>
              <th>Notes</th>
            </tr>
          </thead>
          <tbody>
            {activities.length === 0 ? (
              <tr>
                <td colSpan="6" className="text-center">
                  No activities logged yet. Start tracking your fitness journey!
                </td>
              </tr>
            ) : (
              activities.map(activity => (
                <tr key={activity.id}>
                  <td>{activity.activity_type}</td>
                  <td>{activity.duration}</td>
                  <td>{activity.distance}</td>
                  <td>{activity.calories}</td>
                  <td>{new Date(activity.activity_date).toLocaleDateString()}</td>
                  <td>{activity.notes}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Activities;
