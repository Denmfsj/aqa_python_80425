class UserAgeException(Exception):

    def __init__(self, age):
        message = f'You have no discount at your {age}'
        super().__init__(message)

class ItemValidationException(Exception):

    def __init__(self, item_name, item_id):
        message = f'You cant buy this {item_name} with id = {item_id} with discount'
        super().__init__(message)



def discount(user_age, product_id):

    products_without_discount = [1,2,3,4]

    if 18 < user_age < 60:  # if user_age > 18 AND user_age < 60
        raise UserAgeException(user_age)

    if product_id in products_without_discount:
        raise ItemValidationException(item_name='product', item_id=product_id)

    return 0.01  # 1%

try:
    discount(user_age=99, product_id=3)
except UserAgeException:
    print('You are to yang for this')


