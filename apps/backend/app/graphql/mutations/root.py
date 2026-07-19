import strawberry
from app.graphql.mutations.auth.auth import AuthMutation
from app.graphql.mutations.files.client.uploaded_file.uploaded_file import FileMutation

@strawberry.type
class Mutation(AuthMutation, FileMutation):
    pass