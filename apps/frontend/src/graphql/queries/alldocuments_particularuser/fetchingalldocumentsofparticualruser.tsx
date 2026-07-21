export const GET_ALL_DOCUMENTS_OF_PARTICULAR_USER = `
    query GetAllDocumentsUser{
        getAllDocumentsUser {
            Id
            UserId
            OriginalFileName
        }
    }
`;  