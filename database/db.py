import pymysql


def get_connection():

    connection = pymysql.connect(

        host="localhost",

        user="root",

        password="root",

        database="vulnscanner",

        charset="utf8",

        cursorclass=pymysql.cursors.DictCursor
    )

    return connection