import re
import spacy
from utils.detect_language import detect_language


# Load the spaCy model for English (can be extended for other languages)
nlp = spacy.load("en_core_web_sm")

IGNORE_TERMS = {
    "es": ["teléfono", "departamento", "escuela", "universidad", "licenciatura"],
    "fr": ["téléphone", "lycée", "université", "école"],
    "en": ["phone", "school", "university", "institute"],
    "nl": ["telefoon", "gymnasium", "universiteit", "opleiding"],
}

def extract_name(text, language="en"):
    """
    Extracts a valid name from the resume text.
    """
    ignore_keywords = IGNORE_TERMS.get(language, [])
    logging_steps = []  # Log all steps to debug

    # 1. Detect "Name: <Name>" patterns
    name_pattern = r"(?:Name|Nom)[:\s]*([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)"
    match = re.search(name_pattern, text)
    if match:
        logging_steps.append(f"Matched Name Pattern: {match.group(1)}")
        return match.group(1)

    # 2. Extract PERSON entities with SpaCy
    doc = nlp(text)
    for ent in doc.ents:
        if (
            ent.label_ == "PERSON"
            and not any(keyword in ent.text.lower() for keyword in ignore_keywords)
            and not re.search(r"\d|\||/", ent.text)  # Exclude numbers or symbols
        ):
            logging_steps.append(f"Found PERSON entity: {ent.text}")
            return ent.text

    # 3. Fallback: Check first few lines for name-like structure
    for line in text.splitlines()[:5]:
        words = line.split()
        if (
            len(words) >= 2
            and all(word[0].isupper() and word[1:].islower() for word in words[:2])  # Capitalization check
            and not any(char.isdigit() for char in line)  # Exclude lines with numbers
            and not any(keyword in line.lower() for keyword in ignore_keywords)  # Exclude irrelevant terms
        ):
            name_candidate = " ".join(words[:2])
            logging_steps.append(f"Fallback to first lines: {name_candidate}")
            return name_candidate

    logging_steps.append("No valid name found.")
    print("\n".join(logging_steps))  # Debugging info
    return "Name not found"

def extract_age(text):
    """
    Extract the age from the text by looking for patterns like 'Age: 25' or '25 years old'.
    """
    age_pattern = r"\b(?:Age[:\s]*|)(\d{2})\b(?:\s*years\s*old)?"
    match = re.search(age_pattern, text, re.IGNORECASE)
    return match.group(1) if match else "Not Found"

import re

import re

def extract_education(text, language):
    """
    Extract education qualifications specifically from the 'Education' section of the text.
    """
    # Define language-specific section headers for 'Education'
    section_headers = {
        "en": ["Education", "Academic Background", "Qualifications"],
        "fr": ["Formation", "Éducation", "Diplômes"],
        "es": ["Educación", "Formación Académica", "Calificaciones"],
        "nl": ["Opleiding", "Academische Achtergrond", "Diploma's"]
    }

    # Define language-specific keywords for degrees
    education_terms = {
        "en": ["Bachelor", "Master", "PhD", "Degree", "Diploma", "University", "College", "GPA"],
        "fr": ["Baccalauréat", "Licence", "Master", "Doctorat", "Université", "École", "Diplôme"],
        "es": ["Licenciatura", "Máster", "Doctorado", "Universidad", "Escuela", "Diploma"],
        "nl": ["Bachelor", "Master", "Doctoraat", "Universiteit", "School", "Diploma"]
    }

    # Get the relevant section headers and terms for the detected language
    headers = section_headers.get(language, [])
    terms = education_terms.get(language, [])
    if not headers or not terms:
        return f"Education terms or headers not defined for {language}"

    # Extract the 'Education' section only
    section_pattern = rf"({'|'.join(re.escape(header) for header in headers)})(.*?)(?:\n\n|\Z)"
    education_section = ""
    for match in re.finditer(section_pattern, text, flags=re.DOTALL | re.IGNORECASE):
        education_section += match.group(2)

    if not education_section.strip():
        return "Education section not found"

    # Build regex dynamically from terms
    term_pattern = "|".join(re.escape(term) for term in terms)
    degree_pattern = rf"({term_pattern})(?:\s+[\w\s,]+)?"

    # Extract matches from the education section
    matches = re.findall(degree_pattern, education_section, flags=re.IGNORECASE)

    # Filter out irrelevant matches by validating against education-specific keywords
    filtered_lines = []
    for line in education_section.splitlines():
        if any(term.lower() in line.lower() for term in terms) and "intern" not in line.lower():
            filtered_lines.append(line.strip())

    # Combine results and return
    final_education = set(matches + filtered_lines)
    return ", ".join(sorted(final_education)) if final_education else "Education not found"



def extract_data(text):
    """
    Extract name, age, and education from the given text.
    """
    language = detect_language(text)  # Detect the language of the resume
    name = extract_name(text)  # Extract name
    age = extract_age(text)
    education = extract_education(text, language)  
    return {"name": name, "age": age, "education": education}
