CREATE TABLE Hospital(
    h_id INT UNSIGNED NOT NULL PRIMARY KEY,
    address CHAR(255) NOT NULL,
    name CHAR(255) NOT NULL
);

CREATE TABLE Doctor(
    d_id INT UNSIGNED NOT NULL PRIMARY KEY,
    name CHAR(255) NOT NULL,
    started_working DATE NOT NULL,
    phone_number CHAR(255) NOT NULL,
    h_id INT NOT NULL,
    FOREIGN KEY(h_id) REFERENCES Hospital(h_id)
);

CREATE TABLE Maintenance(
    maint_id INT UNSIGNED NOT NULL PRIMARY KEY,
    name CHAR(255) NOT NULL,
    started_working DATE NOT NULL,
    duty CHAR(255) NOT NULL
);

CREATE TABLE `Hospital-Maintenance Junction Table`(
    h_id INT UNSIGNED NOT NULL,
    maint_id INT UNSIGNED NOT NULL,
    FOREIGN KEY(h_id) REFERENCES Hospital(h_id),
    FOREIGN KEY(maint_id) REFERENCES Maintenance(maint_id)
);

CREATE TABLE Medication(
    m_id INT NOT NULL PRIMARY KEY,
    cost DECIMAL(8, 2) NOT NULL,
    name CHAR(255) NOT NULL,
    type CHAR(255) NOT NULL,
    side_effect CHAR(255) NOT NULL,
    h_id INT NOT NULL,
    FOREIGN KEY(h_id) REFERENCES Hospital(h_id)
);
CREATE TABLE Nurse(
    n_id INT UNSIGNED NOT NULL PRIMARY KEY,
    started_working DATE NOT NULL,
    name CHAR(255) NOT NULL,
    h_id INT NOT NULL,
    FOREIGN KEY(h_id) REFERENCES Hospital(h_id)
);

CREATE TABLE room(
    r_id INT UNSIGNED NOT NULL PRIMARY KEY,
    room_number INT NOT NULL,
    person_allowed INT NOT NULL,
    cost DECIMAL(8, 2) NOT NULL,
    type CHAR(255) NOT NULL,
    h_id INT NOT NULL,
    FOREIGN KEY(h_id) REFERENCES Hospital(h_id)
);

CREATE TABLE `Nurse-Room Junction Table`(
    r_id INT UNSIGNED NOT NULL,
    n_id INT UNSIGNED NOT NULL,
    FOREIGN KEY(r_id) REFERENCES room(r_id),
    FOREIGN KEY(n_id) REFERENCES Nurse(n_id)

);
CREATE TABLE Patient(
    p_id INT UNSIGNED NOT NULL PRIMARY KEY,
    dob DATE NOT NULL,
    admit_date DATE NOT NULL,
    released_date DATE NOT NULL,
    problem CHAR(255) NOT NULL,
    address CHAR(255) NOT NULL,
    name CHAR(255) NOT NULL,
    phone_number CHAR(255) NOT NULL,
    h_id INT NOT NULL,
    d_id INT NOT NULL,
    FOREIGN KEY(h_id) REFERENCES Hospital(h_id),
    FOREIGN KEY(d_id) REFERENCES Doctor(d_id)
);

CREATE TABLE `Prescribed Med`(
    pmed_id INT UNSIGNED NOT NULL PRIMARY KEY,
    assigned_date DATE NOT NULL,
    p_id INT NOT NULL,
    m_id INT NOT NULL,
    FOREIGN KEY(p_id) REFERENCES Patient(p_id),
    FOREIGN KEY(m_id) REFERENCES Medication(m_id)
);