from __future__ import print_function
from flask import Flask
import mysql.connector
from mysql.connector import errorcode
app = Flask(__name__)

@app.route('/')
def hello_world():
	cnx = mysql.connector.connect(user='monty', password='some_pass', host='192.168.0.3', database='menagerie')
	DB_NAME = 'menagerie'
	TABLES = {}
	TABLES['employees'] = (
	    "CREATE TABLE `employees` ("
	    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
	    "  `birth_date` date NOT NULL,"
	    "  `first_name` varchar(14) NOT NULL,"
	    "  `last_name` varchar(16) NOT NULL,"
	    "  `gender` enum('M','F') NOT NULL,"
	    "  `hire_date` date NOT NULL,"
	    "  PRIMARY KEY (`emp_no`)"
	    ") ENGINE=InnoDB")
	TABLES['departments'] = (
	    "CREATE TABLE `departments` ("
	    "  `dept_no` char(4) NOT NULL,"
	    "  `dept_name` varchar(40) NOT NULL,"
	    "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
	    ") ENGINE=InnoDB")
	cursor = cnx.cursor()
	for table_name in TABLES:
	    table_description = TABLES[table_name]
	    try:
	        print("Creating table {}: ".format(table_name), end='')
	        cursor.execute(table_description)
	    except mysql.connector.Error as err:
	        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
	            print("already exists.")
	        else:
	            print(err.msg)
	    else:
	        print("OK")
	cursor.close()	
	cnx.close()	
	return("Hello World")

@app.route('/test')
def testWorld():
    return 'test, World!'
