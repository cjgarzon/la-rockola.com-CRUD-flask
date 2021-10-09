import conexiondb

def LeerDatos():
    con = conexiondb.conexiondb()
    canciones= []
   
    with con.cursor() as cursor:
        query="SELECT * FROM cancion"
        
        cursor.execute(query)
       
        canciones=cursor.fetchall()
        
    con.close()
    return canciones

def LeerDatosAdmin():
    con = conexiondb.conexiondb()
    
    admins=[]
    with con.cursor() as cursor:
       
        admin="SELECT * FROM usuarioadmin"
  
        cursor.execute(admin)
        
        admins=cursor.fetchall()
    con.close()
    return admins