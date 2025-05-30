# Rewrite & Style Transformer

Rewrite & Style Transformer is an AI-powered application that transforms text into different tones and writing styles using LangChain 1.0, OpenAI GPT models, and Gradio. This tool demonstrates practical AI workflows by combining prompt templates, language models, and a user-friendly interface.

---

## 🚀 Features

✅ Transform text into **Professional**, **Casual**, **Poetic**, **Inspirational** or **Goblin** styles  
✅ Built with **LangChain 1.0** and **OpenAI GPT models**  
✅ Clean, interactive UI using **Gradio**  
✅ Modular design for easy extension and customization  

---

## 📦 Project Structure

```

rewrite-transformer/
├── rewrite\_transformer\_gradio.py    # Main app code
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Ignore sensitive files
├── .env.example                     # Example API key placeholder
├── README.md                        # Project documentation
└── LICENSE                          # MIT License

```

---

## ⚙️ Setup & Installation

1️⃣ **Clone the Repository**:

```bash
git clone https://github.com/rrstoll/langchain_rewrite_gradio.git
cd langchain_rewrite_gradio
````

2️⃣ **Install Dependencies**:

```bash
pip install -r requirements.txt
```

3️⃣ **Configure API Key**:

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Then edit `.env` and replace with your actual OpenAI API key:

```bash
OPENAI_API_KEY=sk-your-openai-key-here
```

Or, if deploying to **Hugging Face Spaces**, set your API key in the Space settings as a secret (`OPENAI_API_KEY`).

---

## 🖥️ Run the App

Launch the Gradio app locally:

```bash
python langchain_rewrite_gradio.py
```

Open the link in your browser (e.g., `http://127.0.0.1:7860`).

---

## 🌐 Deploy to Hugging Face Spaces

1️⃣ Create a new **Space** on [Hugging Face](https://huggingface.co/spaces)
2️⃣ Select **Gradio** as the SDK
3️⃣ Push your code:

```bash
git remote add origin https://huggingface.co/spaces/your-username/langchain_rewrite_gradio
git push -u origin main
```

4️⃣ In your Space settings, add a **Secret** for `OPENAI_API_KEY`.

---

## 🔍 Example Usage

**Input**:

```
Let's have a meeting to discuss the project.
```

**Style**:

```
Poetic
```

**Output**:

```
Gather 'round, let us share our dreams of what we'll build together.
```

---

## 💡 Built With

* [LangChain 1.0](https://python.langchain.com)
* [OpenAI GPT Models](https://platform.openai.com)
* [Gradio](https://gradio.app)
* [Python dotenv](https://pypi.org/project/python-dotenv/)

---

## 📬 Contact

Built by [Russ Stoll](https://www.russinmotion.com/)
Let’s connect on [LinkedIn](https://www.linkedin.com/in/russellstoll/)!

---

## 📄 License

MIT License

```
