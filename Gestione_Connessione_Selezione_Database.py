import mysql.connector

# import errorcode per le diverse eccezioni che possono capitare
from mysql.connector import errorcode 


def esegui_sql(cursore, comando):
    # Elenco di tutte le persone della tabella 'dipendenti'
    try:
        cursore.execute(comando)
    except mysql.connector.Error as err:
        print(err)
        return False
    
    else:
        risposta = cursore.fetchall()
        for riga in risposta:
            print(riga)
        return True



def main():
    # Nome del database
    nome_database = "my_photos"
    try:
        # Connessione al Databse Mysql (salvato col DBMS phpmyadmin): 'my_photos' e creazione del cursore
        conn = mysql.connector.connect(user="marcob",
                                    password="password",
                                    host="localhost",
                                    database=nome_database)
        
        curs = conn.cursor()
        
    except mysql.connector.Error as err:
        # Gestione delle diverse situazioni di errore:
        # Se MySQL non risponde o rifiuta la connessione
        if err.errno == errorcode.ER_PROCACCESS_DENIED_ERROR:
            print("Errore nell'accesso a MySQL")
        # Se il database non esiste
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Errore nel nome del database", nome_database)
            print(err)
            print("Fine esecuzione")
            
        # fine esecuzione
        import sys
        sys.exit()


    
    
    # Prosegue l'esecuzione sul database scelto
    sql = "SELECT * FROM dipendenti"
    # ...........
    
    # Controlla correttezza esecuzione
    if esegui_sql(curs, sql):
        print("Comando eseguito con successo")
    else:
        print("Errore nell'esecuzione del comando")
        print(curs.statement)
    
    # chiusura del cursore e rilascio della connessione
    curs.close()
    conn.close()  
    
# esecuzione del programma
main() 