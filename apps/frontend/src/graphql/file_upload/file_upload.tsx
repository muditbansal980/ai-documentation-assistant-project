export const UPLOAD_FILE_MUTATION = `
mutation UploadFile(
    $file:Upload!,
){
    UploadFile(
            file:$file
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