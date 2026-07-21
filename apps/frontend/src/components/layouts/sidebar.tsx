"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
import { getAllDocumentsOfParticularUser } from "../../api/get_alldocument_particularuser/alldocuments";

export default function Sidebar() {
  const [documents, setDocuments] = useState<
    { Id: string; UserId: string; OriginalFileName: string }[]
  >([]);
  const router = useRouter();

  useEffect(() => {
    async function fetchDocuments() {
      const docs = await getAllDocumentsOfParticularUser();
      setDocuments(docs || []);
    }

    fetchDocuments();
  }, []);

  return (
    <aside className="w-64 text-black bg-yellow-400 border-r-4 border-black h-screen fixed top-0 left-0 flex flex-col justify-between p-4 z-40">
      <div>
        {/* Header Section */}
        <div className="border-b-4 border-black pb-4 mb-6">
          <h2 className="text-xl font-black uppercase tracking-tight text-black">
            Documents
          </h2>
          <span className="text-xs font-bold text-black uppercase opacity-80">
            {documents.length} File{documents.length !== 1 ? "s" : ""} Loaded
          </span>
        </div>

        {/* Document List */}
        <ul className="space-y-3 overflow-y-auto max-h-[calc(100vh-180px)] pr-1">
          {documents.map((doc) => (
            <motion.li
              key={doc.Id}
              whileHover={{ x: 4 }}
              whileTap={{ scale: 0.98 }}
              onClick={() => router.push(`/chat/${doc.Id}`)}
              className="p-3 bg-white border-2 border-black font-bold uppercase text-xs shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:bg-red-600 hover:text-white transition-colors cursor-pointer truncate"
              title={doc.OriginalFileName}
            >
              📄 {doc.OriginalFileName}
            </motion.li>
          ))}

          {documents.length === 0 && (
            <li className="p-3 bg-white border-2 border-black font-bold uppercase text-xs text-gray-500 text-center">
              No documents
            </li>
          )}
        </ul>
      </div>

      {/* New Upload Button Accent */}
      <motion.button
        whileHover={{ scale: 1.02 }}
        whileTap={{ scale: 0.98 }}
        onClick={() => router.push("/home")}
        className="w-full bg-black text-white font-black uppercase p-3 border-2 border-black hover:bg-blue-600 transition-colors cursor-pointer text-xs"
      >
        + Upload New PDF
      </motion.button>
    </aside>
  );
}