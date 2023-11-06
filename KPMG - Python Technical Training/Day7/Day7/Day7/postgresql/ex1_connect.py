def connect():
    try :
        #python -m pip install psycopg2
        import psycopg2 as pg
        conn=pg.connect(user="nishant",password="1234",database="newdb",
                        port="5432",host="127.0.0.1")
        cur=conn.cursor()
        return conn,cur
       
    except pg.DatabaseError as de:
        print(de.__class__.__name__,":-",de)
        conn=None 
        cur=None
        return conn,cur
    
if __name__=="__main__":
    b=connect()
    print(b)
    b[0].close()     
        