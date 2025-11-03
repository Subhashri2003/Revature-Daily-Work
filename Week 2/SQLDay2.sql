USE RevStudDb;

BEGIN TRANSACTION;

INSERT INTO student values(101,'aaa','qwerty','blr',346546);
INSERT INTO student values(102,'bbb','vywndi','chn',478476);

SELECT * FROM student;

SAVE TRANSACTION level1;

INSERT INTO student(rollno,snmae,pin)
values(103,'ccc',387549);
INSERT INTO student(snmae,pin,rollno)
values('ddd',387549,104);

SAVE TRANSACTION level2;


UPDATE student SET addr='fwhie' 
WHERE rollno=103;

ROLLBACK TRANSACTION level2;

COMMIT TRANSACTION;

UPDATE student SET addr='hdbwiu' 
WHERE rollno=104;
UPDATE student SET city='hyd' 
WHERE rollno=104;
UPDATE student SET city='chn' 
WHERE rollno=103;

DELETE FROM student WHERE rollno=104;

TRUNCATE TABLE student;



-- creating new database

create database RevCompanyDb

use RevCompanyDb
create table dept(deptno smallint, dname varchar(3) NOT NULL,
constraint  pk_deptno primary key(DEPTNO));

create table emp(empno smallint,
ename varchar(30) NOT NULL,
mgr smallint,
sal numeric(10,2),
comm numeric(7,2),
deptno smallint,
constraint pk_emp primary key(empno),
constraint fk_deptno foreign key(deptno) references dept(deptno));

insert into dept values (10,'IT');
insert into dept values (20,'HR');
insert into dept values (30,'SAL');
insert into dept values (40,'MKT');
insert into dept values (50,'OPS');

select * from dept;

insert into emp (empno, ename, mgr, sal, comm, deptno) values
(1001, 'Alice', NULL, 60000.00, NULL, 10),  -- HR
(1002, 'Bob', 1001, 75000.00, NULL, 20),    -- IT
(1003, 'Charlie', 1002, 50000.00, 500.00, 30), -- Sales
(1004, 'Diana', 1003, 52000.00, 300.00, 30),   -- Sales
(1005, 'Ethan', 1002, 58000.00, NULL, 40),  -- Finance
(1006, 'Fiona', 1005, 62000.00, NULL, 50);  -- Marketing

select * from emp;
select * from dept;
 

 select empno as "number",ename as "name"
 from emp;

 select empno as "number",ename as "name"
 from emp
 where sal>70000;

 select empno as "number",ename as "name"
 from emp
 where empno not in(1002,1003,1005);

 select empno as "number",ename as "name"
 from emp
 where sal between 40000 and 60000;

 select empno as "number",ename as "name"
 from emp
 where ename like  'a%';

 select empno as "number",ename as "name"
 from emp
 where ename like  '__a%';

 select empno as "number",ename as "name"
 from emp
 where ename in ('alice','bob');

 select empno as "number",ename as "name"
 from emp
 where empno=1004 or ename like '%a%';


 select empno as "number",ename as "name", sal
 from emp
 where sal>50000
 order by sal;

 select empno as "number",ename as "name", sal,comm as 'commission'
 from emp
 where sal>50000
 order by comm,sal desc;


 select count(empno) as "number of emp",sum(sal) as "Total", 
 avg(comm) as 'avg commision',min(sal) as'least salary',
 max(sal) as 'Top earner'
 from emp; 


 select deptno, sum(sal) as 'total salary'
 from emp
 group by deptno

 select deptno, sum(sal) as 'total salary'
 from emp
 where deptno in (10,30,50)
 group by deptno
 having sum(sal) >= 62000
 order by sum(sal)



select e.ename,d.dname
from emp e join dept d
on d.deptno = e.deptno;

select e.ename,d.dname
from emp e left outer join dept d
on d.deptno = e.deptno;

select e.ename,d.dname
from emp e right outer join dept d
on d.deptno = e.deptno;

select e.ename,d.dname
from emp e full outer join dept d
on d.deptno = e.deptno;


