

data_from_api = {'id': 5, 'score': '100', 'subjects': 1, 'average_score': 75}


# test

def check_average_score():

    try:
        expected_average_score =  data_from_api['score']/data_from_api['subjects']
    except TypeError:
        expected_average_score = int(data_from_api['score']) / data_from_api['subjects']

    if expected_average_score != data_from_api['average_score']:
        raise AssertionError(f'Scores are not equals:\nExpected: {expected_average_score}'
                             f'\nActual: {data_from_api["average_score"]}')


check_average_score()