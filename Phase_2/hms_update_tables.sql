--
UPDATE 
  Hospital 
SET 
  name = 'SOUTHEAST ALABAMA MEDICAL CENTER' 
WHERE 
  Hospital.name = 'SOUTHEAST ALABAMA MEDICAL CENTERRRRRRRRR';

--
UPDATE 
  Medication 
SET 
  cost = 300 
WHERE 
  Medication.m_id = (
    SELECT 
      Medication.m_id 
    FROM 
      Medication, 
      Hospital 
    where 
      Hospital.name = 'SOUTHEAST ALABAMA MEDICAL CENTER' 
      and Hospital.h_id = Medication.h_id 
      and Medication.name = 'insulin'
  );

--
UPDATE 
  Patient 
SET 
  dob = '2017-10-13 00:00:00' 
WHERE 
  Patient.h_id = (
    SELECT 
      Hospital.h_id 
    FROM 
      Hospital, 
      Patient 
    where 
      Hospital.name = 'CALLAHAN EYE HOSPITAL' 
      and Hospital.h_id = Patient.h_id 
      and Patient.name = 'Alejandro Hernandez'
  );