"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
import { LoginUser } from "@/api/auth/auth";

export function HandleLogin(
    data: { Email: string; Password: string },
    router: ReturnType<typeof useRouter>
) {
    LoginUser(data).then((result) => {
        if (result?.data?.LoginUser?.authToken === "None") {
            alert("Login failed");
            return;
        }
        if (result?.data?.LoginUser?.authToken) {
            localStorage.setItem("auth_token", result.data.LoginUser.authToken);
            router.push("/home");
        }
    });
}

export default function LoginForm() {
    const router = useRouter();
    const [formData, setFormData] = useState({ email: "", password: "" });

    return (
        <div className="min-h-screen text-black bg-white flex items-center justify-center p-6">
            <motion.div
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                className="w-full max-w-md border-4 border-black p-8 shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] bg-white"
            >
                <h1 className="text-4xl font-black text-black uppercase mb-8 border-b-4 border-black pb-4">
                    Login
                </h1>

                <div className="flex flex-col gap-4">
                    <input
                        type="email"
                        placeholder="EMAIL"
                        className="border-2 border-black p-3 outline-none focus:border-red-600 transition-colors uppercase placeholder:text-gray-400 font-semibold"
                        value={formData.email}
                        onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                    />

                    <input
                        type="password"
                        placeholder="PASSWORD"
                        className="border-2 border-black p-3 outline-none focus:border-red-600 transition-colors placeholder:text-gray-800 font-semibold"
                        value={formData.password}
                        onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                    />

                    <motion.button
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                        onClick={() =>
                            HandleLogin(
                                {
                                    Email: formData.email,
                                    Password: formData.password,
                                },
                                router
                            )
                        }
                        className="bg-yellow-400 text-black font-bold uppercase p-4 border-2 border-black hover:bg-blue-600 hover:text-white transition-colors cursor-pointer"
                    >
                        Login
                    </motion.button>
                </div>

                <button
                    onClick={() => router.push("/")}
                    className="mt-6 text-sm font-bold underline hover:text-red-600 block uppercase cursor-pointer"
                >
                    Don&apos;t have an account? Register
                </button>
            </motion.div>
        </div>
    );
}