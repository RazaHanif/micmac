import Homepage from "./pages/Homepage"
import Profilepage from "./pages/Profilepage"
import Profiles from "./pages/Profiles"

import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom"

function App() {
  
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/profile">Profile</Link></li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<Homepage/>}></Route>
          <Route path="profile" element={<Profilepage/>}></Route>
        </Routes>
      </div>
    </Router>
  )
}

export default App
