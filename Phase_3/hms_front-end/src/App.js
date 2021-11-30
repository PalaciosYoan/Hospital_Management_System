import React from "react";
import "./styles.css";
import Card from "./components/hospitals";
import Info from "./components/hospital_info";
import Doctor from "./components/get_hInfo/doctor"
import Doctor_Patient from "./components/get_hInfo/doctor_patient"
import { Route, Routes, BrowserRouter as Router } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Card />} />
        <Route path="/info" element={<Info />} />
        <Route path="/doctor" element={<Doctor />} />
        <Route path="/doctor_patient" element={<Doctor_Patient />} />
      </Routes>
    </Router>
  );
}