# 📚 AI Study Planner

> A personalized, AI-powered study companion that helps you plan smarter, learn faster, and stay motivated — with an interactive chatbot and auto-generated quizzes.

---

## 🌟 Overview

**AI Study Planner** is a Streamlit-based web application that transforms the way you study. Powered by Google Gemini AI, it creates personalized study plans tailored to your goals, generates quizzes to test your knowledge, and features an intelligent chatbot to answer your questions — making studying more engaging, effective, and fun.

---

## ✨ Features

- 🗓️ **Personalized Study Planner** — Generate a custom day-by-day study schedule based on your subject, available time, and exam date
- 🤖 **AI Chatbot** — Ask any study-related question and get instant, intelligent answers powered by Google Gemini
- 📝 **Auto Quiz Generator** — Create quizzes on any topic to test your understanding and reinforce learning
- 🎯 **Goal-based Planning** — Set your targets and let AI break them down into manageable daily tasks
- 💡 **Interactive UI** — Clean, intuitive interface built with Streamlit for a seamless experience

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web UI framework |
| Google Gemini AI (`google-generativeai`) | AI chatbot & content generation |
| python-dotenv | Secure API key management |
| matplotlib | Data visualization |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- A Google Gemini API key → [Get it here](https://makersuite.google.com/app/apikey)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-study-planner.git
   cd ai-study-planner
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your API key**
   ```bash
   # Copy the example env file
   cp .env.example .env
   ```
   Open `.env` and replace with your actual key:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

6. **Run the app**
   ```bash
   streamlit run app.py
   ```

7. Open your browser at **http://localhost:8501** 🎉

---

## 📁 Project Structure

```
ai-study-planner/
│
├── app.py               # Main Streamlit app entry point
├── chatbot.py           # AI chatbot logic
├── requirements.txt     # Python dependencies
├── .env.example         # API key template (safe to share)
├── .env                 # Your actual API keys (NOT pushed to GitHub)
├── .gitignore           # Files excluded from Git
└── README.md            # Project documentation
```

---

## 🔐 Security

- API keys are stored in a `.env` file and **never hardcoded** in source code
- `.env` is listed in `.gitignore` and will **never be pushed** to GitHub
- Use `.env.example` as a template when setting up on a new machine

---

## 📸 Screenshots

> _Add screenshots of your app here after deploying_

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Fork the repo
- Create a new branch (`git checkout -b feature/your-feature`)
- Commit your changes (`git commit -m 'Add some feature'`)
- Push to the branch (`git push origin feature/your-feature`)
- Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Made with ❤️ by **[Prasad Shinde]**  
📧 prasadshinde0428@email.com  
🔗 [GitHub Profile]((https://github.com/Prasad2809))

---

> ⭐ If you found this project helpful, please consider giving it a star on GitHub!
