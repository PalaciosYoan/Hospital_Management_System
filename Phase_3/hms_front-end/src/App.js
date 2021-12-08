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
import Update_Hospital from "./components/update_hInfo/hospital";
import Update_Doctor from "./components/update_hInfo/doctor";
import Update_Nurse from "./components/update_hInfo/nurse";
import Update_Medicine from "./components/update_hInfo/medicine";
import Update_Room from "./components/update_hInfo/room";
import All_Maintenance from "./components/get_hInfo/all_maintenance";
import Update_All_Maintenance from "./components/update_hInfo/all_maintenance";
import Update_Patient from "./components/update_hInfo/patient";


import Nurse_Room_Patient from "./components/get_hInfo/nurse_room_patient";
import Nurse_Room_Nurse from "./components/get_hInfo/nurse_room_nurse";
import Room_Menu_Patient from "./components/get_hInfo/room_menu_patient";
import Room_Menu_Nurse from "./components/get_hInfo/room_menu_nurse";
import Medicine_Patient from "./components/get_hInfo/medicine_patient";
import Insert_Hospital from "./components/insert_hInfo/hospital";
import Insert_Maintenance from "./components/insert_hInfo/maintenance";
import Insert_Maintenance_Menu from "./components/insert_hInfo/maintenance_menu";
import Insert_Medicine from "./components/insert_hInfo/medicine";
import Insert_Nurse from "./components/insert_hInfo/nurse";
import Insert_Patient from "./components/insert_hInfo/patient";
import Insert_Room from "./components/insert_hInfo/room";
import Insert_Doctor from "./components/insert_hInfo/doctor";
import Insert_Nurse_Room from "./components/insert_hInfo/nurse_room";

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
        <Route path="/room_menu_patient" element={<Room_Menu_Patient />} />
        <Route path="/room_menu_nurse" element={<Room_Menu_Nurse />} />
        <Route path="/medicine_patient" element={<Medicine_Patient />} />
        <Route path="/insert_hospital" element={<Insert_Hospital />} />
        <Route path="/insert_maintenance" element={<Insert_Maintenance />} />
        <Route path="/insert_maintenance_menu" element={<Insert_Maintenance_Menu />} />
        <Route path="/insert_medicine" element={<Insert_Medicine />} />
        <Route path="/insert_nurse" element={<Insert_Nurse />} />
        <Route path="/insert_patient" element={<Insert_Patient />} />
        <Route path="/insert_room" element={<Insert_Room />} />
        <Route path="/insert_doctor" element={<Insert_Doctor />} />
        <Route path="/update_nurse" element={<Update_Nurse />} />
        <Route path="/update_medicine" element={<Update_Medicine />} />
        <Route path="/update_room" element={<Update_Room />} />
        <Route path="/all_maintenance" element={<All_Maintenance />} />
        <Route path="/update_all_maintenance" element={<Update_All_Maintenance />} />
        <Route path="/update_patient" element={<Update_Patient />} />
        <Route path="/insert_nurse_room" element={<Insert_Nurse_Room />} />
      </Routes>
    </Router>
  );
}