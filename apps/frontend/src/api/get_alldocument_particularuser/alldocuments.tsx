import {BACKEND_URL} from "../../config/app";
import { GET_ALL_DOCUMENTS_OF_PARTICULAR_USER } from "../../graphql/queries/alldocuments_particularuser/fetchingalldocumentsofparticualruser";

export async function getAllDocumentsOfParticularUser() {
    const token = localStorage.getItem("auth_token");

    const response = await fetch(`${BACKEND_URL}/graphql`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ query: GET_ALL_DOCUMENTS_OF_PARTICULAR_USER }),
    });

    const result = await response.json();
    console.log("Fetched documents:", result.data);
    return result.data.getAllDocumentsUser;
}   