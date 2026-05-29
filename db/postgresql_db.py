import psycopg2



db_creds = {
    "db_name",
    "user",
    "password",
    "host",
    "port"
}



class PostGSQL:


    def __init__(self):
        

        pass


    def get_connection(self):

        connection = psycopg2.connect()