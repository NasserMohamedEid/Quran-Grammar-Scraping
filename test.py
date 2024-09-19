import sys
import pandas as pd
import google.generativeai as genai

sys.stdout.reconfigure(encoding='utf-8')

api_key = "AIzaSyAEK-OhZlcbgIR1IQ9bITZycb7KrCA_idk"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-pro-001')




# Example dataframe with Arabic sentences
data = {'sentence': ['بِسْمِ اللهِ الرَّحْمنِ الرَّحِيمِ', 'الْحَمْدُ لِلّهِ رَبِّ الْعالَمِينَ', 'الرَّحْمنِ الرَّحِيمِ']}
df = pd.DataFrame(data)

context = "You are an expert in Arabic grammatical analysis. Please analyze the following sentences in arabic only and provide their full grammatical structure (إعراب)and be short ."

# Function to send sentence to model and collect response
def get_responses_with_context(df):
    responses = []
    for index, row in df.iterrows():
        sentence = row['sentence']
        # Adding context to the prompt for Arabic grammar analysis
        context_prompt = (
            f"{context}"
            f"{sentence}"
        )
        try:
            response = model.generate_content(context_prompt)
            responses.append(response.text)
        except Exception as e:
            responses.append(f"Error: {e}")
    return responses

# Call the function and store the responses in the dataframe
df['response'] = get_responses_with_context(df)

# Display the updated dataframe with responses
print(df['response'][0])
print(df['response'][1])
print(df['response'][2])