import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchActivities();
  }, []);

  const fetchActivities = async () => {
    try {
      const codespace = process.env.REACT_APP_CODESPACE_NAME;
      const baseUrl = codespace 
        ? `https://${codespace}-8000.app.github.dev`
        : 'http://localhost:8000';
      const apiUrl = `${baseUrl}/api/activities/`;
      
      console.log('Fetching activities from:', apiUrl);
      
      const response = await fetch(apiUrl);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      console.log('Activities data received:', data);
      
      // Handle both paginated (.results) and plain array responses
      const activitiesArray = data.results || data;
      setActivities(activitiesArray);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching activities:', error);
      setError(error.message);
      setLoading(false);
    }
  };

  if (loading) return <div className="text-center mt-5"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div></div>;
  if (error) return <div className="alert alert-danger" role="alert">Error: {error}</div>;

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Activities</h2>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead className="table-dark">
            <tr>
              <th>ID</th>
              <th>User ID</th>
              <th>Activity Type</th>
              <th>Duration (min)</th>
              <th>Points Earned</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            {activities.map((activity) => (
              <tr key={activity.id}>
                <td>{activity.id}</td>
                <td>{activity.user_id}</td>
                <td><span className="badge bg-info">{activity.activity_type}</span></td>
                <td>{activity.duration_minutes}</td>
                <td><span className="badge bg-success">{activity.points_earned}</span></td>
                <td>{new Date(activity.date).toLocaleDateString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Activities;
