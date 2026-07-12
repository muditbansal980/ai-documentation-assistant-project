"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Register(){
    const router = useRouter();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    return (
        <div>
            <h1>Login</h1>
            <input 
                type="email" 
                placeholder="Email" 
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            <input 
                type="password" 
                placeholder="Password" 
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <div>
                <button onClick={() => router.push("/register")}>Don&apos;t have an account? Register</button>
            </div>
        </div>
    )
}