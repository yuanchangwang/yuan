### �������ݿ�

```sql
create database students charset=utf8mb4;
use students
source /home/moluo/Desktop/student_system.sql
```



### ѧ�������

1. ��ѯ���༶305�ж��ٸ�����

   ```sql
   select count(id) from student where class=305 and sex=1;
   ```

2. ��ѯ������Ϊ4���ֵ�����ѧ����Ϣ(��š����������䣬�༶)

   ```sql
   select id,name,age,class from student where name like "____";
   ```

3. ��ѯ������������ѧ����Ϣ(��š����������䣬�༶)

   ```sql
   select id,name,age,class from student where name like "��%';
   ```

4. ��ѯ���༶���Ϊ301,203,303��Ů��������

   ```sql
   select count(id) from student where sex=2 and class in (301,203,303);
   select count(id) from student where sex=2 and (class=301 or class=203 or class=303);
   ```

5. ��ѯ��ѧ����ʮ������Ů����Ϣ(���������䡢���˼��)

   ```sql
   select id,name,sex,age,description from student where sex=2 and id%10=0;
   ```

6. ɾ��301�༶��������23�����ϵ�ѧ����Ϣ

   ```sql
   delete from student where class=301 and age>=23;
   ```

7. ��һ����'��Ȼ'��ѧ�����Ա�ĳ�Ů��

   ```sql
   update student set sex=2 where name='��Ȼ';
   ```

8. ��401�༶�е�����Ϊ'���'��ѧ����Ϣɾ��

   ```sql
   delete from student where class=401 and name='���';
   ```

9. ����305��������ѧ����ƽ�������Լ����ǵ�����������С����

   ```sql
   select avg(age) as avg,max(age) as max,min(age) as min from student where class=305;
   ```

10. ��ѯ401��402��403��404��405������ѧ��������ƽ��ֵ

    ```sql
    select avg(age) as avg from student where class in (401,402,403,404,405);
    ```

11. ��ѯ������ѧ�������ִ�"��"�ֵ�ѧ����Ϣ����������ʹ�����������������

    ```sql
    select id,name,age,class from student where name like '%��%' order by age asc;  // asc����
    select id,name,age,class from student where name like '%��%' order by age desc;  // desc����
    ```

12. �������ѧ����¼�����ݱ���
    ����     ����    �Ա�    �༶   ����ǩ��
    ������    22      1      301   �����䵱�ϰ�
    �Ŵ�ɽ    21      1      302   �����䵱�ϰ�������
    ���޼�    20      1      302   �����ϰ�

    ```sql
    insert into student (name,age,sex,class,description) values
        -> ('������',22,1,301,'�����䵱�ϰ�'),
    -> ('�Ŵ�ɽ',21,1,302,'�����䵱�ϰ�������'),
        -> ('���޼�',20,1,302,'�����ϰ�');
    ```
    
13. ��ѯ������18-20֮��������Ů��

    ```sql
    select name,age,sex from student where sex=2 and name like '��%' and (age between 18 and 20);
    ```

14. ��ѯ������18-20֮�������Ů���������ձ�Ž��н�������

    ```sql
    select id,name,sex,age from student where sex=2 and (age between 18 and 20) order by id desc;
    ```

15. ��ѯ��301,302,303,304,305,306��ÿ���༶��������

    ```sql
    select class,count(id) from student where class in (301,302,303,304,305,306) group by class;
    ```



### �ɼ������

16. ��ѯ��ѧ��Ϊ9��ѧ�����ܳɼ�

    ```sql
    select sid,sum(achievement) from achievement where sid=9;
    ```

17. ��ѯ���γ̱��Ϊ4�Ŀγ�ƽ���ɼ�

    ```sql
    select avg(achievement) from achievement where cid=4;
    ```

18. ��ѯ��ѧ��Ϊ6��ѧ�������гɼ�������ʾ��Ӧ�Ŀγ̱�š�

    ```sql
    select sid,cid,achievement from achievement where sid=6;
    ```

19. ��ѯ���γ̱��Ϊ4�Ŀγ̳ɼ��������з����Ľ������У���ʾ10���ɼ����ɡ�

    ```sql
    select cid,achievement from achievement where cid=4 order by achievement desc limit 10;
    ```

20. ��ѯ��ѧ��Ϊ1,2,3,4,5,6�⼸��ѧԱ��ƽ���ɼ���

    ```sql
    select sid,avg(achievement) from achievement where sid in (1,2,3,4,5,6) group by sid;
    ```

21. ��ѯ���ɼ�����ÿ��ѧ�Ƶ�ƽ���ɼ���

    ```sql
    select cid,avg(achievement) from achievement group by cid;
    ```

    

