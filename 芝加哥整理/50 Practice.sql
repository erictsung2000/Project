CREATE DATABASE `sql_50practice` ;
USE `sql_50practice`;


create table student(
sno VARCHAR(10) primary key, -- 學生編號
sname VARCHAR(20), -- 學生姓名
sage INT, -- 年齡
ssex VARCHAR(5) -- 性別
 );
 
create table teacher(
tno VARCHAR(10) primary key, -- 教師編號
tname VARCHAR(20)-- 教師姓名
 );
 
create table course(
cno VARCHAR(10), -- 課程編號
cname VARCHAR(20), -- 課程名稱
tno VARCHAR(20), -- 教師編號
constraint pk_course primary key (cno,tno)
);
 
create table sc(
sno VARCHAR(10), -- 學生編號
cno VARCHAR(10), -- 課程編號
score FLOAT, -- 分數 (float 不用再指定)
constraint pk_sc primary key (sno,cno)
);

-- 學生表
insert into student values ('s001','張三',23,'男');
insert into student values ('s002','李四',23,'男');
insert into student values ('s003','吳鵬',25,'男');
insert into student values ('s004','琴沁',20,'女');
insert into student values ('s005','王麗',20,'女');
insert into student values ('s006','李波',21,'男');
insert into student values ('s007','劉玉',21,'男');
insert into student values ('s008','蕭蓉',21,'女');
insert into student values ('s009','陳蕭曉',23,'女');
insert into student values ('s010','陳美',22,'女');
insert into student values ('s011','王麗',24,'女');
insert into student values ('s012','蕭蓉',20,'女');

-- 教師表
insert into teacher values ('t001', '劉陽');
insert into teacher values ('t002', '諶燕');
insert into teacher values ('t003', '胡明星');

-- 課程表
insert into course values ('c001','J2SE','t002');
insert into course values ('c002','Java Web','t002');
insert into course values ('c003','SSH','t001');
insert into course values ('c004','Oracle','t001');
insert into course values ('c005','SQL SERVER 2005','t003');
insert into course values ('c006','C#','t003');
insert into course values ('c007','JavaScript','t002');
insert into course values ('c008','DIV+CSS','t001');
insert into course values ('c009','PHP','t003');
insert into course values ('c010','EJB3.0','t002');

-- 成績表
insert into sc values ('s001','c001',78.9);
insert into sc values ('s002','c001',80.9);
insert into sc values ('s003','c001',81.9);
insert into sc values ('s004','c001',50.9);
insert into sc values ('s005','c001',59.9);
insert into sc values ('s001','c002',82.9);
insert into sc values ('s002','c002',72.9);
insert into sc values ('s003','c002',82.9);
insert into sc values ('s001','c003',59);
insert into sc values ('s006','c003',99.8);
insert into sc values ('s002','c004',52.9);
insert into sc values ('s003','c004',20.9);
insert into sc values ('s004','c004',59.8);
insert into sc values ('s005','c004',50.8);
insert into sc values ('s002','c005',92.9);
insert into sc values ('s001','c007',78.9);
insert into sc values ('s001','c010',78.9);
# from 後面命名

-- 1.查詢學生表的 前10條資料
select * from student limit 10 ; 


-- 2.查詢成績表所有成績的最低分,平均分,總分
select MIN(score) "最低分", AVG(score) "平均分" , SUM(score) "總分"
from sc ;

-- 3.查詢老師 “諶燕” 所帶的課程設數量
select count(*) from course
where tno = "t002";


-- 4.查詢所有老師所帶 的課程 數量
select tno , count(*)
from course
group by tno
order by tno ASC ;


-- 5.查詢姓”張”的學生名單
select * from student
where sname like "張%";



-- 6.查詢課程名稱為’Oracle’且分數低於60 的學號和分數
select sname , score 
from student st,sc,course c
where st.sno = sc.sno and sc.cno=c.cno and c.cname = "Oracle"  and sc.score < 60;



-- 7.查詢所有學生的選課情況;




select st.sno,st.sname,c.cname 
from student st,sc,course c
where st.sno = sc.sno and sc.cno = c.cno ;


-- 8.查詢任何一門課程成績在70 分以上的姓名.課程名稱和分數;




select st.sname,c.cname,score
from student st, sc , course c
where st.sno = sc.sno and c.cno = sc.cno and score > 70;


-- 9.查詢不及格的課程,並按課程號從大到小排列




select sc.sno,c.cname,sc.score
from sc , course c
where sc.cno=c.cno and sc.score < 60 
order by sc.cno DESC;


-- 10.查詢沒學過"諶燕"老師講授的任一門課程的學生姓名




select st.sname from student st
where st.sno not in
(select distinct sc.sno from sc,course c ,teacher t
where sc.cno=c.cno and c.tno = t.tno and t.tname = "諶燕");



