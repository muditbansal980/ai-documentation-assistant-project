import strawberry

def get_current_user(info: strawberry.Info) -> dict:
    user = info.context["user"]
    if not user:
        return None  # Return None if the user is not authenticated
    return user