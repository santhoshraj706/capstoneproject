import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

function PostReview() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [dealer, setDealer] = useState(null);
  const [formData, setFormData] = useState({
    name: '',
    review: '',
    purchase: false,
    purchase_date: '',
    car_make: '',
    car_model: '',
    car_year: '',
  });
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate('/login');
      return;
    }
    fetchDealer();
  }, [id]);

  const fetchDealer = async () => {
    try {
      const response = await axios.get(`${API_URL}/dealers/${id}/`);
      setDealer(response.data);
    } catch (err) {
      console.error('Error fetching dealer:', err);
    }
  };

  const handleChange = (e) => {
    const value = e.target.type === 'checkbox' ? e.target.checked : e.target.value;
    setFormData({ ...formData, [e.target.name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');

    try {
      const token = localStorage.getItem('token');
      const response = await axios.post(`${API_URL}/reviews/${id}/`, formData, {
        headers: { Authorization: `Token ${token}` },
      });
      setSuccess('Review submitted successfully!');
      setTimeout(() => navigate(`/dealer/${id}`), 2000);
    } catch (err) {
      setError('Failed to submit review. Please try again.');
    }
  };

  if (!dealer) {
    return <div className="auth-container"><p>Loading...</p></div>;
  }

  return (
    <div>
      <section className="page-hero">
        <div className="hero-content">
          <h1>Write a Review</h1>
          <p>Share your experience with {dealer.full_name}</p>
        </div>
      </section>

      <div className="auth-container">
        <div className="auth-card" style={{ maxWidth: '600px' }}>
          <h2>Review for {dealer.full_name}</h2>
          {error && <div className="error-msg">{error}</div>}
          {success && <div className="success-msg">{success}</div>}
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>Your Name</label>
              <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
                placeholder="Enter your name"
                required
              />
            </div>
            <div className="form-group">
              <label>Your Review</label>
              <textarea
                name="review"
                value={formData.review}
                onChange={handleChange}
                placeholder="Write your review here..."
                rows="5"
                required
              />
            </div>
            <div className="form-group" style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <input
                type="checkbox"
                name="purchase"
                checked={formData.purchase}
                onChange={handleChange}
                style={{ width: 'auto' }}
                id="purchase"
              />
              <label htmlFor="purchase" style={{ margin: 0 }}>I purchased a vehicle from this dealer</label>
            </div>
            {formData.purchase && (
              <>
                <div className="form-group">
                  <label>Purchase Date</label>
                  <input
                    type="date"
                    name="purchase_date"
                    value={formData.purchase_date}
                    onChange={handleChange}
                  />
                </div>
                <div className="form-group">
                  <label>Car Make</label>
                  <input
                    type="text"
                    name="car_make"
                    value={formData.car_make}
                    onChange={handleChange}
                    placeholder="e.g. Toyota, Honda"
                  />
                </div>
                <div className="form-group">
                  <label>Car Model</label>
                  <input
                    type="text"
                    name="car_model"
                    value={formData.car_model}
                    onChange={handleChange}
                    placeholder="e.g. Camry, Civic"
                  />
                </div>
                <div className="form-group">
                  <label>Car Year</label>
                  <input
                    type="number"
                    name="car_year"
                    value={formData.car_year}
                    onChange={handleChange}
                    placeholder="e.g. 2024"
                  />
                </div>
              </>
            )}
            <button type="submit" className="btn">
              <i className="fas fa-paper-plane"></i> Submit Review
            </button>
          </form>
          <p className="auth-link">
            <Link to={`/dealer/${id}`}>Back to dealer details</Link>
          </p>
        </div>
      </div>

      <footer className="footer">
        <div className="container">
          <p>&copy; 2026 CarDealership. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}

export default PostReview;
