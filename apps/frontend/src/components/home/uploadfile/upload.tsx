"use client";

import { useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
import { UploadFile } from "@/api/file_upload/file_upload";

export default function UploadFiles() {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [documentId, setDocumentId] = useState<string | null>(null);
  const [isUploading, setIsUploading] = useState(false);
  const [selectedFileName, setSelectedFileName] = useState<string | null>(null);
  const router = useRouter();

  const uploadFile = async (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!e.target.files || e.target.files.length === 0) {
      console.log("No file selected");
      return;
    }

    const file = e.target.files[0];

    if (file.type !== "application/pdf") {
      alert("Invalid file type. Please select a PDF file.");
      return;
    }

    setSelectedFileName(file.name);
    setIsUploading(true);

    try {
      console.log("Uploading file: " + file.name);
      const result = await UploadFile(file);
      console.log(result);

      if (result?.data?.UploadFile?.__typename === "SuccessfulFileUploadMessage") {
        setDocumentId(result.data.UploadFile.documentId);
        console.log("File uploaded successfully. Document ID: " + result.data.UploadFile.documentId);
      } else {
        console.log("Error uploading file: " + result?.data?.UploadFile?.message);
        setIsUploading(false);
      }
    } catch (error) {
      console.log(error);
      setIsUploading(false);
    }
  };

  useEffect(() => {
    if (documentId) {
      router.push(`/chat/${documentId}`);
    }
  }, [documentId, router]);

  return (
    <div className="min-h-screen text-black bg-white flex items-center justify-center p-6">
      <motion.div
        initial={{ opacity: 0, x: -20 }}
        animate={{ opacity: 1, x: 0 }}
        className="w-full max-w-lg border-4 border-black p-8 shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] bg-white"
      >
        <h1 className="text-4xl font-black uppercase mb-2 border-b-4 border-black pb-4">
          Upload File
        </h1>
        <p className="text-sm font-bold uppercase mb-8 text-gray-600">
          Select a PDF document to start chatting
        </p>

        {/* Hidden File Input */}
        <input
          accept=".pdf,application/pdf"
          type="file"
          ref={fileInputRef}
          onChange={uploadFile}
          className="hidden"
        />

        {/* Interactive Drop / Upload Area */}
        <div
          onClick={() => fileInputRef.current?.click()}
          className="border-4 border-dashed border-black p-10 text-center cursor-pointer bg-red-50 hover:bg-yellow-300 transition-colors flex flex-col items-center justify-center gap-4 group"
        >
          <div className="w-16 h-16 border-4 border-black bg-white flex items-center justify-center shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] group-hover:bg-red-600 group-hover:text-white transition-colors">
            <span className="text-2xl font-black">PDF</span>
          </div>

          <p className="font-black uppercase text-lg">
            {selectedFileName ? selectedFileName : "Click to select a PDF"}
          </p>
        </div>

        {/* Action Button */}
        <motion.button
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
          onClick={() => fileInputRef.current?.click()}
          disabled={isUploading}
          className="w-full mt-6 bg-red-600 text-white font-black uppercase p-4 border-2 border-black hover:bg-black hover:text-white transition-colors cursor-pointer disabled:opacity-50"
        >
          {isUploading ? "Uploading..." : "Browse Files"}
        </motion.button>
      </motion.div>
    </div>
  );
}