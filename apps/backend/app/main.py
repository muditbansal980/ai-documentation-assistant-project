from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import UPLOAD_DIR
from app.graphql.schema import schema

app = FastAPI()

graphql_app = GraphQLRouter(
    schema,
    multipart_uploads_enabled=True,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True, 
)


app.include_router(
    graphql_app,
    prefix="/graphql"
)
