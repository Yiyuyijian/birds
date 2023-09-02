import sqlite3
from sqlite3 import Error

class my_sql(object):
    def __init__(self,db_name:str):
        try: 
            self.__connention = sqlite3.connect(f"{db_name}.db")
            self.__cursor = self.__connention.cursor()
        except Error: 
            print(Error)

    def table_exists(self,table_name:str):
        self.__cursor.execute(f'SELECT name from sqlite_master WHERE type = "table" AND name = "{table_name}"')
        tables = self.__cursor.fetchall()
        try:
            if tables[0][0] == table_name:
                return True
        except:
            return False

    def create_table(self,table_name:str,columns:str):
        print(f"CREATE TABLE if not exists {table_name}{columns}")
        self.__cursor.execute(f"CREATE TABLE if not exists {table_name}{columns}")
        self.__connention.commit()

    def show_tables(self):
        print('SELECT name from sqlite_master WHERE type= "table"')
        self.__cursor.execute('SELECT name from sqlite_master WHERE type= "table"')
        print(self.__cursor.fetchall())

    def delete_table(self,table_name:str):
        print(f'drop table if exists {table_name}')
        self.__cursor.execute(f'drop table if exists {table_name}')

    def insert_row(self,table_name:str,row:tuple):
        print(f"INSERT INTO {table_name} VALUES{row}")
        self.__cursor.execute(f"INSERT INTO {table_name} VALUES{row}")
        self.__connention.commit()

    def value_update(self,table_name:str,column:str,value):
        print(f'UPDATE {table_name} SET {column} = "{value}" where id = 2')
        self.__cursor.execute(f'UPDATE {table_name} SET {column} = "{value}" where id = 2')

    def row_values(self,table_name:str,end_row:int = None):
        print(f'SELECT * FROM {table_name}')
        self.__cursor.execute(f'SELECT * FROM {table_name}')#*表示选择所有列
        if end_row == None:
            return self.__cursor.fetchall()
        else:
            return self.__cursor.fetchmany(end_row)
        
    '''def col_values(self,table_name:str,column:str):
        print(f'SELECT {column} FROM {table_name}')
        self.__cursor.execute(f'SELECT {column} FROM {table_name}')'''

    def close(self):
        self.__connention.close()


if __name__ == "__main__":
    sql = my_sql("test")

    print(sql.row_values('test1'))
