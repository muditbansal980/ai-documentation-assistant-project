from app.db.session import AsyncSessionLocal
import ollama


async def generate_response(
    client_message: str,
    context: list[str]
):
    try:

        context_text = "\n\n".join(context)

        system_prompt = """
You are an AI Document Assistant.
You will answer questions based on the provided context. If the answer is not present in the context, you will respond with "I could not find this information in the document." You will not make up information. You will keep your answers concise and professional. If possible, you will mention page numbers if they are present in the context.
Also you should provide a clear answer about the document and minimum you should respond in 30 words.Also if someone gives a greeting message than respond with greeting message + your intro and work.
Rules:
1. Answer ONLY using the provided context.
2. If the answer is not present in the context, say:
   "I could not find this information in the document."
3. Never make up information.
4. Keep answers concise and professional.
5. If possible, mention page numbers if they are present in the context.
"""

        prompt = f"""
Context:
{context_text}

Question:
{client_message}

Answer:
"""

        response = ollama.chat(
            model="gemma2:2b",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        print("<-------------------Response from Ollama-------------------->\n\n\n\n")
        print("Response:", response["message"]["content"])
        print("<-------------------Response from Ollama-------------------->\n\n\n\n")
        return response["message"]["content"]

    except Exception as e:
        return str(e)
    