### 创建数据库

```sql
create database students charset=utf8mb4;
use students
source /home/moluo/Desktop/student_system.sql
```



### 学生表操作

1. 查询出班级305有多少个男生

   ```sql
   select count(id) from student where class=305 and sex=1;
   ```

2. 查询出名字为4个字的所有学生信息(编号、姓名，年龄，班级)

   ```sql
   select id,name,age,class from student where name like "____";
   ```

3. 查询出所有姓王的学生信息(编号、姓名，年龄，班级)

   ```sql
   select id,name,age,class from student where name like "王%';
   ```

4. 查询出班级编号为301,203,303的女生总人数

   ```sql
   select count(id) from student where sex=2 and class in (301,203,303);
   select count(id) from student where sex=2 and (class=301 or class=203 or class=303);
   ```

5. 查询出学号整十的所有女生信息(姓名、年龄、个人简介)

   ```sql
   select id,name,sex,age,description from student where sex=2 and id%10=0;
   ```

6. 删除301班级中年龄在23岁以上的学生信息

   ```sql
   delete from student where class=301 and age>=23;
   ```

7. 把一个叫'卫然'的学生的性别改成女的

   ```sql
   update student set sex=2 where name='卫然';
   ```

8. 把401班级中的姓名为'吴杰'的学生信息删除

   ```sql
   delete from student where class=401 and name='吴杰';
   ```

9. 计算305班中所有学生的平均年龄以及他们的最大年龄和最小年龄

   ```sql
   select avg(age) as avg,max(age) as max,min(age) as min from student where class=305;
   ```

10. 查询401，402，403，404，405中所有学生的年龄平均值

    ```sql
    select avg(age) as avg from student where class in (401,402,403,404,405);
    ```

11. 查询出所有学生中名字带"白"字的学生信息，并对他们使用年龄进行升序排列

    ```sql
    select id,name,age,class from student where name like '%白%' order by age asc;  // asc升序
    select id,name,age,class from student where name like '%白%' order by age desc;  // desc降序
    ```

12. 添加以下学生记录到数据表中
    姓名     年龄    性别    班级   个性签名
    张三丰    22      1      301   我是武当老板
    张翠山    21      1      302   我是武当老板的五弟子
    张无忌    20      1      302   明教老板

    ```sql
    insert into student (name,age,sex,class,description) values
        -> ('张三丰',22,1,301,'我是武当老板'),
    -> ('张翠山',21,1,302,'我是武当老板的五弟子'),
        -> ('张无忌',20,1,302,'明教老板');
    ```
    
13. 查询年龄在18-20之间的姓李的女生

    ```sql
    select name,age,sex from student where sex=2 and name like '李%' and (age between 18 and 20);
    ```

14. 查询年龄在18-20之间的所有女生，并按照编号进行降序排序

    ```sql
    select id,name,sex,age from student where sex=2 and (age between 18 and 20) order by id desc;
    ```

15. 查询出301,302,303,304,305,306中每个班级总人数。

    ```sql
    select class,count(id) from student where class in (301,302,303,304,305,306) group by class;
    ```



### 成绩表操作

16. 查询出学号为9的学生的总成绩

    ```sql
    select sid,sum(achievement) from achievement where sid=9;
    ```

17. 查询出课程编号为4的课程平均成绩

    ```sql
    select avg(achievement) from achievement where cid=4;
    ```

18. 查询出学号为6的学生的所有成绩，并显示对应的课程编号。

    ```sql
    select sid,cid,achievement from achievement where sid=6;
    ```

19. 查询出课程编号为4的课程成绩，并进行分数的降序排列，显示10个成绩即可。

    ```sql
    select cid,achievement from achievement where cid=4 order by achievement desc limit 10;
    ```

20. 查询出学号为1,2,3,4,5,6这几个学员的平均成绩。

    ```sql
    select sid,avg(achievement) from achievement where sid in (1,2,3,4,5,6) group by sid;
    ```

21. 查询出成绩表中每个学科的平均成绩。

    ```sql
    select cid,avg(achievement) from achievement group by cid;
    ```

    

