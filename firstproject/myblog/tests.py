from django.test import TestCase

# Create your tests here.

import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(
        user='Azure_Django_Blog',
        password='a0952739894Z',
        host='django-blog-database.mysql.database.azure.com',
        database='azure_django_blog',
        ssl_ca='static/ssl/DigiCertGlobalRootCA.crt.pem'
    )
    print("Connection successful!")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    conn.close()
