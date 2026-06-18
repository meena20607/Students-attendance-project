import { useState } from "react";
import "./Login.css";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log({
      email,
      password,
    });
  };

  return (
    <div className="login-container">
      <div className="left-panel">
        <h1>🎓 Student Attendance Management</h1>
        <p>
          Track attendance, manage students, handle leave requests
          and monitor academic progress efficiently.
        </p>
      </div>

      <div className="login-card">
        <h2>Welcome Back</h2>
        <p>Sign in to continue</p>

        <form onSubmit={handleSubmit}>
          <input
            type="email"
            placeholder="Enter Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          <input
            type="password"
            placeholder="Enter Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

          <button type="submit">
            Login
          </button>
        </form>

        <div className="links">
          <a href="/register">Create Account</a>
        </div>
      </div>
    </div>
  );
}

export default Login;