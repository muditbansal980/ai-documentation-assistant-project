export const UPLOAD_FILE_MUTATION = `
mutation UploadFile(
    $file:Upload!,
){
    UploadFile(
            file:$file
    ){
        message
    }
}
`