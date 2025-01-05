import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

const Login = () => <h1>Login Page</h1>;
const Dashboard = () => <h1>Dashboard</h1>;

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </Router>
  );
};

export default App;
