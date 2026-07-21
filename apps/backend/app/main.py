from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import UPLOAD_DIR
from app.graphql.schema import schema
from fastapi.security import OAuth2PasswordBearer
from app.graphql.context import get_context
import os 

app = FastAPI()

FRONTEND_URL = os.getenv("FRONTEND_URL")  # Default to localhost if not set
graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context, # this lines connects the strawberry context to the FastAPI request context, allowing you to access the user information in your resolvers
    multipart_uploads_enabled=True,
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/graphql"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True, 
)


app.include_router(
    graphql_app,
    prefix="/graphql"
)
