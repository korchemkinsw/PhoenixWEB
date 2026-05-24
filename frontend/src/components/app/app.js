import React, {useState, useEffect} from "react";
import {BrowserRouter, Routes, Route} from "react-router-dom"
import { GlobalStyle } from "./styles";
import api from "/src/api";
import CompanyListPage from "/src/components/pages/company-list-page/company-list";
import { company } from "/src/mocks/company-list";

export default function App() {
  const [error, setError] = useState(null);
  const [companyList, setList] = useState([]);
  //useEffect(() => {api.getData(api.BackUrl.company, 'company', setList, setError)}, []);
  useEffect(() => {
    fetch('http://127.0.0.1:8000//phoenix/company')
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        setList(data);
      });
    }, [])

  return (
    <BrowserRouter>
      <GlobalStyle />
      <Routes>
        <Route path="/company" element={<CompanyListPage company={companyList} />} />
      </Routes>
    </BrowserRouter>
  )
}