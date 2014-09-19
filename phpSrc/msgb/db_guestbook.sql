--
-- Table structure for table `tb_user`
--

DROP TABLE IF EXISTS tb_user;

CREATE TABLE tb_user (
	id int(8) NOT NULL AUTO_INCREMENT,
	username varchar(50) NOT NULL,
	userpwd varchar(50) NOT NULL,
	truename varchar(50) NOT NULL,
	email varchar(50) NOT NULL,
	qq varchar(20) NOT NULL,
	tel varchar(20) NOT NULL,
	ip varchar(20) NOT NULL,
	address varchar(250) NOT NULL,
	face varchar(50) NOT NULL,
	regtime datetime NOT NULL,
	sex varchar(2) NOT NULL,
	usertype int(2) NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='保存用户的数据';

--
-- Table structure for table `tb_leaveword`
--

DROP TABLE IF EXISTS tb_leaveword;

CREATE TABLE tb_leaveword (
	id int(8) NOT NULL AUTO_INCREMENT,
	userid int(4) NOT NULL,
	createtime datetime NOT NULL,
	title varchar(250) NOT NULL COMMENT '留言主题',
	content text NOT NULL COMMENT '留言内容',
	PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='留言信息表';

--
-- Table structure for table `tb_replyword`
--

DROP TABLE IF EXISTS tb_replyword;

CREATE TABLE tb_replyword (
	id int(8) NOT NULL AUTO_INCREMENT,
	userid int(4) NOT NULL,
	createtime datetime NOT NULL,
	title varchar(250) NOT NULL COMMENT '留言主题',
	content text NOT NULL COMMENT '留言内容',
	leave_id int(4) NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='回复留言表';

--
-- Table structure for table `tb_admin`
--

DROP TABLE IF EXISTS tb_admin;

CREATE TABLE tb_admin (
	id int(8) NOT NULL AUTO_INCREMENT,
	adminname varchar(20) NOT NULL,
	adminpwd varchar(20) NOT NULL,
	email varchar(30) NOT NULL,
	ip varchar(20) NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='管理员信息表' ;
