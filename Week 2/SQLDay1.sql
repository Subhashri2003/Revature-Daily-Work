CREATE DATABASE RevStudDb;
-- DROP DATABASE RevStudDB;
USE RevStudDb;
CREATE TABLE student (
rollno INT,
snmae VARCHAR(25) not null,
addr VARCHAR(50),
CONSTRAINT pk_rollno PRIMARY KEY(rollno)
);

alter table student add city VARCHAR(20), pin int;
ALTER  TABLE student ALTER COLUMN addr VARCHAR(100);
ALTER TABLE student add dummycol INT;
EXEC sp_rename 'student.dummycol','dummy','COLUMN' ;
ALTER TABLE student DROP COLUMN dummy;