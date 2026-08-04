class PaymentService:
    def charge_user(self, user, amount):
        if not user["active"]:
            return "Cannot charge inactive user"

        return f"Charged {user['name']} amount {amount}"


def calculate_tax(amount):
    return amount * 0.18

