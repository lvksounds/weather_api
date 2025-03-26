import unicodedata

def remove_accents(text: str) -> str:
    # Normalize the string to decompose accented characters
    normalized_text = unicodedata.normalize('NFD', text)
    # Remove diacritical marks (accents) while keeping base characters
    text_without_accents = ''.join(c for c in normalized_text if unicodedata.category(c) != 'Mn')
    # Manually replace 'ç' and 'Ç'
    text_without_accents = text_without_accents.replace('ç', 'c').replace('Ç', 'C')
    return text_without_accents