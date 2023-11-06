import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
try:
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="pynative_pool",
                                                                  pool_size=1,
                                                                  pool_reset_session=True,
                                                                  host='localhost',
                                                                  database='python_db',
                                                                  user='pynative',
                                                                  password='pynative@#29')
'''
    Arguments required to create a connection pool
•    pool_name: The pool name. As you can see we have given a pynative_pool as a connection pool name. 
If this argument not given, MySQL connector python automatically set name by other parameters like the host, user, and database.
 If multiple pools have the same name, then it is not an error. The application must create each pool with a distinct name.
•    pool_size: a pool size is a number of the connection objects that pool can support. 
If this argument not given, the default is 5.
 Pool size cannot be 0 or less than 0.
•    pool_reset_session: Whether to reset session variables when the connection returned to the pool.
•    a user, password, and database are additional connection arguments to connect MySQL.
'''
connection_pool.add_connection(connection_obj= None)
connection_objt = connection_pool.get_connection()
pool_name  = connection_pool.pool_name
pooled_connection = mysql.connector.pooling.PooledMySQLConnection(connection_pool, connection_object)
