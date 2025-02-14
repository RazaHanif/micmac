import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom"
import MainPage from "./pages/MainPage.jsx"
import UserPage from "./pages/UserPage.jsx"
import ProfilePage from "./pages/ProfilePage.jsx"
import ExplorePage from "./pages/ExplorePage.jsx"
import LoginPage from "./pages/LoginPage.jsx"
import './pages/LoginPage.css'
import RegisterPage from "./pages/RegisterPage.jsx"

// I gotta figure out how to use the django log in and auth stuff from the templates.

function App() {

  document.title = "Brick"
  const icon = document.querySelector("link[rel='icon']")
  icon.href = "https://cdn.jsdelivr.net/npm/twemoji@11.3.0/2/svg/1f9f1.svg"
  
  return (
    <Router>
      <div className="main">
        <nav className="nav-bar">
          <div className="nav-icon"><Link className="icon" to="/">&#128230;</Link></div>
          <div className="page-links">
            <div><Link to="/profile">Profile</Link></div>
            <div><Link to="/explore">Explore</Link></div>
          </div>
          <div className="user-icon">
            <div><Link to="/login">Log In</Link></div>
          </div>
        </nav>

        <div className="body">
          <Routes>
            <Route path="/" element={<MainPage/>}></Route>
            <Route path="profile" element={<ProfilePage/>}></Route>
            <Route path="explore" element={<ExplorePage/>}></Route>
            <Route path="login" element={<LoginPage/>}></Route>
            <Route path="register" element={<RegisterPage/>}></Route>
          </Routes>
        </div>
      </div>
    </Router>
  )
}

export default App
