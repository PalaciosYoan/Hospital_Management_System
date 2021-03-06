CREATE TABLE IF NOT EXISTS Hospital(
    h_id CHAR(255) NOT NULL PRIMARY KEY,
    address CHAR(255) NOT NULL,
    name CHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Doctor(
    d_id CHAR(255) NOT NULL PRIMARY KEY,
    name CHAR(255) NOT NULL,
    started_working DATE NOT NULL,
    phone_number CHAR(255) NOT NULL,
    h_id CHAR(255) NOT NULL,
    FOREIGN KEY(h_id) REFERENCES Hospital(h_id)
);

CREATE TABLE IF NOT EXISTS Maintenance(
    maint_id CHAR(255) NOT NULL PRIMARY KEY,
    name CHAR(255) NOT NULL,
    started_working DATE NOT NULL,
    duty CHAR(255) NOT NULL,
    phone_number INT NULL

);

CREATE TABLE IF NOT EXISTS Hospital_Maintenance_Junction_Table(
    h_id CHAR(255) NOT NULL,
    maint_id CHAR(255) NOT NULL,
    FOREIGN KEY(h_id) REFERENCES Hospital(h_id),
    FOREIGN KEY(maint_id) REFERENCES Maintenance(maint_id)
);

CREATE TABLE IF NOT EXISTS Medication(
    m_id CHAR(255) NOT NULL PRIMARY KEY,
    cost DECIMAL(8, 2) NOT NULL,
    name CHAR(255) NOT NULL,
    type CHAR(255) NOT NULL,
    side_effect CHAR(255) NOT NULL,
    h_id CHAR(255) NOT NULL,
    treament_for CHAR(255) NOT NULL,
    FOREIGN KEY(h_id) REFERENCES Hospital(h_id)
);

CREATE TABLE IF NOT EXISTS Nurse(
    n_id CHAR(255) NOT NULL PRIMARY KEY,
    started_working DATE NOT NULL,
    name CHAR(255) NOT NULL,
    h_id CHAR(255) NOT NULL,
    FOREIGN KEY(h_id) REFERENCES Hospital(h_id)
);

CREATE TABLE IF NOT EXISTS Patient(
    p_id CHAR(255) NOT NULL PRIMARY KEY,
    dob DATE NOT NULL,
    admit_date DATE NOT NULL,
    released_date DATE NULL,
    problem CHAR(255) NOT NULL,
    address CHAR(255) NOT NULL,
    name CHAR(255) NOT NULL,
    phone_number CHAR(255) NOT NULL,
    h_id CHAR(255) NOT NULL,
    d_id CHAR(255) NOT NULL,
    r_id CHAR(255) NOT NULL,
    FOREIGN KEY(h_id) REFERENCES Hospital(h_id),
    FOREIGN KEY(d_id) REFERENCES Doctor(d_id),
    FOREIGN KEY(r_id) REFERENCES Room(r_id)
);

CREATE TABLE IF NOT EXISTS Room(
    r_id CHAR(255) NOT NULL PRIMARY KEY,
    room_number INT NOT NULL,
    person_allowed INT NOT NULL,
    cost DECIMAL(8, 2) NOT NULL,
    type CHAR(255) NOT NULL,
    h_id CHAR(255) NOT NULL,
    p_id CHAR(255) NULL,
    FOREIGN KEY(h_id) REFERENCES Hospital(h_id),
    FOREIGN KEY(p_id) REFERENCES Patient(p_id)
);

CREATE TABLE IF NOT EXISTS Nurse_Room_Junction_Table(
    r_id CHAR(255) NOT NULL,
    n_id CHAR(255) NOT NULL,
    FOREIGN KEY(r_id) REFERENCES Room(r_id),
    FOREIGN KEY(n_id) REFERENCES Nurse(n_id)

);

CREATE TABLE IF NOT EXISTS Prescribed_Med(
    pmed_id CHAR(255) NOT NULL PRIMARY KEY,
    assigned_date DATE NOT NULL,
    p_id CHAR(255) NOT NULL,
    m_id CHAR(255) NOT NULL,
    FOREIGN KEY(p_id) REFERENCES Patient(p_id),
    FOREIGN KEY(m_id) REFERENCES Medication(m_id)
);