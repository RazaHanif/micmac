import React from "react"
import StopWatch from "./StopWatch"

function App() {
  document.title = "StopWatch"
  const icon = document.querySelector("link[rel='icon']")
  icon.href = "https://cdn-icons-png.flaticon.com/512/595/595513.png"


  return (
    <StopWatch/>
  )
}

export default App
