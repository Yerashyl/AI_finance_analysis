# Project Roadmap

## 1. Backend / API
- [ ] **Add extended validation rules**
  - Check logical consistency (e.g., `order_date < delivery_date`).
  - Validate numeric ranges and completeness.
- [ ] **Expand Scoring with ML**
  - Train model on historical estimates (smeta).
  - Use ML feedback for the scoring metric.
- [ ] **Transformer Integration**
  - Connect transformers for deeper comment analysis.
  - Generate intelligent recommendations.
- [ ] **Data Visualization**
  - Generate graphs/charts for budget distribution.
  - Highlight anomalies visually.

## 2. ML / NLP
- [ ] **ML Pipeline Preparation**
  - `parser` → `features` → `anomaly` → `NLP` → `score` → `recommendations`.
- [ ] **Unit Tests for ML**
  - Ensure stability of ML components.
- [ ] **Metrics & Evaluation**
  - Track Precision/Recall for anomalies.
  - Track Accuracy for comment classification.
- [ ] **Performance Optimization**
  - Profile code for large files.

## 3. Telegram Bot
- [ ] **Implementation**
  - Full integration with FastAPI.
  - Support `start`, `help`, `status` commands.
- [ ] **File Handling**
  - Support Excel file structure.
  - Format output recommendations nicely for chat.

## 4. Docker / CI/CD
- [ ] **Testing & Quality**
  - Add unit tests in `tests/`.
  - Configure GitHub Actions for CI (test, lint, ML eval).
- [ ] **Containerization**
  - Verify `Dockerfile` and `docker-compose` are production-ready.

## 5. Additional ("Wow" Features)
- [ ] **Receipt OCR**
  - Upload photo of receipts -> Extract data.
- [ ] **Mini-Frontend**
  - React/Vue app for visualizing results.
- [ ] **Extensibility**
  - Plugin system for new Excel formats/models.
- [ ] **Documentation**
  - User and Developer guides.
