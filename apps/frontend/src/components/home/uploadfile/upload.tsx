"use client"
import { useRef} from "react";
import { UploadFile } from "@/api/file_upload/file_upload";

export default function UploadFiles() {
    const fileInputRef = useRef<HTMLInputElement>(null);
    const uploadFile = async (
        e: React.ChangeEvent<HTMLInputElement>
    ) => {
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
            <input type="file" ref={fileInputRef} onChange={uploadFile} />
            <button onClick={() => fileInputRef.current?.click()}>
                Upload
            </button>
        </div>
    )
}