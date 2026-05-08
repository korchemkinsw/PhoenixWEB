import React, {useState, useEffect} from "react";
import {BrowserRouter, Routes, Route} from "react-router-dom"
import { GlobalStyle } from "./styles";
import api from "/src/api";
import CompanyListPage from "/src/components/pages/company-list-page/company-list";
import { company } from "/src/mocks/company-list";

export default function App() {
  const [error, setError] = useState(null);
  const [companyList, setList] = useState([]);
  const [panelsList, setPanels] = useState([]);
  useEffect(() => {api.getData(api.BackUrl.company, 'company', setList, setError)});
  return (
    <BrowserRouter>
      <GlobalStyle />
      <Routes>
        <Route path="/company" element={<CompanyListPage company={companyList} />} />
      </Routes>
    </BrowserRouter>
  )
}