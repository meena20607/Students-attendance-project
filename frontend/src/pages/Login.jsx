import { useState } from "react";
import axios from "axios";
import "./Login.css";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/api/auth/admin/login",
        {
          email,
          password,
        }
      );

      localStorage.setItem(
        "token",
        response.data.token
      );

      setMessage("✅ Login Successful");

setTimeout(() => {
  window.location.href = "/courses";
}, 1000);

      console.log("Token:", response.data.token);

      // Later we will redirect to dashboard
      // window.location.href = "/dashboard";

    } catch (error) {
      console.error(error);
      setMessage("❌ Invalid Email or Password");
    }
  };

  return (
    <div className="login-container">
      <div className="left-panel">
        <h1>🎓 Student Attendance Management</h1>

        <p>
          Track attendance, manage students,
          handle leave requests and monitor
          academic progress efficiently.
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
            onChange={(e) =>
              setEmail(e.target.value)
            }
            required
          />

          <input
            type="password"
            placeholder="Enter Password"
            value={password}
            onChange={(e) =>
              setPassword(e.target.value)
            }
            required
          />

          <button type="submit">
            Login
          </button>
        </form>

        {message && (
          <p
            style={{
              marginTop: "15px",
              textAlign: "center",
              fontWeight: "bold",
            }}
          >
            {message}
          </p>
        )}

        <div className="links">
          <a href="/register">
            Create Account
          </a>
        </div>
      </div>
    </div>
  );
}

export default Login;