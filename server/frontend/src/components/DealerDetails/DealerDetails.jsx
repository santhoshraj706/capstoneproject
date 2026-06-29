import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

function DealerDetails() {
  const { id } = useParams();
  const [dealer, setDealer] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [loggedIn, setLoggedIn] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) setLoggedIn(true);
  }, []);

  useEffect(() => {
    fetchDealerDetails();
    fetchReviews();
  }, [id]);

  const fetchDealerDetails = async () => {
    try {
      const response = await axios.get(`${API_URL}/dealers/${id}/`);
      setDealer(response.data);
    } catch (err) {
      console.error('Error fetching dealer:', err);
    }
  };

  const fetchReviews = async () => {
    try {
      const response = await axios.get(`${API_URL}/reviews/${id}/`);
      setReviews(response.data);
      setLoading(false);
    } catch (err) {
      console.error('Error fetching reviews:', err);
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="auth-container"><p>Loading dealer details...</p></div>;
  }

  if (!dealer) {
    return <div className="auth-container"><p>Dealer not found.</p></div>;
  }

  return (
    <div>
      <section className="page-hero">
        <div className="hero-content">
          <h1>{dealer.full_name}</h1>
          <p>{dealer.address}, {dealer.city}, {dealer.state} {dealer.zip}</p>
        </div>
      </section>

      <section className="dealers-section">
        <div className="container">
          <div style={{ display: 'flex', gap: '20px', marginBottom: '30px', flexWrap: 'wrap' }}>
            <Link to="/" className="btn" style={{ width: 'auto', padding: '10px 25px', textDecoration: 'none' }}>
              <i className="fas fa-arrow-left"></i> Back to Dealers
            </Link>
            {loggedIn && (
              <Link to={`/postreview/${dealer.dealer_id}`} className="btn" style={{ width: 'auto', padding: '10px 25px', textDecoration: 'none', background: 'linear-gradient(135deg, #0f3460, #16213e)' }}>
                <i className="fas fa-star"></i> Write a Review
              </Link>
            )}
          </div>

          <div className="dealer-card" style={{ marginBottom: '40px' }}>
            <div className="dealer-card-body">
              <h3><i className="fas fa-building"></i> {dealer.full_name}</h3>
              <p><i className="fas fa-map-marker-alt"></i> {dealer.address}</p>
              <p><i className="fas fa-city"></i> {dealer.city}, {dealer.state} {dealer.zip}</p>
              {dealer.st && <p><i className="fas fa-globe"></i> {dealer.st}</p>}
              <p><i className="fas fa-map-pin"></i> Lat: {dealer.lat}, Long: {dealer.long}</p>
            </div>
          </div>

          <h2 style={{ fontSize: '2rem', color: '#1a1a2e', marginBottom: '25px' }}>
            <i className="fas fa-comments"></i> Reviews ({reviews.length})
          </h2>

          {reviews.length === 0 ? (
            <p style={{ textAlign: 'center', color: '#666', padding: '40px' }}>No reviews yet. Be the first to review!</p>
          ) : (
            <div className="reviews-container">
              {reviews.map(review => (
                <div key={review.id} className="review-card">
                  <div className="review-header">
                    <span className="reviewer-name">
                      <i className="fas fa-user"></i> {review.name}
                    </span>
                    <span className={`sentiment ${review.sentiment}`}>
                      <i className={`fas ${review.sentiment === 'positive' ? 'fa-smile' : review.sentiment === 'negative' ? 'fa-frown' : 'fa-meh'}`}></i>{' '}
                      {review.sentiment ? review.sentiment.charAt(0).toUpperCase() + review.sentiment.slice(1) : 'N/A'}
                    </span>
                  </div>
                  <p style={{ color: '#555', lineHeight: '1.6' }}>{review.review}</p>
                  <div style={{ marginTop: '10px', fontSize: '0.85rem', color: '#999' }}>
                    {review.purchase && <span style={{ marginRight: '15px' }}><i className="fas fa-check-circle" style={{ color: '#28a745' }}></i> Purchased</span>}
                    {review.car_make && <span style={{ marginRight: '15px' }}><i className="fas fa-car"></i> {review.car_make} {review.car_model} ({review.car_year})</span>}
                    {review.purchase_date && <span><i className="fas fa-calendar"></i> {review.purchase_date}</span>}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </section>

      <footer className="footer">
        <div className="container">
          <p>&copy; 2026 CarDealership. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}

export default DealerDetails;
