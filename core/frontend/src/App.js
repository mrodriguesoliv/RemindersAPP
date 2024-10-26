// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate} from 'react-router-dom';
import ReminderTable from './ReminderTable';
import Login from './Login';

function RemindersAPP() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Navigate to="/reminders.app" />} />
          <Route path="/reminders.login" element={<Login/>} />
          <Route path="/reminders.app" element={<ReminderTable/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default RemindersAPP;
