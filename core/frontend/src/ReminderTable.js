import './index.css';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {Container, Spinner, Alert } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const ReminderTable = () => {
    const [reminders, setReminders] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [inputValue, setInputValue] = useState('');
    const [responseData] = useState('');
    const [username, setUsername] = useState('');

    const fetchReminders = async () => {
        try {
            const response = await axios.get('/reminders.app/');
            setReminders(response.data);
            setLoading(false);
        } catch (error) {
            console.error('Erro ao buscar dados:', error);
            setError(error);
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchReminders();
        const storedUsername = localStorage.getItem('username');
        setUsername(storedUsername || '');
    }, []);

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!inputValue) return;

        const token = localStorage.getItem('accessToken');

        try {
            await axios.post('/v1.0/conversation/', { message: inputValue, conversation_id: "1" }, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                }
            });
            await fetchReminders();
            setInputValue('');
        } catch (error) {
            console.error('Erro ao enviar mensagem:', error);
        }
    };

    const handleLogout = () => {
        localStorage.removeItem('accessToken');
        localStorage.removeItem('username');
        setUsername(''); 
    };

    const handleRowClick = async (reminder) => {
        const token = localStorage.getItem('accessToken'); 
        console.log('Evento clicado:', reminder.event);
    
        try {
            const response = await axios.post('/v1.0/conversation/detail', { 
                conversation_id: "1",
                message: `Me de um texto completo falando sobre o seguinte tema: ${reminder.event}`,
                
            }, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                },
            });
            
            console.log('Resposta da API:', response.data);


            const details = response.data.response;
            alert(details);
        } catch (error) {
            console.error('Erro ao buscar detalhes do evento:', error);
            alert('Erro ao buscar detalhes. Tente novamente mais tarde.');
        }
    };




    if (loading) return (
        <Container className="text-center mt-5">
            <Spinner animation="border" role="status">
                <span className="visually-hidden">Carregando...</span>
            </Spinner>
            <p className="mt-3">Carregando dados...</p>
        </Container>
    );

    if (error) return (
        <Container className="mt-5">
            <Alert variant="danger">
                <Alert.Heading>Erro ao carregar dados</Alert.Heading>
                <p>Ocorreu um erro ao tentar buscar os lembretes. Verifique a conexão com a API.</p>
            </Alert>
        </Container>
    );

    return (
        <div>
                <header className="header">
                    {username ? (
                        <>
                            <span className='header-item'>Bem-vindo, {username}!</span>
                            <Link to="/reminders.login" className='header-item' onClick={handleLogout}>Logout</Link>
                        </>
                    ) : (
                        <Link to="/reminders.login" className='header-item'>LOGIN</Link>
                    )}

                </header>
    
                <h1 className='title'>Just do it.</h1>
    
                <div className="navbar">
                    <form className="navbar-form" onSubmit={handleSubmit}>
                        <input className="navbar-input"
                            type="text"
                            value={inputValue}
                            onChange={handleInputChange}
                            placeholder="Type your message..."
                        />
                        <button type="submit" className="navbar-button">Reminder me!</button>
                    </form>
                    {responseData && <div className="response-message">{responseData}</div>}
                </div>
    
                <div>
                    <table className="reminder-table">
                        <thead>
                            <tr>
                                <th>Evento</th>
                                <th>Descrição</th>
                                <th>Local</th>
                            </tr>
                        </thead>

                        <tbody>
                            {reminders.length > 0 ? (
                                reminders.map((reminder, index) => (
                                    <tr key={index} onClick={() => handleRowClick(reminder)}>
                                        <td>{reminder.event}</td>
                                        <td>{reminder.description}</td>
                                        <td>{reminder.location}</td>
                                    </tr>
                                ))
                            ) : (
                                <tr>
                                    <td colSpan="3">Nenhum lembrete encontrado</td>
                                </tr>
                            )}
                        </tbody>
                    </table>
                </div>
                
                <tfoot className='footer'>
                    <footer>
                        <p>Ao enviar mensagens para o RemindersAPP, você aceita nossos <u>Termos</u> e declara ter lido nossa <u>Política de Privacidade</u>.</p>
                    </footer>
                </tfoot>

            </div>
    );
};    

export default ReminderTable;
