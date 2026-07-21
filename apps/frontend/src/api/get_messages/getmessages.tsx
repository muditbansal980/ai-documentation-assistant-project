import { BACKEND_URL } from "../../config/app";
import { GET_CONVERSATIONAL_MESSAGES } from "../../graphql/queries/convo_messages/convomessages";
export async function getConversationalMessages(docId: string) {

    const variables = { docId };
    const token = localStorage.getItem("auth_token");

    const response = await fetch(`${BACKEND_URL}/graphql`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ query: GET_CONVERSATIONAL_MESSAGES, variables }),
    });

    const result = await response.json();
    console.log("Fetched messages:", result.data.getConversationalMessages);
    return result.data.getConversationalMessages;
}