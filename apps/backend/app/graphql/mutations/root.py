import strawberry
from app.graphql.mutations.auth.auth import AuthMutation
from app.graphql.mutations.files.client.uploaded_file.uploaded_file import FileMutation
from app.graphql.mutations.client_messages.client_message import ClientMessageMutation
@strawberry.type
class Mutation(AuthMutation, FileMutation,ClientMessageMutation):
    pass