import React, {useState} from 'react'
import Button from '@material-ui/core/Button';
import Navbar from './components/Navbar'
import './App.css';


function App() {
  const [insult, setInsult] = useState("Click The Button!")

  const newInsult = () => {
    fetch("https://cors-anywhere.herokuapp.com/http://qtcoder.pythonanywhere.com/randominsult")
      .then(res => res.json())
      .then(data => setInsult(data.insult))
  }

  return (
    <div className="App">
      <Navbar/>
      <h1 id="title">Insult Generator</h1>
      <div className="insultContainer">
        <h2>{ insult }</h2>
        <Button variant="contained" color="primary" onClick={newInsult} style={{background:'linear-gradient(45deg, #2193b0 30%, #6dd5ed 90%)'}}>
          New Insult
        </Button>
      </div>
    </div>
  );
}

export default App;
