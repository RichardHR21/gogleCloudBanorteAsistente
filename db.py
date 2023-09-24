'''
#from google.cloud.sql.connector import Connector
from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql
import datetime

class dataBase():
    # initialize Connector object
    def __init__(self) :
        self.connector = Connector()

        # create connection pool
        self.pool = sqlalchemy.create_engine(
            "mysql+pymysql://",
            creator=self.getconn,
        )
        # create table
        self.create_stmt = sqlalchemy.text(
            "CREATE TABLE Investments (id int auto_increment, date datetime, inv_mon float, Primary Key (id))"
        )

        # insert statement
        self.insert_stmt = sqlalchemy.text(
            "INSERT INTO Investments (date, inv_mon) VALUES (:date, :inv_mon)",
        )

        self.delete_stmt = sqlalchemy.text(
            "DROP TABLE Investments, Investments2,  Investments3, Investments4,  Investments5"
        )
    

    # function to return the database connection
    def getconn(self) -> pymysql.connections.Connection:
        conn: pymysql.connections.Connection = self.connector.connect(
            "ornate-grin-400003:us-central1:banorte-finsor",
            "pymysql",
            user="root",
            password="123",
            db="banorte-finsor"
        )
        return conn

    

    

    def make(self):

        with self.pool.connect() as db_conn:
            # insert into database
            db_conn.execute(self.insert_stmt, parameters={"date": datetime.date.today(), "inv_mon": "5200.52"})

            # query database
            result = db_conn.execute(sqlalchemy.text("SELECT * from Investments")).fetchall()

            # commit transaction (SQLAlchemy v2.X.X is commit as you go)
            db_conn.commit()

            # Do something with the results
            for row in result:
                print(row)


        self.connector.close()
'''
from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql
import datetime

def google_cloud():
    # initialize Connector object
    connector = Connector()

    # function to return the database connection
    def getconn() -> pymysql.connections.Connection:
        conn: pymysql.connections.Connection = connector.connect(
            "ornate-grin-400003:us-central1:banorte-finsor",
            "pymysql",
            user="root",
            password="123",
            db="banorte-finsor"
        )
        return conn

    # create connection pool
    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )

    # create table
    create_stmt = sqlalchemy.text(
        "CREATE TABLE Investments (id int auto_increment, date datetime, inv_mon float, Primary Key (id))"
    )

    # insert statement
    insert_stmt = sqlalchemy.text(
        "INSERT INTO Investments (date, inv_mon) VALUES (:date, :inv_mon)",
    )

    delete_stmt = sqlalchemy.text(
        "DROP TABLE Investments, Investments2,  Investments3, Investments4,  Investments5"
    )

    with pool.connect() as db_conn:
        # insert into database
        db_conn.execute(insert_stmt, parameters={"date": datetime.date.today(), "inv_mon": float(5200.52)})

        # query database
        result = db_conn.execute(sqlalchemy.text("SELECT * from Investments")).fetchall()

        # commit transaction (SQLAlchemy v2.X.X is commit as you go)
        db_conn.commit()

        # Do something with the results
        for row in result:
            print(row)


    connector.close()

google_cloud()