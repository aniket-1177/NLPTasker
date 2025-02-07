# NLP Task Extraction Project

## Overview
**NLPTasker** is an **NLP-based heuristic pipeline** designed to extract and categorize tasks from **unstructured text**. It identifies actionable items, extracts relevant entities, and determines deadlines when available.

## Objective
Given a paragraph of text, the program identifies tasks and extracts:
- **What action needs to be performed** (task extraction)
- **Who needs to perform it** (entity extraction)
- **When it should be completed** (deadline extraction, if available)

### Example
#### Input Text:
```
Rahul wakes up early every day. He goes to college in the morning and comes back at 3 pm. At present, Rahul is outside. He has to buy the snacks for all of us.
```
#### Output:
```csv
Task, Entity, Deadline, Category
"Rahul has to buy the snacks for all of us", Rahul, None, "Personal"
```

---

## Features
✅ **Heuristic-Based Extraction** - No pre-annotated datasets required.

✅ **Task Identification** - Uses **POS tagging, named entity recognition (NER), and sentence structure analysis**.

✅ **Entity Extraction** - Identifies responsible persons using NLP models.

✅ **Deadline Detection** - Extracts time-sensitive information.

✅ **Task Categorization** - Uses **LDA topic modeling** to dynamically group tasks.

✅ **Logging & Error Handling** - Robust logging for debugging.

---

## How It Works
### 1. **Preprocessing**
- Cleans the text (removes stopwords, punctuation, metadata)
- Tokenizes sentences and applies POS tagging

### 2. **Task Identification**
- Detects imperative verbs (e.g., *"buy," "submit," "review"*)
- Extracts phrases with actionable intent (*"has to," "should," "must"\*)

### 3. **Entity & Deadline Extraction**
- Uses **NER** to find responsible individuals
- Identifies deadline-related phrases (*"by 5 pm," "tomorrow," "before Monday"*)

### 4. **Task Categorization**
- Uses **TF-IDF and LDA** to cluster tasks into meaningful categories such as:
  - **Personal** (e.g., Buy groceries)
  - **Professional** (e.g., Submit report by Monday)
  - **Administrative** (e.g., Schedule meeting with HR)
  - **Team Collaboration** (e.g., Discuss project with team)

### 5. **Output Format**
Extracted tasks are stored in a **CSV file** (`output/output.csv`) with the following fields:
- **Task**: Extracted task sentence
- **Entity**: The person responsible
- **Deadline**: Timeframe (if applicable)
- **Category**: Assigned topic category
- **Processed Task**: Preprocessed task representation

---

## Installation
### **1. Clone Repository**
```bash
git clone https://github.com/your-username/NLPTasker.git
cd NLPTasker
```
### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```
### **3. Download NLP Models**
```bash
python -m spacy download en_core_web_sm
nltk.download('punkt')
nltk.download('stopwords')
```

---

## Usage
### **1. Add Input Text**
Create a text file `data/input.txt` and add unstructured text containing potential tasks.

### **2. Run the Task Extractor**
```bash
python main.py
```

### **3. View Results**
Extracted tasks will be saved in `output/output.csv`.

---


## Example Output (CSV Format)
| Task | Entity | Deadline | Category |
|------|--------|----------|------------|
| "Rahul has to buy the snacks for all of us" | Rahul | None | Personal |
| "John must submit the report by Monday" | John | Monday | Professional |

---

## Future Improvements
🔹 **Fine-tune heuristics for better accuracy**  
🔹 **Enhance entity recognition with Named Entity Linking (NEL)**  
🔹 **Support for multi-task detection in a single sentence**  

---

