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