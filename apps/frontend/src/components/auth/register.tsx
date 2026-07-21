"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
// import { RegisterUserInput } from "@/types/auth/authtypes";
import { RegisterUser } from "@/api/auth/auth";

export default function Register() {
  const router = useRouter();
  const [formData, setFormData] = useState({ username: "", email: "", password: "" });

  const handleRegister = async () => {
    await RegisterUser({
      Username: formData.username,
      Email: formData.email,
      Password: formData.password,
    });
  };

  return (
    <div className="min-h-screen bg-white text-black flex items-center justify-center p-6">
      <motion.div 
        initial={{ opacity: 0, x: -20 }}
        animate={{ opacity: 1, x: 0 }}
        className="w-full max-w-md border-4 border-black p-8 shadow-[12px_12px_0px_0px_rgba(0,0,0,1)]"
      >
        <h1 className="text-4xl font-black uppercase mb-8 border-b-4 border-black pb-4">
          Register
        </h1>

        <div className="flex flex-col gap-4 text-black">
          {["username", "email", "password"].map((field) => (
            <input
              key={field}
              type={field === "password" ? "password" : "text"}
              placeholder={field.toUpperCase()}
              className="border-2 text-black border-black p-3 outline-none focus:border-red-600 transition-colors"
              value={formData[field as keyof typeof formData]}
              onChange={(e) => setFormData({ ...formData, [field]: e.target.value })}
            />
          ))}

          <motion.button
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            onClick={handleRegister}
            className="bg-blue-600 text-white font-bold uppercase p-4 border-2 border-black hover:bg-yellow-400 hover:text-black transition-colors"
          >
            Register
          </motion.button>
        </div>

        <button 
          onClick={() => router.push("/login")}
          className="mt-6 text-sm font-bold underline hover:text-red-600"
        >
          ALREADY HAVE AN ACCOUNT?
        </button>
      </motion.div>
    </div>
  );
}