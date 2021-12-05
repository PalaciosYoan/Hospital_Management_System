import React from "react";
import "./styles.css";
import Card from "./components/hospitals";
import Info from "./components/get_hInfo/hospital_info";
import Doctor from "./components/get_hInfo/doctor";
import Doctor_Patient from "./components/get_hInfo/doctor_patient";
import Single_Patient from "./components/get_hInfo/single_patient";
import Patient from './components/get_hInfo/patient';
import Room from "./components/get_hInfo/room";
import Nurse from "./components/get_hInfo/nurse";
import Medicine from "./components/get_hInfo/medicine";
import Maintenance from "./components/get_hInfo/maintenance";
import Nurse_Room from "./components/get_hInfo/nurse_room";
import Hospital_Maintenance from "./components/get_hInfo/hospital_maintenance";
import Patient_Medication from "./components/get_hInfo/patient_medication";
import Nurse_Room_Menu from "./components/get_hInfo/nurse_room_menu";
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
        <Route path="/nurse" element={<Nurse />} />
        <Route path="/medicine" element={<Medicine />} />
        <Route path="/maintenance" element={<Maintenance />} />
        <Route path="/nurse_room" element={<Nurse_Room />} />
        <Route path="/hospital_maintenance" element={<Hospital_Maintenance />} />
        <Route path="/patient_medication" element={<Patient_Medication />} />
        <Route path="/nurse_room_menu" element={<Nurse_Room_Menu />} />

      </Routes>
    </Router>
  );
}