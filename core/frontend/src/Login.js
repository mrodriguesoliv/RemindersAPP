import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios'; // Importando o axios
import {
  MDBBtn,
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBCard,
  MDBCardBody,
  MDBInput,
} from 'mdb-react-ui-kit';
import 'mdb-react-ui-kit/dist/css/mdb.min.css';

function App() {
  const [username, setUsername] = useState(''); // Estado para o username
  const [password, setPassword] = useState(''); // Estado para a password
  const [token, setToken] = useState(''); // Estado para o token
  const [error, setError] = useState(''); // Estado para mensagens de erro;


  const navigate = useNavigate(); // Inicializando useNavigate aqui




  const login = async () => {
    try {


      const response = await axios.post('http://127.0.0.1:8000/v1.0/api/token/', { username, password }); // URL da sua view Django
      console.log('Login bem-sucedido', response.data);
      
      
      const token = response.data.token; // Altere 'accessToken' se necessário
      setToken(token);
      localStorage.setItem('accessToken', token); // Armazena o token no localStorage
      localStorage.setItem('username', username);
      navigate('/reminders.app/'); // Altere o caminho se necessário

      
    } catch (err) {
      console.error('Erro ao fazer login:', err);
      setError("Credenciais Inválidas!");
      setToken(token);
      // Limpar os valores dos campos
      setUsername('');
      setPassword('');

    }
  };

  const handleKeyPress = (event) => { // Chama a função de login ao pressionar ENTER
    if (event.key === 'Enter') {
      event.preventDefault();
      login(); 
    }
  };



  return (
    <MDBContainer fluid>
      <MDBRow className='d-flex justify-content-center align-items-center h-100'>
        <MDBCol col='12'>
          <MDBCard className='bg-dark text-white my-5 mx-auto' style={{ borderRadius: '1rem', maxWidth: '400px' }}>
            <MDBCardBody className='p-5 d-flex flex-column align-items-center mx-auto w-100'>
              <h2 className="fw-bold mb-2 text-uppercase">Login</h2>
              {error && <p className="text-danger">{error}</p>}
              <MDBInput
                wrapperClass='mb-4 mx-5 w-100'
                labelClass='text-white'
                type='text'
                size="lg"
                placeholder='Type your user'
                value={username}
                onChange={(e) => setUsername(e.target.value)} 
                onKeyDown={handleKeyPress}
              />
              <MDBInput
                wrapperClass='mb-4 mx-5 w-100'
                labelClass='text-white'
                type='password'
                size="lg"
                placeholder='Type your password'
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                onKeyDown={handleKeyPress}
              />

              <p className="small mb-3 pb-lg-2"><a className="text-white-50" href="#!">Forgot password?</a></p>
              <MDBBtn outline className='mx-2 px-5' color='white' size='lg' onClick={login}>
                LOGIN
              </MDBBtn>

              <div>
                <p className="mb-0">Don't have an account? <a href="#!" className="text-white-50 fw-bold">Sign Up</a></p>
              </div>
            </MDBCardBody>
          </MDBCard>
        </MDBCol>
      </MDBRow>
    </MDBContainer>
  );
}

export default App;
