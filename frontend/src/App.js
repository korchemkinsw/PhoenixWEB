import React, {useState, useEffect} from "react";
import logo from './logo.svg';
import './App.css';
import { company } from "./mocks/company-list";
import CompanyListPage from "./components/pages/company-list-page/company-list";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
          <CompanyListPage company={company}/>
        </a>
      </header>
    </div>
  );
}

export default App;
