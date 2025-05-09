def connect_to_db():  #  конектимось до БД
    print('Connection to db....')
    return True

def close_connect_to_db(conn):  #  закрити до БД
    # conn.close()
    print('Close connection')
    pass

def execute_query(query, conn):
    #return conn.execute(query)
    print('Executing  query......')

    return [{'id': 5, 'name': 'Alex'}],


try:
    connect = connect_to_db()
    res = execute_query('Select * from user_data where user_id = 5', connect)
except TimeoutError:
    print('Timeouterror')

except Exception:
    print('Exception')

finally:
    print('Finally execution')
    close_connect_to_db(connect)

