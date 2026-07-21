"use client";

import { useState, useEffect, useRef } from "react";
import { useParams } from "next/navigation";
import { motion, AnimatePresence } from "framer-motion";
import { SendingMessage } from "@/api/sending_message/client_sending_message";
import { getConversationalMessages } from "@/api/get_messages/getmessages";
import Sidebar from "@/components/layouts/sidebar";

type ConversationalMessage = {
    Id: string;
    DocId: string;
    UserId: string;
    Message: string;
    Response: string;
};

export default function ChatInterface() {
    const [senderMessage, setSenderMessage] = useState("");
    const [loading, setLoading] = useState(false);
    const { documentId } = useParams();
    const [conversationalMessages, setConversationalMessages] = useState<ConversationalMessage[]>([]);
    const chatBottomRef = useRef<HTMLDivElement>(null);

    // const fetchMessages = async () => {
    //     if (!documentId) return;
    //     const messages = await getConversationalMessages(String(documentId));
    //     setConversationalMessages(messages || []);
    // };

    useEffect(() => {

        async function fetchMessages() {

            const messages = await getConversationalMessages(String(documentId))

            setConversationalMessages(messages)

        }

        fetchMessages()

    }, [documentId])

    // Auto-scroll to bottom on new messages
    useEffect(() => {
        chatBottomRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [conversationalMessages, loading]);

    async function handleSendMessage() {
        if (!senderMessage.trim() || loading) return;

        const currentMsg = senderMessage;
        setSenderMessage("");
        setLoading(true);

        try {
            await SendingMessage(currentMsg, String(documentId));
            // await fetchMessages();
        } catch (error) {
            console.error("Error sending message:", error);
        } finally {
            setLoading(false);
        }
    }

    return (
        <div className="min-h-screen bg-white flex flex-col items-center p-4 md:p-8">
            <Sidebar />
            <div className="w-full max-w-4xl border-4 border-black shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] bg-white flex flex-col h-[85vh]">

                {/* Bauhaus Header */}
                <div className="border-b-4 border-black p-4 bg-yellow-400 flex items-center justify-between">
                    <h1 className="text-2xl md:text-3xl font-black uppercase tracking-tight">
                        Document Chat
                    </h1>
                    <span className="bg-black text-white px-3 py-1 text-xs font-bold uppercase tracking-wider">
                        ID: {String(documentId).slice(0, 8)}...
                    </span>
                </div>

                {/* Message Feed Container */}
                <div className="flex-1 overflow-y-auto p-4 md:p-6 space-y-6 bg-slate-50">
                    {conversationalMessages.length === 0 && !loading && (
                        <div className="h-full flex items-center justify-center">
                            <p className="border-2 border-black p-4 bg-white font-bold uppercase text-gray-500 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
                                Ask a question to begin the conversation
                            </p>
                        </div>
                    )}

                    <AnimatePresence initial={false}>
                        {conversationalMessages.map((message, index) => (
                            <motion.div
                                key={message.Id || index}
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                className="space-y-3"
                            >
                                {/* User Message (Blue accent) */}
                                <div className="flex justify-end">
                                    <div className="max-w-[85%] md:max-w-[75%] border-2 border-black bg-blue-600 text-white p-4 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] font-semibold">
                                        <span className="block text-[10px] font-black uppercase text-blue-200 mb-1">
                                            YOU
                                        </span>
                                        {message.Message}
                                    </div>
                                </div>

                                {/* LLM Response (White container with Red accent header) */}
                                <div className="flex justify-start">
                                    <div className="max-w-[85%] md:max-w-[75%] border-2 border-black bg-white text-black p-4 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] font-medium">
                                        <span className="block text-[10px] font-black uppercase text-red-600 mb-1">
                                            SYSTEM RESPONSE
                                        </span>
                                        {message.Response}
                                    </div>
                                </div>
                            </motion.div>
                        ))}
                    </AnimatePresence>

                    {/* Loading Indicator */}
                    {loading && (
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            className="flex justify-start"
                        >
                            <div className="border-2 border-black bg-red-600 text-white p-3 font-black uppercase text-xs animate-pulse shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
                                Do not refresh the page.Please wait while we process your response...
                            </div>
                        </motion.div>
                    )}

                    <div ref={chatBottomRef} />
                </div>

                {/* Input Bar */}
                <div className="border-t-4 border-black p-4 bg-white flex flex-col sm:flex-row gap-3">
                    <input
                        type="text"
                        placeholder="TYPE YOUR QUESTION HERE..."
                        value={senderMessage}
                        onChange={(e) => setSenderMessage(e.target.value)}
                        onKeyDown={(e) => e.key === "Enter" && handleSendMessage()}
                        className="flex-1 border-2 border-black p-3 font-semibold uppercase outline-none focus:border-red-600 placeholder:text-gray-600 text-black"
                    />
                    <motion.button
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                        onClick={handleSendMessage}
                        disabled={loading}
                        className="bg-black text-white font-black uppercase px-8 py-3 hover:bg-yellow-400 hover:text-black border-2 border-black transition-colors cursor-pointer disabled:opacity-50"
                    >
                        Send
                    </motion.button>
                </div>

            </div>
        </div>
    );
}