from langdetect import detect

def detect_language(text):
    """
    Detect the language of a given text.
    
    Args:
        text (str): The text to detect language for.
    
    Returns:
        str: The detected language code (e.g., 'en', 'es', 'fr', 'nl').
    """
    try:
        return detect(text)
    except Exception as e:
        return "unknown"
