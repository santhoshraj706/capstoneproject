import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

function Home() {
  const [dealers, setDealers] = useState([]);
  const [filteredDealers, setFilteredDealers] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [states, setStates] = useState([]);
  const [activeState, setActiveState] = useState('All');
  const [loading, setLoading] = useState(true);
  const [user, setUser] = useState(null);
  const [loggedIn, setLoggedIn] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('token');
    const userData = localStorage.getItem('user');
    if (token && userData) {
      setLoggedIn(true);
      setUser(JSON.parse(userData));
    }
  }, []);

  useEffect(() => {
    fetchDealers();
  }, []);

  const fetchDealers = async () => {
    try {
      const response = await axios.get(`${API_URL}/dealers/`);
      setDealers(response.data);
      setFilteredDealers(response.data);
      const uniqueStates = [...new Set(response.data.map(d => d.state))].sort();
      setStates(uniqueStates);
      setLoading(false);
    } catch (err) {
      console.error('Error fetching dealers:', err);
      setLoading(false);
    }
  };

  const handleSearch = () => {
    const filtered = dealers.filter(d =>
      d.full_name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      d.city?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      d.state?.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredDealers(filtered);
  };

  const filterByState = (state) => {
    setActiveState(state);
    if (state === 'All') {
      setFilteredDealers(dealers);
    } else {
      setFilteredDealers(dealers.filter(d => d.state === state));
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    setLoggedIn(false);
    setUser(null);
  };

  if (loading) {
    return (
      <div className="auth-container">
        <p>Loading dealers...</p>
      </div>
    );
  }

  return (
    <div>
      <section className="page-hero">
        <div className="hero-content">
          <h1>Welcome to CarDealership</h1>
          <p>Find your dream car from our trusted network of dealers</p>
          {loggedIn && user && (
            <p style={{ marginTop: '15px', color: '#e94560', fontWeight: 600 }}>
              Welcome, {user.username}!
            </p>
          )}
        </div>
      </section>

      <section className="dealers-section">
        <div className="container">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '30px' }}>
            <h2 style={{ fontSize: '2rem', color: '#1a1a2e' }}>Our Dealers</h2>
            {loggedIn ? (
              <button onClick={handleLogout} className="btn" style={{ width: 'auto', padding: '10px 25px', background: '#666' }}>
                <i className="fas fa-sign-out-alt"></i> Logout
              </button>
            ) : (
              <Link to="/login" className="btn" style={{ width: 'auto', padding: '10px 25px', textDecoration: 'none' }}>
                <i className="fas fa-sign-in-alt"></i> Login to Review
              </Link>
            )}
          </div>

          <div className="search-bar">
            <input
              type="text"
              placeholder="Search dealers by name, city, or state..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
            />
            <button onClick={handleSearch}><i className="fas fa-search"></i> Search</button>
          </div>

          <div className="filter-buttons">
            <button
              className={`filter-btn ${activeState === 'All' ? 'active' : ''}`}
              onClick={() => filterByState('All')}
            >
              All
            </button>
            {states.map(state => (
              <button
                key={state}
                className={`filter-btn ${activeState === state ? 'active' : ''}`}
                onClick={() => filterByState(state)}
              >
                {state}
              </button>
            ))}
          </div>

          {filteredDealers.length === 0 ? (
            <p style={{ textAlign: 'center', color: '#666', padding: '40px' }}>No dealers found.</p>
          ) : (
            <div className="dealers-grid">
              {filteredDealers.map(dealer => (
                <div key={dealer.dealer_id} className="dealer-card">
                  <div className="dealer-card-body">
                    <h3><i className="fas fa-building"></i> {dealer.full_name}</h3>
                    <p><i className="fas fa-map-marker-alt"></i> {dealer.city}, {dealer.state} {dealer.zip}</p>
                    <p><i className="fas fa-road"></i> {dealer.address}</p>
                    <div style={{ display: 'flex', gap: '10px', marginTop: '15px' }}>
                      <Link to={`/dealer/${dealer.dealer_id}`} className="btn" style={{ flex: 1, textAlign: 'center', textDecoration: 'none', width: 'auto', padding: '10px' }}>
                        <i className="fas fa-info-circle"></i> View Details
                      </Link>
                      {loggedIn && (
                        <Link to={`/postreview/${dealer.dealer_id}`} className="btn" style={{ flex: 1, textAlign: 'center', textDecoration: 'none', width: 'auto', padding: '10px', background: 'linear-gradient(135deg, #0f3460, #16213e)' }}>
                          <i className="fas fa-star"></i> Review Dealer
                        </Link>
                      )}
                    </div>
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

export default Home;
