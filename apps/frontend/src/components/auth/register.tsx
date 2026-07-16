"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { RegisterUserInput } from "@/types/auth/authtypes";
import {RegisterUser} from "@/api/auth/auth"



function handleRegister(data:RegisterUserInput){
    RegisterUser(data).then((result)=>{
        console.log(result)
    })
}

export default function Register(){
    const router = useRouter();
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    return (
        <div>
            <h1>Register</h1>
            <input 
                type="text" 
                placeholder="Username" 
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />
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
                handleRegister({
                    Username: username,
                    Email: email,
                    Password: password
                })
            }}>
                Register
            </button>
            <div>
                <button onClick={() => router.push("/login")}>Already have an account</button>
            </div>
        </div>
    )
}