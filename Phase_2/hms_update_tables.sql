--
UPDATE 
  Hospital 
SET 
  name = 'SOUTHEAST ALABAMA MEDICAL CENTER LTD' 
WHERE 
  Hospital.name = 'SOUTHEAST ALABAMA MEDICAL CENTER';

--
UPDATE 
  Medication 
SET 
  cost = 300 
WHERE 
  Medication.m_id IN (
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
  Patient.h_id IN (
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

--
UPDATE 
  Room 
SET 
  cost = Room.cost + (Room.cost * .10)
WHERE 
  Room.r_id IN (
    SELECT 
      Room.r_id
    FROM 
      Hospital, 
      Room 
    where 
      Hospital.name like '%CENTER%' 
      and Hospital.h_id = Room.h_id
  );

--
UPDATE 
  Medication 
SET 
  type = 'NOT-SELLING'
WHERE 
  Medication.m_id IN (
    SELECT 
     Medication.m_id
    FROM 
      Medication
    where 
     Medication.type = 'HORMONES'
  ); 