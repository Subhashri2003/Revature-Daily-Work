use RevCompanyDb;

select * from emp;

select e.ename as 'Employee', m.ename as 'Manager'
from emp e join emp m
on e.mgr=m.empno;

select e.ename as 'Employee', d.deptno as 'Deptno'
from emp e cross join dept d;

select *
from emp e cross join dept d

select ename 
from emp
where deptno=(select deptno 
from dept
where  dname='IT')

select ename from emp 
where sal>(select avg(sal) from emp)

select deptno,avgsal from 
(select deptno,avg(sal) as avgsal
from emp 
group by deptno) 
as Details; 


select ename,deptno,sal
from emp e
where sal>(select avg(sal) from emp 
where deptno=e.deptno);

--views
create view vemp as select empno,ename from emp where deptno in(10,20,30);


select * from vemp;

insert into emp(empno,ename,deptno) values(1110,'xxx',20)
insert into vemp values(1111,'yyy');

update vemp set empno=10000 where empno=1111
update vemp set ename='kkk' where empno=1111


delete from vemp where  empno=1111
drop view vemp
create nonclustered index idepyno on emp(deptno)
drop index emp.ideptno


--stored procedures

create or alter procedure sp_empdata
  @empno int, @ename varchar(30),@deptno int,@sal numeric(10,2)
as 
  begin
    begin transaction
     insert into emp(empno,ename,sal,deptno)
     values (@empno,@ename,@sal,@deptno)
     update emp set comm=sal*0.1 where empno=@empno
     commit
     select * from emp
     return 1
end

declare @status int
exec sp_empdata 1016,'raju',20,20000
print @status

--functions

create or alter function dbo.EmpInsertion(@empno int,@ename varchar(30))
returns varchar(20)
as
begin
 return cast(@empno as varchar) + '-' + @ename
end

select dbo.EmpInsertion(2000,'quig') response


create or alter function AvgSal()
returns table
as
return select avg(sal) as avgsal from emp group by deptno;

select * from AvgSal() 

create trigger trg_AfterInsertEmp
on emp
after insert
as
begin
print 'New employee record inserted into emp table';
end

insert into emp(empno,ename) values (11111,'ecsewf')