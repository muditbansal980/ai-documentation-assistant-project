import { BACKEND_URL } from "@/config/app";
import { UPLOAD_FILE_MUTATION } from "@/graphql/file_upload/file_upload";
export async function UploadFile(file: File) {
    console.log("Uploading file: " + file.name);
    const formData = new FormData();

    formData.append(
        "operations",
        JSON.stringify({
            query: UPLOAD_FILE_MUTATION,
            variables: {
                file: null,
            },
        })
    );

    formData.append(
        "map",
        JSON.stringify({
            "0": ["variables.file"],
        })
    );

    formData.append("0", file);
    for (const [key, value] of formData.entries()) {
        console.log(key, value);
    }
    const token = localStorage.getItem("auth_token");
    const response = await fetch(
        `${BACKEND_URL}/graphql`,
        {
            method: "POST",
            body: formData,
            headers: {
                "Authorization": `Bearer ${token}`
            }
        }
    );

    const result = await response.json();
    if(result.data?.UploadFile?.__typename === "AuthError") {
        if(result.data.UploadFile.statusCode === 401) {
            alert("You are not authenticated. Please log in.");
        } else {
            alert(`Error: ${result.data.UploadFile.message}`);
        }
    }
    if (result.errors) {
        console.log("Error:", result.errors);
    }

    console.log(result);
    return result;
}

