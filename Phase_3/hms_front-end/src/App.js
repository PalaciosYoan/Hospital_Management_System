import React from "react";
import "./styles.css";
import Card from "./components/hospitals";
import Info from "./components/get_hInfo/hospital_info";
import Doctor from "./components/get_hInfo/doctor"
import Doctor_Patient from "./components/get_hInfo/doctor_patient"
import Single_Patient from "./components/get_hInfo/single_patient"
import Patient from './components/get_hInfo/patient'
import Room from "./components/get_hInfo/room"
import { Route, Routes, BrowserRouter as Router } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Card />} />
        <Route path="/info" element={<Info />} />
        <Route path="/doctor" element={<Doctor />} />
        <Route path="/doctor_patient" element={<Doctor_Patient />} />
        <Route path="/single_patient" element={<Single_Patient />} />
        <Route path="/patient" element={<Patient />} />
        <Route path="/room" element={<Room />} />
      </Routes>
    </Router>
  );
}