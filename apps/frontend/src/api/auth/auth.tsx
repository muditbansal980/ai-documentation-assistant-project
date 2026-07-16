import { BACKEND_URL } from "@/config/app"
import { RegisterUserInput } from "@/types/auth/authtypes"
import { REGISTER_MUTATION } from "@/graphql/auth/auth"
import { LOGIN_MUTATION } from "@/graphql/auth/auth"
export async function RegisterUser(data: RegisterUserInput) {
    console.log("BACKEND_URL", BACKEND_URL)
    console.log("REGISTER_MUTATION", REGISTER_MUTATION)
    console.log("data", data)
    const response = await fetch(`${BACKEND_URL}/graphql`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            query: REGISTER_MUTATION,
            variables: data
        })

    });
    console.log("response", response)
    const result = await response.json();
    return result;
}

export async function LoginUser(data: { Email: string, Password: string }) {
    const response = await fetch(`${BACKEND_URL}/graphql`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            query: LOGIN_MUTATION,
            variables: data
        })
    });
    const result = await response.json();
    return result;
}