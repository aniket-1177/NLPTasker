import re

def extract_deadline(sentence: str) -> str:
    """Extracts deadline from text."""
    deadline_patterns = [
        r'by\s+([\w\s]+)', r'until\s+([\w\s]+)', r'on\s+([\w\s]+)', r'before\s+([\w\s]+)'
    ]
    
    for pattern in deadline_patterns:
        match = re.search(pattern, sentence, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    time_keywords = ['today', 'tomorrow', 'next week', 'this week', 'monday', 'friday']
    for keyword in time_keywords:
        if keyword in sentence.lower():
            return keyword

    return None
