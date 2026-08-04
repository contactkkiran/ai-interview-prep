from payments import PaymentService
from users import UserService


def main():
    user_service = UserService()
    payment_service = PaymentService()

    user = user_service.get_user("user-123")
    result = payment_service.charge_user(user, amount=499)

    print(result)


if __name__ == "__main__":
    main()

