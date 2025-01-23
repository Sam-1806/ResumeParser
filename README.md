# ResumeParser
# Resume Processor System

This project processes resumes in multiple languages (English, French, Spanish, and Dutch) and extracts key details such as Name, Age, and Education. The system allows users to upload resumes in `.pdf` or `.txt` format, processes them, and exports the extracted data into a `.csv` file.

The frontend is built with Streamlit, ensuring a user-friendly interface. The backend is implemented in Python using SpaCy for Named Entity Recognition (NER) and other libraries for text processing.

---

## Features
1. **Language Support**: Extracts data from resumes in English, French, Spanish, and Dutch.
2. **Key Data Extraction**: Extracts:
   - **Name**
   - **Age**
   - **Education** (including degree and major, e.g., "Bachelor's in Computer Science").
3. **Multi-Format Support**: Accepts `.pdf` and `.docx` files.
4. **Export to CSV**: Consolidates extracted data into a `results.csv` file.

---

## Prerequisites
1. Python 3.8 or above
2. An active internet connection to install dependencies

---

## Setup and Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/Sam-1806/ResumeParser.git
cd resume-processor
```

# Resume Processor

## Step 2: Create a Virtual Environment
```bash
python -m venv ResumeProcessor
```
## Step 3: Activate the Virtual Environment

### Windows:
```bash
ResumeProcessor\Scripts\activate
```

### macOS/Linux:
```bash
source ResumeProcessor/bin/activate
```

## Step 4: Install Dependencies
Install all required packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Step 5: Download SpaCy Language Model
SpaCy requires a pre-trained language model to extract entities. Run:
```bash
python -m spacy download en_core_web_sm
```

---

## Usage

### Step 1: Start the Application
Run the Streamlit app:
```bash
streamlit run main.py
```

### Step 2: Upload Resumes
Open your browser and navigate to [http://localhost:8501/](http://localhost:8501/).
Drag and drop or select resumes in `.pdf` or `.docx` format.

### Step 3: View Extracted Data
The app will display extracted details such as Name, Age, and Education in a table.
You can download the results as a `.csv` file.

---

## Folder Structure
resume-processor/
├── main.py                # Main script to run the Streamlit app
├── requirements.txt       # Dependencies for the project
├── utils/
│   ├── detect_language.py # Utility to detect the language of the resume
│   └── extract_data.py    # Utility functions for data extraction
├── sample_resumes/        # Folder to store sample resume files
└── README.md              # This readme file

---

## Troubleshooting

### Issue: SpaCy Model Not Found
If you encounter an error like:
OSError: [E050] Can't find model 'en_core_web_sm'

Run the following command to download the model:
python -m spacy download en_core_web_sm

### Issue: Missing Libraries
Ensure all dependencies are installed by running:
pip install -r requirements.txt

---

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For further questions, please contact:

**Name:** Samruddhi Bhabad  
**Email:** [samruddhibhabad@gmail.com](mailto:samruddhibhabad@gmail.com)
