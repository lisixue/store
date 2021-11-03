CREATE DATABASE bank CHARACTER SET utf8
CREATE TABLE USER(
	account INT(8) PRIMARY KEY,
	username VARCHAR(20),
	PASSWORD INT(6),
	country VARCHAR(20),
	province VARCHAR(20),
	street VARCHAR(20),
	door VARCHAR(20),
	money INT(20),
	registerDate DATETIME,
	bankname VARCHAR(20) 
);

INSERT INTO USER VALUE (10214512,'小李',123456,'中国','河南','一号路','001',4500,'2021-10-25','中国工商银行'),
	(15421475,'小许',111111,'中国','浙江','小豆蔻','015',5140,'2020-01-10 10:10:10','浙江分行'),
	(15924475,'小王',111111,'中国','上海','七马路','004',8690,'2020-09-19','上海分行')







