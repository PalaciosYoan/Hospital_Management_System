select Room.room_number, Room.person_allowed, Room.cost, Room.type
from Room,
    (
    select *
    from 
        Nurse_Room_Junction_Table,
            (
                select n_id as nurse_id
                from Nurse
                where name = "charlotte Levi"
            ) nur
    where Nurse_Room_Junction_Table.n_id = nur.nurse_id
    ) t1
where t1.r_id = Room.r_id;


select Room.room_number, Room.person_allowed, Room.cost, Room.type
                from Room,
                (
                    select *
                    from 
                        Nurse_Room_Junction_Table t1,
                        (
                            select n_id as nurse_id
                            from Nurse
                            where name = "Olivia Liam"
                        )
                    where n_id = nurse_id
                ) t1
                where t1.r_id = Room.r_id;



select 
    p.dob, p.admit_date, p.problem, p.address, p.name, p.phone_number
from Patient p,
(
    select p_id
    from Prescribed_Med,
    (
        select m_id
        from Medication,
        (
            select h_id
            from Hospital
            where name = "CALLAHAN EYE HOSPITAL"
        ) h1
        where
            Medication.name = "Cephalosporins" and h1.h_id = Medication.h_id ) t1
    where
        t1.m_id = Prescribed_Med.m_id
) m1
where
    p.p_id = m1.p_id;


select *
from Patient, 
    (select p_id 
    from Room,
        (
            select h_id
            from Hospital
            where name = "CALLAHAN EYE HOSPITAL"
        ) h1
    where Room.h_id = h1.h_id and room.room_number = 2
    ) t2
where Patient.p_id = t2.p_id;

select Room.p_id
from Room, Nurse_Room_Junction_Table t1
where 
    Room.p_id;

select Room.r_id
from Room, Nurse_Room_Junction_Table t1
where 
    Room.p_id and t1.r_id = Room.r_id;



select Nurse.name, Nurse.started_working
from Nurse, 
    (select Nurse_Room_Junction_Table.n_id 
    from Nurse_Room_Junction_Table,
        (
            select r_id
            from Room,
            (
                select h_id
                from Hospital
                where
                    name = "SOUTHEAST ALABAMA MEDICAL CENTER"
            )h1
            where room_number = 18 and h1.h_id = Room.h_id
        ) h1
    where Nurse_Room_Junction_Table.r_id = h1.r_id 
    ) t2
where Nurse.n_id = t2.n_id;



select name, cost, type, side_effect, treament_for,  assigned_date
from Medication,
        ( select assigned_date, m_id as med_id
            from Prescribed_Med,
            (
                select p_id
                from Patient
                where name = "Alejandro Hernandez" and dob = "None"
                ) p1
            where p1.p_id = Prescribed_Med.p_id
        ) h1
where Medication.m_id=h1.med_id;




select *
from Room, Hospital
where
    Room.p_id = 'nan' AND
    Room.h_id = Hospital.h_id and
    Hospital.name = "MARSHALL MEDICAL CENTER SOUTH";