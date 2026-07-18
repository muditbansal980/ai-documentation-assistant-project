import uuid 
from sqlalchemy import select
from app.db.session import AsyncSessionLocal
from app.models.users.user import User
from app.schemas.auth.login import UserLoginSchema
from app.schemas.auth.register import UserRegisterSchema
from pwdlib import PasswordHash
from app.services.auth.auth import create_access_token

async def register_user(register_data: UserRegisterSchema):
    try: 
        password_hash = PasswordHash.recommended()
        async with AsyncSessionLocal() as session:
            user = User(
                Id = str(uuid.uuid4()),
                Username = register_data.Username,
                Email = register_data.Email,
                Password = password_hash.hash(register_data.Password)
            )
            session.add(user)
            await session.commit()
            return {"message": "User registered successfully", "user_id": str(user.Id)}
    except Exception as e:
        return {"error": str(e)}


async def login_user(login_data: UserLoginSchema):
    try:
        logindata = login_data
        password_hash = PasswordHash.recommended()
        print("Logging in user with data:", logindata)
        async with AsyncSessionLocal() as session:
            query = await session.execute(
            select(User).where(
                User.Email == login_data.Email
            )
        )
            user = query.scalar_one_or_none()
            
            print("User found:", user)
            if(user is None):
                return {"message": "No such user found"}
            else:
                # Create a JWT token for the user
                token = create_access_token(
                    data={"sub": str(user.Id), "username": user.Username, "email": user.Email}
                )
                if(password_hash.verify(login_data.Password, user.Password)):
                    return {"message": "Login successful", "auth_token": token}
                else:
                    return {"message": "Incorrect password"}
    except Exception as e:
        return {"error": str(e)}
