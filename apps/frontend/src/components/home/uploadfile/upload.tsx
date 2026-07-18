"use client"
import { useRef} from "react";
import { UploadFile } from "@/api/file_upload/file_upload";

export default function UploadFiles() {
    const fileInputRef = useRef<HTMLInputElement>(null);
    const uploadFile = async (
        e: React.ChangeEvent<HTMLInputElement>
    ) => {
        if (!e.target.files || e.target.files.length === 0) {
            console.log("No file selected");
            return;
        }
        if(e.target.files[0].type !== "application/pdf") {
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
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <div>
            <input accept=".pdf,application/pdf" type="file" ref={fileInputRef} onChange={uploadFile} />
            <button onClick={() => fileInputRef.current?.click()}>
                Upload
            </button>
        </div>
    )
}