# count quantity of items of all clients
orders = [
    {
        "client": {
            "id": 1,
            "name": "Ivan",
            "orders": [
                {"id": 101, "items": [{"product": "apple", "qty": 2}, {"product": "banana", "qty": 3}]},
                {"id": 102, "items": [{"product": "apple", "qty": 1}]}
            ]
        }
    },
    {
        "client": {
            "id": 2,
            "name": "Olga",
            "orders": [
                {"id": 103, "items": [{"product": "banana", "qty": 2}, {"product": "orange", "qty": 5}]}
            ]
        }
    }
]

#  average grade
students = {
    "student": {
        "name": "Petro",
        "profile": {
            "id": 42,
            "courses": [
                {"title": "Math", "grades": [90, 85, 100]},
                {"title": "History", "grades": [70, 75]},
                {"title": "Biology", "grades": [88, 92]}
            ]
        }
    }
}

# users with gmail
company = {
    "organization": {
        "name": "Tech Corp",
        "departments": [
            {
                "name": "IT",
                "employees": [
                    {"name": "Anna", "contacts": {"email": "anna@gmail.com"}},
                    {"name": "Bohdan", "contacts": {"email": "bohdan@corp.com"}}
                ]
            },
            {
                "name": "HR",
                "employees": [
                    {"name": "Ira", "contacts": {"email": "ira@gmail.com"}},
                    {"name": "Oleksii", "contacts": {"email": "oleksii@corp.com"}}
                ]
            }
        ]
    }
}


#################################################################
# add property is progress or done
statuses = {
    "projects": [
        {
            "name": "Alpha",
            # додати property is_completed: bool, True якщо всі tasks.done == True в іншому випадку is_completed = Fasle
            "team": {
                "members": [
                    {"name": "Ivan", "tasks": [
                        {"title": "Dev", "done": False},
                        {"title": "Setup", "done": True}]
                     }
                ]
            }
        },
        {
            "name": "Beta",
            "team": {
                "members": [
                    {"name": "Oksana", "tasks": [
                        {"title": "Research", "done": True},
                        {"title": "Deploy", "done": True}]
                     }
                ]
            }
        }
    ]
}

# codewars

# for project in statuses['projects']:  # project це словник
#     project['is_completed'] = True  # проект закінчений
#
#     for member in project['team']['members']:
#         for task in member['tasks']:
#             if task['done'] is False:
#                 project['is_completed'] = False
#                 break
#
#         if project['is_completed'] is False:
#             break


# for project in statuses['projects']:  # project це словник
#     is_completed = True  # делолтне значення
#
#     tasks_statuses = []
#
#     for member in project['team']['members']:
#         for task in member['tasks']:
#             tasks_statuses.append(task['done'])  # додаю булеві значення
#
#     if False in tasks_statuses:
#         is_completed = False  # не всі таски зроблені
#
#     project['is_completed'] = is_completed



# # print unique skills
# skills = [
#     {
#         "user": {
#             "name": "Andriy",
#             "profile": {
#                 "skills": ["python", "docker", "linux"]
#             }
#         }
#     },
#     {
#         "user": {
#             "name": "Liza",
#             "profile": {
#                 "skills": ["python", "aws", "linux"]
#             }
#         }
#     },
#     {
#         "user": {
#             "name": "Marta",
#             "profile": {
#                 "skills": ["git", "docker", "aws"]
#             }
#         }
#     }
# ]

# unique_skills = set()
#
# for user_object in skills:
#     # print(user_object)
#
#     user_profile = user_object.get('user').get('profile')
#     user_skills = user_profile.get("skills")
#     print(user_skills)
#     unique_skills = unique_skills.union(user_skills)
#     # unique_skills.update(user_skills)
#
#
#     # user_skills = user_object.get('user').get('profile').get("skills")
#     # print(f'profile = {user_profile}')
#     # print(f'skills = {user.get("profile")["skills"]}')
# print(unique_skills)
