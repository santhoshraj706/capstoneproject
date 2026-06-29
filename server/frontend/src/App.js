import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom';
import './App.css';
import Register from './components/Register/Register';
import Login from './components/Login/Login';
import Home from './components/Home/Home';
import DealerDetails from './components/DealerDetails/DealerDetails';
import PostReview from './components/PostReview/PostReview';

function NavBar() {
  const location = useLocation();

  const isActive = (path) => {
    return location.pathname === path ? 'active' : '';
  };

  return (
    <nav className="navbar">
      <div className="nav-container">
        <div className="nav-brand">
          <i className="fas fa-car"></i>
          <span>CarDealership</span>
        </div>
        <ul className="nav-menu">
          <li><Link to="/" className={isActive('/')}><i className="fas fa-home"></i> Home</Link></li>
          <li><Link to="/about" className={isActive('/about')}><i className="fas fa-info-circle"></i> About Us</Link></li>
          <li><Link to="/contact" className={isActive('/contact')}><i className="fas fa-envelope"></i> Contact Us</Link></li>
          <li><Link to="/register" className={isActive('/register')}><i className="fas fa-user-plus"></i> Register</Link></li>
          <li><Link to="/login" className={isActive('/login')}><i className="fas fa-sign-in-alt"></i> Login</Link></li>
        </ul>
      </div>
    </nav>
  );
}

function About() {
  return (
    <div>
      <section className="page-hero">
        <div className="hero-content">
          <h1>About Us</h1>
          <p>Your trusted partner in finding the perfect vehicle</p>
        </div>
      </section>
      <section className="about-section">
        <div className="container">
          <div className="about-intro">
            <h2>Who We Are</h2>
            <p>CarDealership is a premier automotive dealership committed to providing exceptional vehicles and outstanding customer service.</p>
          </div>
          <div className="team-grid">
            <div className="team-card">
              <div className="team-img" style={{backgroundImage: "url('https://images.unsplash.com/photo-1560250097-0b93528c311a?w=200&h=200&fit=crop&crop=face')"}}></div>
              <h3>John Smith</h3>
              <span className="role">CEO & Founder</span>
              <p>Over 20 years of experience in the automotive industry.</p>
              <span className="email">john.smith@cardealership.com</span>
            </div>
            <div className="team-card">
              <div className="team-img" style={{backgroundImage: "url('https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=200&h=200&fit=crop&crop=face')"}}></div>
              <h3>Sarah Johnson</h3>
              <span className="role">Sales Director</span>
              <p>Leading our sales team with passion and integrity.</p>
              <span className="email">sarah.johnson@cardealership.com</span>
            </div>
            <div className="team-card">
              <div className="team-img" style={{backgroundImage: "url('https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=200&h=200&fit=crop&crop=face')"}}></div>
              <h3>Michael Chen</h3>
              <span className="role">Finance Manager</span>
              <p>Expert in automotive financing solutions.</p>
              <span className="email">michael.chen@cardealership.com</span>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

function Contact() {
  return (
    <div>
      <section className="page-hero">
        <div className="hero-content">
          <h1>Contact Us</h1>
          <p>We'd love to hear from you</p>
        </div>
      </section>
      <section className="contact-section">
        <div className="container">
          <div className="contact-grid">
            <div className="contact-info">
              <h2>Get In Touch</h2>
              <div className="info-card">
                <i className="fas fa-map-marker-alt"></i>
                <div><h3>Visit Us</h3><p>1234 Auto Mall Drive, San Jose, CA 95110</p></div>
              </div>
              <div className="info-card">
                <i className="fas fa-phone-alt"></i>
                <div><h3>Call Us</h3><p>+1 (555) 123-4567</p></div>
              </div>
              <div className="info-card">
                <i className="fas fa-envelope"></i>
                <div><h3>Email Us</h3><p>info@cardealership.com</p></div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div className="App">
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dealer/:id" element={<DealerDetails />} />
          <Route path="/postreview/:id" element={<PostReview />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
