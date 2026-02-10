import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    activity_type: 'running',
    duration_minutes: '',
    distance: '',
    calories: '',
    notes: '',
    date: new Date().toISOString().split('T')[0]
  });

  const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

  useEffect(() => {
    fetchActivities();
  }, []);

  const fetchActivities = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/activities/`);
      if (response.ok) {
        const data = await response.json();
        setActivities(data);
      }
    } catch (error) {
      console.error('Error fetching activities:', error);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`${API_BASE_URL}/api/activities/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      });
      
      if (response.ok) {
        setShowForm(false);
        setFormData({
          activity_type: 'running',
          duration_minutes: '',
          distance: '',
          calories: '',
          notes: '',
          date: new Date().toISOString().split('T')[0]
        });
        fetchActivities();
      }
    } catch (error) {
      console.error('Error creating activity:', error);
    }
  };

  return (
    <div className="activities">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>My Activities</h2>
        <button 
          className="btn btn-primary"
          onClick={() => setShowForm(!showForm)}
        >
          {showForm ? 'Cancel' : '+ Log Activity'}
        </button>
      </div>

      {showForm && (
        <div className="card mb-4">
          <div className="card-body">
            <h5 className="card-title">Log New Activity</h5>
            <form onSubmit={handleSubmit}>
              <div className="row">
                <div className="col-md-6 mb-3">
                  <label className="form-label">Activity Type</label>
                  <select 
                    className="form-select"
                    name="activity_type"
                    value={formData.activity_type}
                    onChange={handleInputChange}
                    required
                  >
                    <option value="running">Running</option>
                    <option value="walking">Walking</option>
                    <option value="cycling">Cycling</option>
                    <option value="swimming">Swimming</option>
                    <option value="strength">Strength Training</option>
                    <option value="yoga">Yoga</option>
                    <option value="other">Other</option>
                  </select>
                </div>
                <div className="col-md-6 mb-3">
                  <label className="form-label">Date</label>
                  <input 
                    type="date"
                    className="form-control"
                    name="date"
                    value={formData.date}
                    onChange={handleInputChange}
                    required
                  />
                </div>
              </div>
              <div className="row">
                <div className="col-md-4 mb-3">
                  <label className="form-label">Duration (minutes)</label>
                  <input 
                    type="number"
                    className="form-control"
                    name="duration_minutes"
                    value={formData.duration_minutes}
                    onChange={handleInputChange}
                    required
                  />
                </div>
                <div className="col-md-4 mb-3">
                  <label className="form-label">Distance (miles)</label>
                  <input 
                    type="number"
                    step="0.1"
                    className="form-control"
                    name="distance"
                    value={formData.distance}
                    onChange={handleInputChange}
                  />
                </div>
                <div className="col-md-4 mb-3">
                  <label className="form-label">Calories</label>
                  <input 
                    type="number"
                    className="form-control"
                    name="calories"
                    value={formData.calories}
                    onChange={handleInputChange}
                  />
                </div>
              </div>
              <div className="mb-3">
                <label className="form-label">Notes</label>
                <textarea 
                  className="form-control"
                  name="notes"
                  rows="3"
                  value={formData.notes}
                  onChange={handleInputChange}
                ></textarea>
              </div>
              <button type="submit" className="btn btn-primary">Save Activity</button>
            </form>
          </div>
        </div>
      )}

      <div className="row">
        {activities.length === 0 ? (
          <div className="col-12">
            <div className="alert alert-info">
              No activities logged yet. Click "Log Activity" to get started!
            </div>
          </div>
        ) : (
          activities.map((activity) => (
            <div key={activity.id} className="col-md-6 mb-3">
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">
                    {activity.activity_type.charAt(0).toUpperCase() + activity.activity_type.slice(1)}
                  </h5>
                  <p className="card-text">
                    <strong>Duration:</strong> {activity.duration_minutes} minutes<br />
                    {activity.distance && <><strong>Distance:</strong> {activity.distance} miles<br /></>}
                    {activity.calories && <><strong>Calories:</strong> {activity.calories}<br /></>}
                    <strong>Points:</strong> {activity.points}<br />
                    <strong>Date:</strong> {activity.date}
                  </p>
                  {activity.notes && (
                    <p className="card-text"><small className="text-muted">{activity.notes}</small></p>
                  )}
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default Activities;
