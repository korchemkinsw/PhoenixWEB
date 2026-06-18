import React, { useState, useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom"
import { GlobalStyle } from "./styles";
import ResponsePage from "/src/components/pages/response-team -page/response-team";
import CompanyListPage from "/src/components/pages/company-list-page/company-list";
import ResponseCardPage from "/src/components/pages/response-card-page/response-card";
import { company } from "/src/mocks/company-list";

export default function App() {
  return (
    <BrowserRouter >
      <GlobalStyle />
      <Routes >
        <Route path = "/response" element = { < ResponsePage />} />
        <Route path = "/response/:id" element = { < ResponsePage />} />
        <Route path = "/company" element = { < CompanyListPage /> } />
        <Route path = "/company/:id" element = { <ResponseCardPage  />} />
      </Routes> 
    </BrowserRouter>
  )
}
