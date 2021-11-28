--
DELETE FROM 
  Hospital 
WHERE 
  h_id = '0bb2f9d2-ecd4-4ad7-98b6-d0571c728e3a';
DELETE FROM 
  Hospital 
WHERE 
  h_id = '3b5a7cde-7377-4590-a0d8-431ec91b1a00';
DELETE FROM 
  Hospital 
WHERE 
  h_id = 'f336f51f-6216-4b08-a0f1-f23bd860dd39';
DELETE FROM 
  Hospital 
WHERE 
  h_id = '0cb321dd-472a-474e-84ab-44a8c8dada4c';
DELETE FROM 
  Hospital 
WHERE 
  h_id = '08ff82be-3ec7-4df0-b1eb-6cd9debbb045';
DELETE FROM 
  Hospital 
WHERE 
  h_id = '8644e1e7-c1cd-4d06-a341-de7ff8d10d15';
DELETE FROM 
  Hospital 
WHERE 
  h_id = '5ea136bc-a263-44cf-83f7-8ce473526164';
DELETE FROM 
  Hospital 
WHERE 
  h_id = '73b2e004-7096-4be4-81e5-e6c0c38e214f';
DELETE FROM 
  Hospital 
WHERE 
  h_id = '2a502f14-7102-4aa1-8544-75ce9120f319';

--
DELETE FROM 
  Doctor 
WHERE 
  Doctor.h_id = (
    SELECT 
      Doctor.h_id 
    FROM 
      Hospital, 
      Doctor 
    where 
      Hospital.name = 'ELIZA COFFEE MEMORIAL HOSPITAL' 
      and Hospital.h_id = Doctor.h_id 
      and Doctor.name = 'Joe Rib'
  );

--
DELETE FROM 
  Medication 
WHERE 
  Medication.m_id = (
    select 
      m_id 
    from 
      Medication, 
      Hospital 
    where 
      Hospital.name = 'SOUTHEAST ALABAMA MEDICAL CENTER' 
      and Hospital.h_id = Medication.h_id 
      and cost < 200
  );

--
Delete FROM 
  Room 
where 
  r_id in (
    Select 
      r_id 
    from 
      Room 
    where 
      p_id = 'nan'
  );

--'everyone who has been released
DELETE FROM 
  Patient 
WHERE 
  p_id NOT IN (
    SELECT 
      p_id 
    FROM 
      Patient 
    WHERE 
      released_date = ''
  )