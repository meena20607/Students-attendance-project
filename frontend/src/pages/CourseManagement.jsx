import { useEffect, useState } from "react";
import axios from "axios";
import "./CourseManagement.css";

function CourseManagement() {
  const [courseName, setCourseName] = useState("");
  const [courseCode, setCourseCode] = useState("");
  const [description, setDescription] = useState("");
  const [courses, setCourses] = useState([]);

  const fetchCourses = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:5000/api/courses/"
      );
      setCourses(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    fetchCourses();
  }, []);

  const addCourse = async (e) => {
    e.preventDefault();

    try {
      await axios.post(
        "http://127.0.0.1:5000/api/courses/",
        {
          course_name: courseName,
          course_code: courseCode,
          description: description,
        }
      );

      setCourseName("");
      setCourseCode("");
      setDescription("");

      fetchCourses();
    } catch (error) {
      console.error(error);
    }
  };

  const deleteCourse = async (id) => {
    try {
      await axios.delete(
        `http://127.0.0.1:5000/api/courses/${id}`
      );

      fetchCourses();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="course-page">
      <h1 className="page-title">
        📚 Course Management
      </h1>

      <form
        className="course-form"
        onSubmit={addCourse}
      >
        <input
          type="text"
          placeholder="Course Name"
          value={courseName}
          onChange={(e) =>
            setCourseName(e.target.value)
          }
          required
        />

        <input
          type="text"
          placeholder="Course Code"
          value={courseCode}
          onChange={(e) =>
            setCourseCode(e.target.value)
          }
          required
        />

        <input
          type="text"
          placeholder="Description"
          value={description}
          onChange={(e) =>
            setDescription(e.target.value)
          }
        />

        <button
          className="add-btn"
          type="submit"
        >
          Add Course
        </button>
      </form>

      <div className="table-container">
        <h2>All Courses</h2>

        <table className="course-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Course Name</th>
              <th>Course Code</th>
              <th>Description</th>
              <th>Action</th>
            </tr>
          </thead>

          <tbody>
            {courses.map((course) => (
              <tr key={course.id}>
                <td>{course.id}</td>
                <td>{course.course_name}</td>
                <td>{course.course_code}</td>
                <td>{course.description}</td>

                <td>
                  <button
                    className="delete-btn"
                    onClick={() =>
                      deleteCourse(course.id)
                    }
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>

        </table>
      </div>
    </div>
  );
}

export default CourseManagement;