# 🏠 Jordan — Persistent Home Chatbot

A smart, memory-enabled chatbot built with **Python** and **ChatterBot**.  
Jordan recognizes users, remembers previous training, and can learn new dialogues incrementally.

---

## ⚡ Key Features
- **Persistent storage** — training data saved in SQLite  
- **One-time training** — no retraining on every start  
- **Incremental learning** — new dialogues can be added without losing old ones  
- **Identity recognition** — personalized responses for Mark and Jane

---

## 🧠 Example Interaction
<details>
  <summary>Example Interaction</summary>
  
  **You:** State your identity please: Mark  
  **Jordan:** Welcome, Mark. Happy to have you at home.  
  **Jordan:** Hello! I'm Jordan! How can I help you today?  
  **You:** Who is the owner of this house?  
  **Jordan:** Mark is the owner of this house.  
  **You:** What is my favourite sport?  
  **Jordan:** You have always loved baseball.  
  **You:** bye  
  **Jordan:** Goodbye! Have a great day!
</details>

---

## ⚙️ Installation
```bash
git clone https://github.com/vkrylova/ChatBot.git
cd ChatBot
pip install -r requirements.txt
python main.py
```

---

## 💡 Notes
- The bot automatically creates database.sqlite3 on first run
- Subsequent runs use existing database, preserving training
- Delete database.sqlite3 to reset training

---

## 🛠️ Tech Stack
- Python 3.x
- ChatterBot
- SQLite
