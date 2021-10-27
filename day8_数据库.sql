-- MySQL dump 10.13  Distrib 5.6.24, for Win32 (x86)
--
-- Host: localhost    Database: company
-- ------------------------------------------------------
-- Server version	5.6.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


DROP DATABASE IF EXISTS company;

CREATE DATABASE IF NOT EXISTS company CHARACTER SET utf8;

USE company;


--
-- Table structure for table `t_dept`
--

`t_dept`


-- 1.查询出部门编号为30的所有员工
SELECT ename 员工姓名 ,deptno 部门编号 FROM t_employees
WHERE deptno = 30

-- 2.所有经理的姓名、编号和部门编号
SELECT ename 员工姓名, empno 员工编号, deptno 部门编号
FROM t_employees
WHERE  job = '经理'

-- 3.找出奖金高于工资的员工。
SELECT ename 员工姓名
FROM t_employees
WHERE comm > sal

-- 4.找出奖金高于工资60%的员工。
SELECT ename 员工姓名
FROM t_employees
WHERE comm > sal * 0.6

-- 5.找出部门编号为10中所有经理，和部门编号为20中所有分析员的详细资料。
SELECT *
FROM t_employees
WHERE (deptno = 10 AND job = '经理') OR (deptno = 20 AND job = '分析员')

-- 6. 找出部门编号为10中所有经理，部门编号为20中所有分析员，
-- 还有即不是经理又不是武装上将但其工资大或等于3000的所有员工详细资料。
SELECT *
FROM t_employees
WHERE (deptno = 10 AND job = '经理') OR (deptno = 20 AND job = '分析员') OR (job NOT IN( '经理' ,'武装上将') AND sal >= 3000)

-- 7. 无奖金或奖金低于1000的员工。
SELECT ename 员工姓名
FROM t_employees
WHERE comm = 0 OR comm < 1000

-- 8.查询名字由三个字组成的员工。
SELECT *
FROM t_employees
WHERE ename LIKE '___'

-- 9.查询2000年以及以后入职的员工。
SELECT *
FROM t_employees
WHERE hiredate > '1999-12-31'

-- 10.查询所有员工详细信息，用编号升序排序
SELECT *
FROM t_employees
ORDER BY empno ASC

-- 11.查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序
SELECT *
FROM t_employees
ORDER BY sal DESC,hiredate ASC

-- 12.查询每个部门的平均工资
SELECT deptno ,AVG(sal)
FROM t_employees
GROUP BY deptno

-- 13.查询每个部门的雇员数量。
SELECT deptno,COUNT(deptno) number
FROM t_employees
GROUP BY deptno

-- 14. 查询每种工作的最高工资、最低工资、人数
SELECT job,MAX(sal) 最高工资, MIN(sal) 最低工资,COUNT(job) 人数
FROM t_employees
GROUP BY job


