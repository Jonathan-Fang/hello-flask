import pymysql

def mysqlconnect():
    # connect to the MySQL database
    connect = pymysql.connect(
        host='localhost',
        user='root',
        password='Tgbmysqlr!', # hardcoding password, development vs. production, could query password
        db='sept_database',
    )

    # cur = connect.cursor()
    # cur.execute("select @@version") #ln 12-15 debug can delete
    # output = cur.fetchall()
    # print(output) #debug
    select_alpha = 'SELECT * FROM sept_table_alpha'
    sql_queries = ['SELECT * FROM sept_table_alpha', 'SELECT * FROM sept_table_beta', "INSERT INTO sept_table_alpha(username, password, element, age) VALUES(\'buriedintheearth\', \'help345\', \'earth\', 18)", "DELETE FROM sept_table_alpha WHERE sept_table_alpha.PrimaryID = 1"]
    sql_descriptions = ['selected from sept_table_alpha', 'selected from sept_table_beta', 'added a row', 'removed a row']
    with connect: #with is a python thing
        with connect.cursor() as cursor:
            for i in range(len(sql_queries)):
                # read all records from both tables # some kind of loop
                sql = sql_queries[i]
                # sql = 'SELECT * FROM sept_table_alpha' #input into list; 
                cursor.execute(sql)
                if "INSERT" in sql or "DELETE" in sql:
                    cursor.execute(select_alpha)
                result = cursor.fetchall()
                desc = sql_descriptions[i] #second list corresponding to queries
                print(result)
                print(desc)

        #         sql = 'SELECT * FROM sept_table_beta'
        #         cursor.execute(sql)
        #         result = cursor.fetchall()
        #         desc = 'selected from sept_table_beta'
        #         print(result)
        #         print(desc)
        
        # with connect.cursor() as cursor: # redundent
        #     # add a row
        #     sql = """INSERT INTO sept_table_alpha(username, password, element, age) VALUES('buriedintheearth', 'help345', 'earth', 18)"""
        #     cursor.execute(sql)
        #     sql = 'SELECT * FROM sept_table_alpha'
        #     cursor.execute(sql)
        #     result = cursor.fetchall()
        #     desc = 'added a row'
        #     print(result)
        #     print(desc)

        #     # delete a row
        #     sql = """DELETE FROM sept_table_alpha WHERE sept_table_alpha.PrimaryID = 1"""
        #     cursor.execute(sql)
        #     sql = 'SELECT * FROM sept_table_alpha'
        #     cursor.execute(sql)
        #     result = cursor.fetchall()
        #     desc = 'removed a row'
        #     print(result)
        #     print(desc)

    # close the connection
    # connect.close()

# Driver code
if __name__ == "__main__" :
    mysqlconnect()