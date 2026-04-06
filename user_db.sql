create database USER_DB
GO

use USER_DB
GO

create table users (
    Id int primary key,
    Ten varchar(100),
    DiaChi varchar(100),
    Email varchar(100)
)

insert into users values
(1,'Thuy Linh','Hoa Binh','lyn@gmail.com'),
(2,'Ngan','Nam Dinh','ngan@gmail.com')