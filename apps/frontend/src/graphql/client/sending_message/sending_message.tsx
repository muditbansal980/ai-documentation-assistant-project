export const SENDING_MESSAGE_MUTATION = `
mutation SendingMessage(
    $message: String!, 
    $documentId: String!
){
    ClientMessage(
            message: $message, 
            documentId: $documentId
    ){
            __typename
        ... on MessageResponse {
            message
        }
        ... on AuthError {
            message
            statusCode
        }
    }
}
`