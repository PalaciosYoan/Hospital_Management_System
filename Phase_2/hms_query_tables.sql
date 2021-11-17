--
SELECT 
  name, address
FROM 
  Hospital;

--
SELECT 
  * 
FROM 
  Doctor 
WHERE 
  h_id = "18e0672b-e749-4965-b3f7-8bfda0aa23e5";

--
SELECT 
  Doctor.name 
FROM 
  Doctor, 
  Hospital 
WHERE 
  Doctor.h_id = Hospital.h_id 
  AND Hospital.name = "ELIZA COFFEE MEMORIAL HOSPITAL";

--
SELECT 
  Room.type 
FROM 
  Room, 
  Hospital 
WHERE 
  Room.h_id = Hospital.h_id 
  AND Hospital.name = "SOUTHEAST ALABAMA MEDICAL CENTER" 
  and Room.cost > 4000;

--
SELECT 
  name 
FROM 
  Hospital 
WHERE 
  address LIKE '%LOS ANGELES%';

--
SELECT 
  Hospital.name, 
  Doctor.name, 
  started_working 
FROM 
  Doctor, 
  Hospital 
WHERE 
  started_working > '2015-01-15' 
  and Hospital.h_id = Doctor.h_id;

--
SELECT 
  Patient.name, 
  Medication.name, 
  Medication.treament_for as Treatment_For 
FROM 
  Patient, 
  Medication, 
  Prescribed_Med 
WHERE 
  Patient.p_id = Prescribed_Med.p_id 
  and Medication.m_id = Prescribed_Med.m_id;

--
SELECT 
  DISTINCT Patient.name 
FROM 
  Patient, 
  Prescribed_Med 
WHERE 
  Patient.p_id not in (
    Select 
      p_id 
    from 
      Prescribed_Med
  );