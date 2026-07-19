import {BACKEND_URL} from "@/config/app"
import {SENDING_MESSAGE_MUTATION} from "@/graphql/client/sending_message/sending_message"

export async function SendingMessage(message:string, documentId: string) {
    const token = localStorage.getItem("auth_token");
    try {
        console.log("Sending message:", message, "to documentId:", documentId);
        const response = await fetch(`${BACKEND_URL}/graphql`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify({
                query: SENDING_MESSAGE_MUTATION,
                variables: {
                    message: message,
                    documentId: documentId
                }
            })
        });

        if (!response.ok) {
            throw new Error("Failed to send message");
        }
        const data = await response.json();
        alert("Message sent successfully: " + data.data.ClientMessage.message);
        return data;
    } catch (error) {
        console.error("Error sending message:", error);
        throw error;
    }
}