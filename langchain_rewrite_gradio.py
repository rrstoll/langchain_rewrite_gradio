# 📌 Import dependencies
import os
from dotenv import load_dotenv
import gradio as gr
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()  # This loads environment variables from the .env file
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it in your .env file.")

# 📌 Initialize the OpenAI Chat model
llm = ChatOpenAI(temperature=0.3, api_key=api_key)

# 📌 Define prompt template
prompt = ChatPromptTemplate.from_template(
    "Rewrite the following text in a {style} tone:\n\n{text}"
)

# Create the output parser
output_parser = StrOutputParser()

# Compose the chain using LangChain Expression Language
chain = prompt | llm | output_parser

# Define the Gradio interface function
def rewrite_text(text, style):
    if not text or not style:
        return "Please enter text and select a style."
    return chain.invoke({"text": text, "style": style})

# 📌 Gradio UI layout
with gr.Blocks() as demo:
    gr.Markdown("# ✍️ Rewrite & Style Transformer")
    gr.Markdown("Transform your text into different tones with the power of LangChain + GPT.")
    
    with gr.Row():
        text_input = gr.Textbox(label="Enter text", placeholder="e.g., Let's have a meeting to discuss the project.", lines=4)
    
    style_choice = gr.Dropdown(
        choices=["Professional", "Casual", "Poetic", "Inspirational", "Goblin"],
        label="Select Style"
    )

    submit_button = gr.Button("Rewrite")
    output_text = gr.Textbox(label="Rewritten Text", lines=4)
    
    submit_button.click(rewrite_text, inputs=[text_input, style_choice], outputs=output_text)

# 📌 Run the app
if __name__ == "__main__":
    demo.launch()