-- 11.查詢兩門以上不及格課程的同學的學號及其平均成績
select sno , avg(score)
from sc
where sno in (
select sno
from sc 
where sc.score < 60
 group by sno 
having count(sno)>1)
group by sno;



-- 12.檢索"c004"課程分數小於60,按分數降序排列的同學學號
select sno,score
from sc 
where cno = "c004" and score < 60 
order by score DESC;


-- 13.刪除"s002"同學的"c001"課程的成績
--  delete from sc where sno='s002' and cno='c001';


-- 14.查詢"c001"課程比"c002"課程成績高的所有學生的學號;
select a.sno as "學生學號" from sc a
left join sc b ON a.sno = b.sno
where a.cno = "c001" AND b.cno = "c002" AND a.score > b.score;


-- 15.查詢平均成績大於60 分的同學的學號和平均成績;
select sno , avg(score)
from sc 
group by sno 
having avg(score) > 60;

-- 16.查詢所有同學的學號.姓名.選課數.總成績;

select a.*, s.sname from 
(select sno,sum(score),count(cno) from sc group by sno) a ,student s where a.sno=s.sno;

-- 17.查詢姓"劉"的老師的個數;
select count(*) from teacher where tname like '劉%';



-- 18.查詢沒學過"諶燕"老師課的同學的學號.姓名;
select * from student st where st.sno not in
(select distinct sno from sc s join course c on s.cno=c.cno
join teacher t on c.tno=t.tno where tname='諶燕'); 


-- 19.查詢學過"c001"並且也學過編號"c002"課程的同學的學號.姓名;
select st.* from sc a
join sc b on a.sno=b.sno
join student st
on st.sno=a.sno
where a.cno='c001' and b.cno='c002' and st.sno=a.sno;


-- 20.查詢學過"諶燕"老師所教的所有課的同學的學號:姓名;
 select st.* from student st join sc s on st.sno=s.sno
 join course c on s.cno=c.cno
 join teacher t on c.tno=t.tno
 where t.tname='諶燕';


-- 21.查詢課程編號"c002"的成績比課程編號"c001"課程低的所有同學的學號.姓名;
 select * from student st
 join sc a on st.sno=a.sno
 join sc b on st.sno=b.sno
 where a.cno='c002' and b.cno='c001' and a.score < b.score;

-- 22.查詢所有課程成績小於60 分的同學的學號.姓名;
 select st.*,s.score from student st
 join sc s on st.sno=s.sno
 join course c on s.cno=c.cno
 where s.score <60;

-- 23.查詢沒有學全所有課的同學的學號.姓名;
select s.sno, s.sname from student s -- 學號 姓名
left join sc s2 on s2.sno=s.sno
group by s.sno, s.sname 
having count(s2.cno)< (select count(cno) from course); -- 學生的課程 < 全部的課程

-- 24.查詢至少有一門課與學號爲"s001"的同學所學相同的同學的學號和姓名;
-- <> 不等於
 select st.* from student st,
 (select distinct a.sno from
 (select * from sc) a,
 (select * from sc where sc.sno='s001') b
 where a.cno=b.cno) h
 where st.sno=h.sno and st.sno<>'s001';
 
-- 25.查詢至少學過學號爲"s001"同學所有一門課的其他同學學號和姓名;
# 空格代表 AS 命名
 select * from sc
 left join student st on st.sno=sc.sno
 where sc.sno <>'s001' -- 在學生裡，學號不等於001的
 and sc.cno in (select cno from sc where sno='s001'); -- 他們的課程號碼在 (課表裡是學號為001)
 
-- 26.把"SC"表中"諶燕"老師教的課的成績都更改爲此課程的平均成績;
--  update sc c set score=(select avg(c.score)  from course a,teacher b
--                              where a.tno=b.tno
--                              and b.tname='諶燕'
--                              and a.cno=c.cno
--                              group by c.cno)
--  where cno in(
--  select cno from course a,teacher b
--  where a.tno=b.tno
--  and b.tname='諶燕');

-- 27.查詢和"s001"號的同學學習的課程完全相同的其他同學學號和姓名;
SELECT s2.sno, s2.sname
FROM sc s1
JOIN sc s2 ON s1.cno = s2.cno AND s1.sno <> s2.sno
JOIN student s2_info ON s2.sno = s2_info.sno
WHERE s1.sno = 's001'
GROUP BY s2.sno, s2.sname
HAVING COUNT(DISTINCT s1.cno) = (SELECT COUNT(DISTINCT cno) FROM sc WHERE sno = 's001');




-- 28.刪除學習"諶燕"老師課的SC 表記錄;
--  delete from sc
--  where sc.cno in
--  (
--  select cno from course c
--  left join teacher t on  c.tno=t.tno
--  where t.tname='諶燕'
--  );
 
