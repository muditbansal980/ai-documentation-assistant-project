"use client"
import {useState} from "react"
import {useParams} from "next/navigation"
import {SendingMessage} from "@/api/sending_message/client_sending_message"
export default function ChatInterface() {
    const [senderMessage, setSenderMessage] = useState("")
    const {documentId} = useParams()
    async function handleSendMessage() {
        const chatting  = await SendingMessage(senderMessage, String(documentId))
        console.log(chatting)
    }

    return (
        <div>
            <div>
                <input onChange = {(e) => setSenderMessage(e.target.value)} type="text" placeholder="Type your message here..." />
                <button onClick={handleSendMessage}>Send</button>
            </div>
            <div className="response">
                <p>Chatting response will come here after sending a message from LLM.</p>
            </div>
        </div>
    )
}