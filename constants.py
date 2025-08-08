import pathlib

BASE_DIR = pathlib.Path(__file__).parent
RESOURCE_FOLDER = pathlib.Path(BASE_DIR, 'tests', 'resources')
RESOURCE_USER_DATA_FOLDER = pathlib.Path(RESOURCE_FOLDER, 'user_data')
USER_DATA_PROD = pathlib.Path(RESOURCE_USER_DATA_FOLDER, 'prod_user.txt')
LESSON_15_FOLDER = BASE_DIR / 'lessons' / 'lesson_15'
UI_SCREENSHOTS_FOLDER = BASE_DIR / 'screenshots'