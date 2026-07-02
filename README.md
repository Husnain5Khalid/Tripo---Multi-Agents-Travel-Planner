# Tripo---Multi-Agents-Travel-Planner

## How to run

1. Create the Virtual Environment

conda create -n travel python=3.11 -y

2. Activate the Environment

conda activate travel

3. Install the Requirement

pip install -r requirements.txt

# 🌍 Multi-Agent AI Travel Planner

An intelligent travel planning application powered by **Multiple Agentic AI systems** that collaborate to create personalized, efficient, and comprehensive travel itineraries.

## 🚀 Overview

The Multi-Agent AI Travel Planner leverages multiple AI agents, each responsible for a specific aspect of travel planning. Instead of relying on a single AI model, specialized agents work together to deliver accurate, personalized, and optimized travel recommendations.

Whether you're planning a weekend getaway or an international vacation, the system helps generate a complete travel plan based on your preferences, budget, destination, and travel dates.

---

## ✨ Features

- 🤖 Multi-Agent AI Architecture
- 📍 Destination Recommendations
- 🗺️ Day-wise Itinerary Generation
- 💰 Budget Planning
- 🏨 Hotel Suggestions
- 🍽️ Restaurant Recommendations
- ✈️ Transportation Planning
- 🌤️ Weather Information
- 🎯 Personalized Travel Recommendations
- ⚡ Fast and Automated Planning

---

## 🏗️ Multi-Agent Workflow

The system consists of multiple AI agents that work together:

### 1. User Preference Agent
- Collects travel requirements
- Understands budget
- Identifies interests
- Determines travel duration

### 2. Destination Research Agent
- Finds suitable destinations
- Researches attractions
- Identifies local highlights

### 3. Itinerary Planning Agent
- Creates day-by-day travel plans
- Optimizes travel schedule
- Balances activities

### 4. Budget Agent
- Estimates total trip cost
- Suggests budget-friendly alternatives
- Tracks expenses

### 5. Accommodation Agent
- Recommends hotels
- Suggests stays based on budget
- Provides accommodation options

### 6. Transportation Agent
- Suggests flights
- Plans local transportation
- Optimizes travel routes

### 7. Food & Activities Agent
- Recommends restaurants
- Suggests local cuisines
- Finds entertainment options

### 8. Final Report Agent
- Combines outputs from all agents
- Generates a complete travel plan
- Presents the final itinerary

---

## 🛠️ Tech Stack

- Python
- Agentic AI
- Large Language Models (LLMs)
- LangChain / LangGraph *(if used)*
- OpenAI API / Gemini API *(depending on your implementation)*
- Streamlit / Flask / FastAPI *(if applicable)*

---

## 📂 Project Structure

```
travel-planner/
│
├── agents/
│   ├── preference_agent.py
│   ├── destination_agent.py
│   ├── itinerary_agent.py
│   ├── budget_agent.py
│   ├── hotel_agent.py
│   ├── transport_agent.py
│   └── report_agent.py
│
├── utils/
├── prompts/
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/multi-agent-travel-planner.git
```

```bash
cd multi-agent-travel-planner
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
OPENAI_API_KEY=your_api_key

# OR

GOOGLE_API_KEY=your_google_api_key
```

---

## ▶️ Run the Project

```bash
python app.py
```

or

```bash
streamlit run app.py
```

depending on your application.

---

## 📌 Example Input

```
Destination: Japan
Duration: 7 Days
Budget: $2500
Interests:
- Nature
- Food
- Historical Places
```

---

## 📖 Example Output

- Recommended destinations
- Day-wise itinerary
- Hotel recommendations
- Transportation details
- Estimated budget
- Local restaurants
- Tourist attractions
- Weather information
- Travel tips

---

## 🔄 Agent Collaboration Flow

```
User Input
     │
     ▼
Preference Agent
     │
     ▼
Destination Agent
     │
     ▼
Itinerary Agent
     │
     ▼
Budget Agent
     │
     ▼
Hotel Agent
     │
     ▼
Transport Agent
     │
     ▼
Food & Activity Agent
     │
     ▼
Final Report Agent
     │
     ▼
Complete Travel Plan
```

---

## 🎯 Future Improvements

- Flight price comparison
- Real-time weather integration
- Google Maps integration
- Live hotel booking
- Visa requirement checker
- Currency conversion
- PDF itinerary export
- Multi-language support
- Voice-based travel assistant

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Husnain Khalid**

If you found this project helpful, consider giving it a ⭐ on GitHub.


