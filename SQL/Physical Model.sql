-- employee table 
create table employee (
    ID serial primary key, 
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    date_of_birth date not null,
    email varchar(50) not null
);

select * from employee

-- item table 
CREATE TABLE item (
    ID SERIAL PRIMARY KEY,
    Category VARCHAR(50) NOT NULL,
    Sticker_Number VARCHAR(10) NOT NULL,
    Item_Issued_HandedOut DATE not NULL,
    Item_Issued_HandedIn DATE NULL,
    Employee_ID INTEGER NOT NULL,
    CONSTRAINT fk_employee_ID
        FOREIGN KEY (Employee_ID)
        REFERENCES employee (ID)
        ON DELETE RESTRICT 
        ON UPDATE CASCADE
);
-- Unique index for sticker_number (Used GPT for exact query)
CREATE UNIQUE INDEX idx_sticker_number_unique
ON item (Sticker_Number)
WHERE Item_Issued_HandedIn IS NULL;

select * from item

-- updating values (item) => to verify that both "Item_Issued_HandedIn" & "Item_Issued_HandedOut" column values are not NULL 
UPDATE item
SET Item_Issued_HandedIn = '2024-11-20'
WHERE Sticker_Number = 'HNDKS19' AND Item_Issued_HandedIn IS NULL;

select * from item 

-- ticket table and alter ticket with constraints 
create table ticket (
    ID serial primary key, 
    problem_description varchar(150) not null,
    ticket_num integer not null,
    creation_date date default current_date,
    completion_date date null,
    employee_ID_created integer not null,
    employee_ID_assigned integer not null
);
alter table ticket
    add constraint fk_employee_ID_created
    foreign key (employee_ID_created)
    references employee (ID)
        on delete restrict
        on update cascade, 
    add constraint fk_employee_ID_assigned 
    foreign key (employee_ID_assigned)
    references employee (ID)
        on delete restrict
        on update cascade


select * from ticket


-- office table 
create table office (
    ID serial primary key,
    Office_Name varchar(50) not null,
    Street_Address varchar(100) not null,
    zip_code_Address varchar(10) not null
);

select * from office


-- room table 
create table room (
    Room_Num varchar(10) primary key,
    Room_Type varchar(10) not null,
    Office_ID integer not null,
    constraint fk_room_ID
        foreign key (office_id)
        references office (ID)
    on delete cascade 
    on update cascade
);

select * from room


-- officehasitem (junction table) for office and item
create table OfficeHasItem (
    ID serial primary key,
    office_ID integer not null,
    item_ID integer not null,
    constraint fk_office_ID
    foreign key (office_ID)
        references office (ID),
    constraint fk_item_ID
    foreign key (item_ID)
        references item (ID)
    on delete restrict 
    on update cascade
);

select * from OfficeHasItem

-- itemassoicatedroom (junction table) for item and room 
create table ItemAssociatedRoom (
    ID serial primary key,
    room_ID varchar(10) not null,
    item_ID integer not null,
    constraint fk_room_ID
    foreign key (Room_ID)
        references room (room_num),
    constraint fk_item_ID
    foreign key (Item_ID)
        references item (ID)
    on delete restrict 
    on update cascade
);

select * from itemassociatedroom
