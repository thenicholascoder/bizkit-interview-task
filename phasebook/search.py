from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

# original method
# def search_users(args):
#     """Search users database

#     Parameters:
#         args: a dictionary containing the following search parameters:
#             id: string
#             name: string
#             age: string
#             occupation: string

#     Returns:
#         a list of users that match the search parameters
#     """

#     # Implement search here!

#     return USERS

# Search algorithm
# def search_users(args):
#     id = args.get("id")
#     name = args.get("name", "").lower()
#     age = args.get("age")
#     occupation = args.get("occupation", "").lower()

#     def match_user(user):
#         if id and user["id"] == id:
#             return True
#         if name and name in user["name"].lower():
#             return True
#         if age and abs(int(user["age"]) - int(age)) <= 1:
#             return True
#         if occupation and occupation in user["occupation"].lower():
#             return True
#         return False

#     return [user for user in USERS if match_user(user)]

# Bonus challenge
def search_users(args):
    id = args.get("id")
    name = args.get("name", "").lower()
    age = args.get("age")
    occupation = args.get("occupation", "").lower()

    def match_priority(user):
        priority = 0
        if id and user["id"] == id:
            priority -= 4
        if name and name in user["name"].lower():
            priority -= 3
        if age and abs(int(user["age"]) - int(age)) <= 1:
            priority -= 2
        if occupation and occupation in user["occupation"].lower():
            priority -= 1
        return priority

    matched_users = [user for user in USERS if match_priority(user) < 0]
    return sorted(matched_users, key=match_priority)