CREATE TABLE USERDIRECTORY
( 
	USERID VARCHAR2(32 CHAR) NOT NULL,
	PASSWORD VARCHAR2(128 CHAR),
	FIRSTNAME VARCHAR2(64 CHAR),
	LASTNAME VARCHAR2(64 CHAR),
	PRIMARY KEY (USERID)
);

CREATE TABLE USERDIRROLES
( 
	USERID VARCHAR2(32 CHAR) NOT NULL,
	ROLETYPE VARCHAR2(9 CHAR) NOT NULL,
	NAME VARCHAR2(32 CHAR) NOT NULL,
	VALUE VARCHAR2(64 CHAR) NOT NULL,
	CONSTRAINT PK_USERDIRROLES PRIMARY KEY (USERID, ROLETYPE, NAME, VALUE)
);