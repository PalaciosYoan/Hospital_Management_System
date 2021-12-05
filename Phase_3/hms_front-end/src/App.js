import React from "react";
import "./styles.css";
import Hospital from "./components/get_hInfo/hospitals";
import Hospital_Info from "./components/get_hInfo/hospital_info";
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
import Room_Menu from "./components/get_hInfo/room_menu";
import Update_Hospital from "./components/update_hinfo/hospital";
import Update_Doctor from "./components/update_hinfo/doctor";
import Nurse_Room_Patient from "./components/get_hInfo/nurse_room_patient";
import Nurse_Room_Nurse from "./components/get_hInfo/nurse_room_nurse";
import { Route, Routes, BrowserRouter as Router } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Hospital />} />
        <Route path="/info" element={<Hospital_Info />} />
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
        <Route path="/room_menu" element={<Room_Menu />} />
        <Route path="/nurse_room_patient" element={<Nurse_Room_Patient />} />
        <Route path="/update_hospital" element={<Update_Hospital />} />
        <Route path="/update_doctor" element={<Update_Doctor />} />
        <Route path="/nurse_room_nurse" element={<Nurse_Room_Nurse />} />
      </Routes>
    </Router>
  );
}