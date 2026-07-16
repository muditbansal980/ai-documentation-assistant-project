"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { LoginUser } from "@/api/auth/auth";

function handleLogin(data: { Email: string; Password: string }) {
    LoginUser(data).then((result)=>{
        console.log("Final Result:", result)
    })
}
export default function LoginForm(){
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
            <button onClick={()=>{
                handleLogin({
                    Email: email,
                    Password: password
                })
            }}>
                Login
            </button>
            <div>
                <button onClick={() => router.push("/")}>Don&apos;t have an account? Register</button>
            </div>
        </div>
    )
}