-- 29.向SC 表中插入一些記錄,這些記錄要求符合以下條件:沒有上過編號"c002"課程的同學學號."c002"號課的平均成績;
 insert into sc (sno,cno,score)
 select distinct st.sno,sc.cno,(select avg(score)from sc where cno='c002')
 from student st,sc
 where not exists
 (select * from sc where cno='c002' and sc.sno=st.sno) and sc.cno='c002';



-- 30.查詢各科成績最高和最低的分:以如下形式顯示:課程ID,最高分,
 select cno ,max(score),min(score) from sc group by cno;
 
-- 31.按各科平均成績從低到高和及格率的百分數從高到低順序
 select cno,avg(score),sum(case when score>=60 then 1 else 0 end)/count(*)
 as "及格率"
from sc group by cno
 order by avg(score) , 及格率
 desc;

-- 32.查詢不同老師所教不同課程平均分從高到低顯示

 
-- 33.統計列印各科成績,各分數段人數:課程ID,課程名稱,[100-85],[85-70],[70-60],[ <60]
select sc.cno,c.cname,
 sum(case  when score between 85 and 100 then 1 else 0 end) AS "[100-85]",
 sum(case  when score between 70 and 85 then 1 else 0 end) AS "[85-70]",
 sum(case  when score between 60 and 70 then 1 else 0 end) AS "[70-60]",
 sum(case  when score <60 then 1 else 0 end) AS "[<60]"
 from sc, course c
 where  sc.cno=c.cno
 group by sc.cno ,c.cname;
 
-- 34.查詢各科成績前三名的記錄:(不考慮成績並列情況)
SELECT *
FROM sc x
WHERE (SELECT COUNT(*) FROM sc y WHERE x.cno = y.cno AND x.score < y.score)<3 
ORDER BY cno,score DESC;


-- 35.查詢每門課程被選修的學生數
 select cno,count(sno)from sc group by cno;
 
-- 36.查詢出只選修了一門課程的全部學生的學號和姓名
select sc.sno,st.sname,count(cno) from student st
 left join sc
 on sc.sno=st.sno
 group by st.sname,sc.sno having count(cno)=1;
 
-- 37.查詢男生.女生人數
 select ssex,count(*)from student group by ssex;

-- 38.查詢同名同性學生名單,並統計同名人數
 select sname,count(*)from student group by sname having count(*)>1;
 
-- 39. 1981 年出生的學生名單(注:Student 表中Sage 列的類型是INT)
SELECT *
FROM student
WHERE sage = 1981;

 
-- 40.查詢每門課程的平均成績,結果按平均成績升序排列,平均成績相同時,按課程號降序排列
  select cno,avg(score) from sc group by cno order by avg(score)asc,cno desc;
 
-- 41.查詢平均成績大於85 的所有學生的學號.姓名和平均成績
select st.sno,st.sname,avg(score) from student st
 left join sc
 on sc.sno=st.sno
 group by st.sno,st.sname having avg(score)>85;
 
-- 42.查詢課程編號爲c001 且課程成績在80 分以上的學生的學號和姓名;
 select st.sno,st.sname,sc.score from sc,student st
 where sc.sno=st.sno and cno='c001' and score>80;
 
-- 43.求選了課程的學生人數
 select count(distinct sno) from sc;
 
-- 44.查詢選修"諶燕"老師所授課程的學生中,成績最高的學生姓名及其成績
 select st.sname,score from student st,sc ,course c,teacher t
 where
 st.sno=sc.sno and sc.cno=c.cno and c.tno=t.tno
 and t.tname='諶燕' and sc.score=
 (select max(score)from sc where sc.cno=c.cno);
 
-- 45.查詢各個課程及相應的選修人數
 select cno,count(sno) from sc group by cno;
 
-- 46.查詢不同課程成績相同的學生的學號.課程號.學生成績
 select a.* from sc a ,sc b where a.score=b.score and a.cno<>b.cno; 	
 
-- 47.查詢每門功課成績最好的前兩名
SELECT sno, cno, score
FROM (
  SELECT sno, cno, score,
         ROW_NUMBER() OVER (PARTITION BY cno ORDER BY score DESC) as ranking
  FROM sc
) AS ranked_scores
WHERE ranking <= 2;


 
-- 48.統計每門課程的學生選修人數(超過10 人的課程才統計).要求輸出課程號和選修人數,查詢結果按人數降序排列,若人數相同,按課程號升序排列
select cno,count(sno) from sc group by cno
 having count(sno)>10
 order by count(sno) desc,cno asc;
 
-- 49.檢索至少選修兩門課程的學生學號
 select sno from sc group by sno having count(cno)>1;
 
-- 50.查詢全部學生都選修的課程的課程號和課程名
 select distinct(c.cno),c.cname from course c ,sc
 where sc.cno=c.cno
