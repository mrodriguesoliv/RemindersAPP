import React, { useEffect, useRef, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'; // Para navegação após login
import './LoginSignUp.css';

const Login = () => {
  const loginBtnRef = useRef(null);
  const signupBtnRef = useRef(null);
  const [username, setUsername] = useState(''); // Corrigindo a referência ao username
  const [password, setPassword] = useState(''); // Corrigindo a referência ao password
  const [error, setError] = useState(''); // Para exibir mensagens de erro
  const [token, setToken] = useState(''); // Estado para o token
  const navigate = useNavigate(); // Hook para navegação após o login
 
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


  const handleSignUp = async (e) => {
    e.preventDefault();

    if (!username || !password) {
        setError('Username and password are required.');
        return;
    }

    console.log('Signing up with:', { username, password }); 

    try {
        // Primeira requisição para o endpoint de signup
        await axios.post('http://127.0.0.1:8000/v1.0/signup/', {
            username: username,
            password: password,
        });

        // Chama o handleSignIn automaticamente após o signup bem-sucedido
        await handleSignIn(e);
    } catch (error) {
        setError('Signup failed. Please check your credentials.');
        console.error('Signup failed', error);  
    }
};


  const handleSignIn = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(`${apiUrl}v1.0/api/token/`, {
        username: username,
        password: password,
      });
      
      const token = response.data.token; // Altere 'accessToken' se necessário
      setToken(token);
      localStorage.setItem('accessToken', token); // Armazena o token no localStorage
      localStorage.setItem('username', username);
      navigate('/reminders.app/'); // Altere o caminho se necessário
    } catch (error) {
      setError('Login failed. Please check your credentials.'); // Exibe a mensagem de erro
      console.error('Login failed', error);
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
          onChange={(e) => {
            setUsername(e.target.value);
            console.log('Username:', e.target.value);
          }}/>
          <input 
          type="password" 
          className="input" 
          placeholder="password" 
          onChange={(e) => setPassword(e.target.value)}/>
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
              onChange={(e) => setUsername(e.target.value)} // Corrigindo o valor do input
            />
            <input
              type="password"
              className="input" 
              placeholder="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)} // Corrigindo o valor do input
            />
          </div>
          <button className="submit-btn" onClick={handleSignIn}>Sign in</button>
          {error && <p style={{ color: 'red' }}>{error}</p>} {/* Exibe erro se houver */}
        </div>
      </div>
    </div>
  );
};

export default Login;
