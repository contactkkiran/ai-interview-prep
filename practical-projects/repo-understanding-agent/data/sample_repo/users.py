class UserService:
    def get_user(self, user_id):
        return {
            "id": user_id,
            "name": "Kiran",
            "active": True,
        }


def is_active_user(user):
    return user.get("active") is True

