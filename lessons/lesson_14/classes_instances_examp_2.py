class DbUser:


    def __init__(self, user_id, user_name, current_permission=None):  # метод конструктор
        self.user_id = user_id
        self.user_name = user_name
        self.current_permission = current_permission


    def get_current_permission(self):
        # апит кудись
        self.current_permission == ['View', 'Delete']


main_user = DbUser(1, 'Ivan')

if main_user.current_permission is None:
    main_user.get_current_permission()

