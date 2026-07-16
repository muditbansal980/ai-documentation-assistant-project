import uuid 
from sqlalchemy import select
from app.db.session import AsyncSessionLocal
from app.models.users.user import User
from app.schemas.auth.login import UserLoginSchema
from app.schemas.auth.register import UserRegisterSchema


async def register_user(register_data: UserRegisterSchema):
    try: 
        print("Registering user with data:", register_data)
        async with AsyncSessionLocal() as session:
            user = User(
                Id = str(uuid.uuid4()),
                Username = register_data.Username,
                Email = register_data.Email,
                Password = register_data.Password
            )
            session.add(user)
            await session.commit()
            return {"message": "User registered successfully", "user_id": str(user.Id)}
    except Exception as e:
        return {"error": str(e)}


async def login_user(login_data: UserLoginSchema):
    try:
        logindata = login_data
        print("Logging in user with data:", logindata)
        async with AsyncSessionLocal() as session:
            query = await session.execute(
            select(User).where(
                User.Email == login_data.Email
            )
        )
            user = query.scalar_one_or_none()
            if(user is None):
                return {"message": "No such user found"}
            else:
                if(user.Password == logindata.Password):
                    return {"message": "Login successful"}
                else:
                    return {"message": "Incorrect password"}
    except Exception as e:
        return {"error": str(e)}
