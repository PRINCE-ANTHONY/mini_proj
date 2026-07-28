# 🎙️ LEMORA AI - Voice Assistant

LEMORA AI is a voice-powered AI assistant built using **Python**, **Streamlit**, and **Groq AI**. It allows users to ask questions through voice input, converts speech into text using Groq's Whisper model, generates intelligent responses using Llama 3.3, and converts the response back into natural speech using Google Text-to-Speech. The application loads the Groq API key from environment variables before initializing the client. :contentReference[oaicite:0]{index=0}

---

## 🌐 Live Demo

🔗 **https://lemora.streamlit.app/**

---

## 📸 Preview

![Dark themed Streamlit interface for Lemora AI voice assistant showing a microphone icon, heading text Lemora AI voice assistant, explanatory text You can ask it anything you want and it will answer it, and a browser audio recorder control for recording a question](image.png)

---

## ✨ Features

- 🎤 Voice input directly from your browser
- 📝 Speech-to-text transcription
- 🤖 AI-powered responses
- 🔊 Text-to-speech output
- ⚡ Fast inference using Groq
- 🌐 Simple and responsive Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API
- Whisper Large V3 Turbo
- Llama 3.3 70B Versatile
- Google Text-to-Speech (gTTS)
- Python Dotenv

---

## How It Works

1. Record your voice.
2. Your audio is transcribed using **Whisper Large V3 Turbo**.
3. The transcribed text is sent to **Llama 3.3 70B Versatile**.
4. The AI generates a response.
5. The response is converted into speech.
6. The audio is played back to the user. :contentReference[oaicite:1]{index=1}

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/lemora-ai.git
```

Move into the project directory

```bash
cd lemora-ai
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_api_key
```

Run the application

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
LEMORA-AI/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 📋 Requirements

```
streamlit
groq
python-dotenv
gTTS
```

The project depends on these core packages. :contentReference[oaicite:2]{index=2}

---

## 🎯 Future Improvements

- 💬 Chat history
- 🌍 Multiple language support
- 🎨 Improved UI/UX
- 📄 Export conversation
- 🎙️ Voice selection
- 🌙 Dark mode customization
- 📱 Better mobile experience

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to fork the repository and submit a pull request.

---

## 👨‍💻 Author

**D PRINCE ANTHONY**

GitHub: https://github.com/PRINCE-ANTHONY

LinkedIn: https://www.linkedin.com/in/prince-anthony006/

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

It motivates me to build more AI projects.

---

## 📄 License

This project is licensed under the MIT License.