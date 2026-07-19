import strawberry

def get_current_user(info: strawberry.Info) -> dict:
    user = info.context["user"]
    if not user:
        print("<-------------------No user error in get_current_user-------------------->\n\n\n\n")
        print("<-------------------No user error in get_current_user-------------------->")
        return None  # Return None if the user is not authenticated
    return user