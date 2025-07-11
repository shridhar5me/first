import openai
openai.api_key = "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"

def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:

Email:
{email_text}

Reply:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content