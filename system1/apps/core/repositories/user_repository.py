from system1.apps.core.models import Users


class UserRepository:
    def find_by_id(self, user_id: int):
        user = Users.objects.filter(user_id=user_id).first()

        return user
    
    def find_all(self):
        users = Users.objects.filter(is_active=True)

        return users

    def create(self, name: str, email: str, password: str):
        user = Users.objects.create(
            username=name,
            email=email
        )
        user.set_password(password)
        user.save()

        return user