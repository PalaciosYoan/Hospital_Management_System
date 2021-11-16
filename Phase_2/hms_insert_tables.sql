--
INSERT INTO Hospital(h_id, address, name) 
VALUES 
  (
    "0bb2f9d2-ecd4-4ad7-98b6-d0571c728e3a", 
    "7277 Market Ave. Soddy Daisy, TN 37379", 
    "BOLIVAR MEDICAL CENTER"
  );
INSERT INTO Hospital(h_id, address, name) 
VALUES 
  (
    "3b5a7cde-7377-4590-a0d8-431ec91b1a00", 
    "499 Fairfield Lane Port Orange, FL 32127", 
    "MERIT HEALTH WESLEY"
  );
INSERT INTO Hospital(h_id, address, name) 
VALUES 
  (
    "f336f51f-6216-4b08-a0f1-f23bd860dd39", 
    "14 East Oxford Lane Beckley, WV 25801", 
    "BENEFIS TETON MEDICAL CENTER"
  );
INSERT INTO Hospital(h_id, address, name) 
VALUES 
  (
    "0cb321dd-472a-474e-84ab-44a8c8dada4c", 
    "911 Woodland Street Schererville, IN 46375", 
    "BAPTIST MEM HOSP/ GOLDEN TRIANGLE INC"
  );
INSERT INTO Hospital(h_id, address, name) 
VALUES 
  (
    "08ff82be-3ec7-4df0-b1eb-6cd9debbb045", 
    "8181 Iroquois Street Unit 78 Bonita Springs, FL 34135", 
    "METHODIST HEALTHCARE - OLIVE BRANCH HOSPITAL"
  );
INSERT INTO Hospital(h_id, address, name) 
VALUES 
  (
    "8644e1e7-c1cd-4d06-a341-de7ff8d10d15", 
    "7878 Ridgeview Ave. Massillon, OH 44646", 
    "QUITMAN COUNTY HOSPITAL CAH"
  );
INSERT INTO Hospital(h_id, address, name) 
VALUES 
  (
    "5ea136bc-a263-44cf-83f7-8ce473526164", 
    "73 Oak Ave. Eastlake, OH 44095", 
    "SHELBY BAPTIST MEDICAL CENTER"
  );
INSERT INTO Hospital(h_id, address, name) 
VALUES 
  (
    "73b2e004-7096-4be4-81e5-e6c0c38e214f", 
    "947 Primrose Road Hobart, IN 46342", 
    "GREENE COUNTY HOSPITAL CAH"
  );
INSERT INTO Hospital(h_id, address, name) 
VALUES 
  (
    "2a502f14-7102-4aa1-8544-75ce9120f319", 
    "14 Harvard St. Griffin, GA 30223", 
    "TWIN RIVERS REGIONAL MEDICAL CENTER"
  );

--
INSERT INTO Doctor(
  d_id, name, started_working, phone_number, 
  h_id
) 
VALUES 
  (
    "9a41e1d6-6a82-4dea-b399-92472277352c", 
    "Joe Rib", "11/14/2020", "3263096506", 
    "18e0672b-e749-4965-b3f7-8bfda0aa23e5"
  );
INSERT INTO Doctor(
  d_id, name, started_working, phone_number, 
  h_id
) 
VALUES 
  (
    "d4a5749f-4521-49a1-91e1-4d57d37c1f6d", 
    "Roger Jae", "11/14/2021", "4324556631", 
    "08ff82be-3ec7-4df0-b1eb-6cd9debbb045"
  );
