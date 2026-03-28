# OpenEnv GridWorld Agent 🚀

## 🧠 Overview
This project implements a custom OpenEnv environment for Reinforcement Learning using:
- step()
- reset()
- state()

The environment is a GridWorld where an agent learns to reach a goal while avoiding obstacles.

---

## 🎯 Features
- Custom environment class (OpenEnv)
- Q-learning based training
- Fully offline (no APIs used)
- Simple and clean structure

---

## 🧩 Environment Details
- Agent = 1 🤖
- Goal = 2 🎯
- Obstacles = -1 🚧
- Empty space = 0 ⬜

---

## ▶️ How to Run

Install dependencies:
pip install -r requirements.txt

Train the agent:
python train.py

Run demo:
python demo.py

---

## 📁 Project Structure

env.py → Environment (step, reset, state)  
train.py → Training using Q-learning  
demo.py → Demo run  
requirements.txt → Dependencies  
README.md → Documentation  

---

## 📌 Notes
- Works completely offline  
- No external APIs  
- Built as a real-world OpenEnv simulation project
