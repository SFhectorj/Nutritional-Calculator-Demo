# Nutritional-Calculator-Demo

A Python and Flask-based web application that uses the OpenAI API to analyze images of food. The app identifies the food, calculates its nutritional value (calories, protein, carbs, and fat), and suggests 3 relevant recipes.

## Tech Stack

*   **Backend:** Python, Flask
*   **Frontend:** HTML, CSS, JavaScript (Vanilla)
*   **AI / API:** OpenAI API (`gpt-4.1` model)
*   **Environment Management:** `python-dotenv`

## Functionality

1.  **Image Upload:** The user selects an image of food via the web interface.
2.  **Preview:** A preview of the selected image is displayed to the user.
3.  **Analysis:** Upon clicking "Analyze Food", the image is converted to a Base64 string and sent to the Flask backend.
4.  **AI Processing:** The backend constructs a prompt instructing the OpenAI `gpt-4.1` model to identify the food and return a structured JSON response containing the food's name, nutritional info, and 3 recipes.
5.  **Display Results:** The frontend parses the JSON response and displays the nutritional information in a styled list, along with the recipe suggestions.

## Directory Structure

```
Nutritional-Calculator-Demo/
├── README.md               # Project documentation
├── nutrition_calc.py       # Main Flask application and API integration
├── test_api.py             # Script to verify OpenAI API connectivity
├── .env                    # Environment variables (contains OPENAI_API_KEY)
└── templates/
    └── index.html          # Frontend web interface
```

## How to Run

1.  Ensure you have the required dependencies installed (`flask`, `openai`, `python-dotenv`).
2.  Create a `.env` file in the root directory and add your OpenAI API key: `OPENAI_API_KEY=your_key_here`
3.  Run the Flask app: `python nutrition_calc.py`
4.  Open your web browser and navigate to `http://127.0.0.1:5000`.
