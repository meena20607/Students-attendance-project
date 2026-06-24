import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";
import CourseManagement from "./pages/CourseManagement";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />

        <Route
          path="/register"
          element={<Register />}
        />

        <Route
          path="/courses"
          element={<CourseManagement />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;