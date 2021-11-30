import React from "react";
import "./styles.css";
import Card from "./components/hospitals";
import Info from "./components/hospital_info";
import { Route, Routes, BrowserRouter as Router } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Card />} />
        <Route path="/info" element={<Info />} />
      </Routes>
    </Router>
  );
}