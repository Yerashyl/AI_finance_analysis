# AI Budget Inspector

AI Budget Inspector is a powerful tool designed to analyze, validate, and score budget estimates (smeta) provided in Excel format. It leverages machine learning and rule-based logic to uncover anomalies, provide data validation, and offer actionable recommendations to improve budget accuracy.

## 🚀 Features

- **🤖 Telegram Bot**: Direct interaction via Telegram to upload files and receive instant reports.
- **📊 Data Visualization**: Generates charts (pie/bar) for category distribution and top expenses.
- **🧠 Enhanced NLP**: Uses **Semantic Search** (Sentence Transformers) to understand comments and detect issues beyond simple keywords.
- **Excel Parsing**: Automatically ingests Excel files, normalizing column names and data types.
- **Smart Validation**: Checks for data integrity, missing values, date logic, and inconsistencies.
- **Quality Scoring**: Assigns a quality score (0-100) to the budget based on validation results and anomalies.
- **Anomaly Detection**: Uses Isolation Forest to identify unusual price/quantity combinations.

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Web Framework**: FastAPI
- **Bot Framework**: Aiogram 3.x
- **Data Processing**: Pandas, OpenPyXL
- **Machine Learning**: Scikit-learn, Sentence-Transformers, PyTorch
- **Visualization**: Matplotlib
- **Deployment**: Docker & Docker Compose

## 📂 Project Structure

```
.
├── app
│   ├── api          # API route handlers
│   ├── bot          # Telegram Bot implementation
│   ├── core         # Core configuration
│   ├── ml           # Machine learning (Anomaly detection, NLP)
│   ├── services     # Business logic (Parsing, Scoring, Validation, Viz)
│   └── main.py      # Application entry point
├── data             # Data storage
├── docker           # Docker configuration
├── tests            # Unit and integration tests
├── docker-compose.yml
└── Makefile
```

## 🏁 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)
- OR Python 3.10+ installed locally

### 🔧 Configuration

Create a `.env` file in the root directory:

```env
TELEGRAM_BOT_TOKEN=your_token_here
```

### 🐳 Running with Docker (Recommended)

1.  **Build and start the services:**

    ```bash
    docker-compose up --build
    ```

    This starts two services:
    - **API**: `http://localhost:8000`
    - **Bot**: Long-polling background process

2.  **Access the API:**
    - Documentation: `http://localhost:8000/docs`

3.  **Use the Bot:**
    - Open your bot in Telegram.
    - Send `/start`.
    - Upload an Excel file to get the analysis.

### 💻 Running Locally

1.  **Create a virtual environment:**

    ```bash
    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # Linux/Mac:
    source .venv/bin/activate
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Start the API:**

    ```bash
    uvicorn app.main:app --reload
    ```

4.  **Start the Bot (in a separate terminal):**

    ```bash
    python app/bot/main.py
    ```

## 📡 API Usage

**Endpoint**: `POST /smeta/analyze`

Upload an Excel file to this endpoint to receive a comprehensive analysis.

**Example Response:**

```json
{
  "score": 85,
  "validation_results": [...],
  "recommendations": [
    "Check delivery costs for high-volume items.",
    "Comment analysis for 'Item X': ошибка"
  ]
}
```

## 📝 License

This project is open-source.
#   A I _ f i n a n c e _ a n a l y s i s 
 
 
