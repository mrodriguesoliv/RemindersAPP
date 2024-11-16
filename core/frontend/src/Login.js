import React, { useEffect, useRef, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './LoginSignUp.css';

const Login = () => {
  const loginBtnRef = useRef(null);
  const signupBtnRef = useRef(null);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [token, setToken] = useState('');
  const navigate = useNavigate();

  const apiUrl = process.env.REACT_APP_API_URL;
  
  useEffect(() => {
    const loginBtn = loginBtnRef.current;
    const signupBtn = signupBtnRef.current;

    const handleLoginClick = (e) => {
      let parent = e.target.parentNode.parentNode;
      const isSlideUp = Array.from(parent.classList).includes("slide-up");

      if (!isSlideUp) {
        parent.classList.add('slide-up');
      } else {
        signupBtn.parentNode.classList.add('slide-up');
        parent.classList.remove('slide-up');
      }
    };
  
    const handleSignupClick = (e) => {
      let parent = e.target.parentNode;
      const isSlideUp = Array.from(parent.classList).includes("slide-up");

      if (!isSlideUp) {
        parent.classList.add('slide-up');
      } else {
        loginBtn.parentNode.parentNode.classList.add('slide-up');
        parent.classList.remove('slide-up');
      }
    };

    loginBtn.addEventListener('click', handleLoginClick);
    signupBtn.addEventListener('click', handleSignupClick);

    return () => {
      loginBtn.removeEventListener('click', handleLoginClick);
      signupBtn.removeEventListener('click', handleSignupClick);
    };
  }, []);

  const handleKeyPressSignUp = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      handleSignUp(e);
    }
  };

  const handleKeyPressSignIn = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      handleSignIn(e);
    }
  };

  const getCSRFToken = () => {
    const match = document.cookie.match(new RegExp('(^| )csrftoken=([^;]+)'));
    return match ? match[2] : '';
  };
  
  const handleSignUp = async (e) => {
    e.preventDefault();

    if (!username || !password) {
        setError('Username and password are required.');
        return;
    }

    try {
     
        const csrfToken = getCSRFToken();

        if (!csrfToken) {
            setError('CSRF token not found.');
            return;
        }

        await axios.post(
            `${apiUrl}v1.0/signup/`,
            { username, password },
            {
                headers: {
                    'X-CSRFToken': csrfToken,
                },
            }
        );

        await handleSignIn(e);
    } catch (error) {
        setError('Signup failed. Please check your credentials.');
        console.error('Signup failed', error);  
    }
  };

  const handleSignIn = async (e) => {
    e.preventDefault();
    
    try {
  
      const csrfToken = getCSRFToken();

      if (!csrfToken) {
          console.error('CSRF token not found.');
          return;
      }

      const response = await axios.post(
          `${apiUrl}v1.0/api/token/`,
          {
              username: username,
              password: password,
          },
          {
              headers: {
                  'X-CSRFToken': csrfToken,
              },
          }
      );

      const { access_token } = response.data;

      localStorage.setItem('access_token', access_token);

      console.log('Login successful! Access token:', access_token);
  } catch (error) {
      console.error('Login error:', error.response?.data || error.message);
  }
};

  return (
    <div className="form-structor">
      <div className="signup">
        <h2 className="form-title" id="signup" ref={signupBtnRef}><span>or</span>Sign up</h2>
        <div className="form-holder">
          <input 
            type="text" 
            className="input" 
            placeholder="username" 
            onChange={(e) => setUsername(e.target.value)}
          />
          <input 
            type="password" 
            className="input" 
            placeholder="password" 
            onChange={(e) => setPassword(e.target.value)}
            onKeyUp={handleKeyPressSignUp}
          />
        </div>
        <button className="submit-btn" onClick={handleSignUp}>Sign up</button>
      </div>
      <div className="login slide-up">
        <div className="center">
          <h2 className="form-title" id="login" ref={loginBtnRef}><span>or</span>Sign in</h2>
          <div className="form-holder">
            <input
              type="text"
              className="input"
              placeholder="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <input
              type="password"
              className="input" 
              placeholder="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              onKeyUp={handleKeyPressSignIn}
            />
          </div>
          <button className="submit-btn" onClick={handleSignIn}>Sign in</button>
          {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
      </div>
    </div>
  );
};

export default Login;
