export const GET_CONVERSATIONAL_MESSAGES = `
    query GetConversationalMessages($docId: String!) {
        getConversationalMessages(docId: $docId) {
            Id
            DocId
            UserId
            Message
            Response
            CreatedAt
        }
    }
`;