-- inserting data into employee table
insert into employee
    (first_name, last_name, date_of_birth, email)
values
    ('arpit', 'kothari', '1999-02-20', 'arpit.k@student.ie.edu')

insert into employee
    (first_name, last_name, date_of_birth, email)
values
    ('ishan', 'juneja', '2001-05-01', 'ishan.juneja@student.ie.edu')

insert into employee
    (first_name, last_name, date_of_birth, email)
values
    ('Zarifa', 'Mammadli', '2003-09-16', 'zarifa.m@stduent.ie.edu')


-- adding values (item)
insert into item
    (category, sticker_number, item_issued_handedout, employee_id)
values
    ('laptop', 'HNDKS09', '2024-11-05', '2')

insert into item
    (category, sticker_number, item_issued_handedout, employee_id)
values
    ('laptop', 'HNDKS19', '2024-11-19', '1')

insert into item
    (category, sticker_number, item_issued_handedout, item_issued_handedin, employee_id)
values
    ('Phone', 'HNDKS20', '2024-11-23', '2024-11-24', '3')


-- inserting values to ticket table
insert into ticket
    (problem_description, ticket_num, employee_id_created, employee_id_assigned)
 values
    ('laptop broken', '2', '2', '1')
insert into ticket
    (problem_description,ticket_num,creation_date, completion_date,employee_id_created,employee_id_assigned)
 values
    ('item lost','1','2024-01-01','2024-01-02','1','2')


-- inseting values to office table 
insert into office
    (office_name, street_address, zip_code_address)
values 
    ('MMB31', 'Maria de Molina BIS, 31', '28008')
insert into office
    (office_name, street_address, zip_code_address)
values 
    ('MM31', 'Maria de Molina, 31', '28008')


-- inseting values to room table 
insert into room
    (room_num, room_type, office_id)
values 
    ('MMB503', 'Class room', '1')
insert into room
    (room_num, room_type, office_id)
values
    ('MM608', 'Study room', '1')


-- inserting values to officehasitem table 
insert into officehasitem
    (office_id, item_id)
values
    ('1', '3')


-- inserting values to itemassociatedroom table 
insert into itemassociatedroom
    (room_id, item_id)
values
    ('MM406', '10')
