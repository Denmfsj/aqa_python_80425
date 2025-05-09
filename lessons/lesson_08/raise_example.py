#raise ArithmeticError('My error')

def connect_to_db():  #  конектимось до БД
    print('Connection to db....')
    return True

def connect_to_db_broken():  #  конектимось до БД
    print('Connection to db....')
    raise TimeoutError('Connect to db TimeOut')

def execute_query(query, conn):
    raise ArithmeticError('Smth happens while query was executed')

def close_connect_to_db(conn):  #  закрити до БД
    print('Close connection')




# test 1


def test_check_data():
    try:
        # precondition
        connect = None
        connect = connect_to_db()

        # body
        db_data = execute_query('Select * from user_data where user_id = 5', connect)
        api_resp = []

        if db_data != api_resp:
            raise AssertionError('Data is not correct between db and API')

    except TimeoutError:  # якщо TimeoutError то вважаємо тест пройшов
        print('Cant connect to DB ... please check creds')  # logging

    except ArithmeticError as e:
        print('Cant reach data from table ...') # logging
        raise e

    finally:
        # post-condition
        if connect:
            close_connect_to_db(connect)

test_check_data()

