--
SELECT 
  * 
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
  started_working = '7/24/2017' 
  and Hospital.h_id = Doctor.h_id
