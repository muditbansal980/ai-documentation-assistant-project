"use client"
import { useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation"
import { UploadFile } from "@/api/file_upload/file_upload";

export default function UploadFiles() {

    const fileInputRef = useRef<HTMLInputElement>(null);
    const [documentId, setDocumentId] = useState<string | null>(null);
    const router = useRouter();
    const uploadFile = async (
        e: React.ChangeEvent<HTMLInputElement>
    ) => {
        if (!e.target.files || e.target.files.length === 0) {
            console.log("No file selected");
            return;
        }
        if (e.target.files[0].type !== "application/pdf") {
            alert("Invalid file type. Please select a PDF file.");
            return;
        }
        console.log("onChange fired");
        const file = e.target.files?.[0];

        if (!file) return;

        try {
            console.log("Uploading file: " + file.name);
            const result = await UploadFile(file);
            console.log(result);
            if (result.data.UploadFile.__typename === "SuccessfulFileUploadMessage") {
                setDocumentId(result.data.UploadFile.documentId);
                console.log("File uploaded successfully. Document ID: " + result.data.UploadFile.documentId);

            } else {
                console.log("Error uploading file: " + result.data.UploadFile.message);
            }
        } catch (error) {
            console.log(error);
        }
    };
    useEffect(()=>{
        if(documentId){
            router.push(`/chat/${documentId}`);
        }
        return;
    },[documentId, router])
    return (
        <div>
            <input accept=".pdf,application/pdf" type="file" ref={fileInputRef} onChange={uploadFile} />
            <button onClick={() => fileInputRef.current?.click()}>
                Upload
            </button>
        </div>
    )
}