import re
import os

def fix_encoding(text):
    """Fix common encoding issues in text"""
    if text is None:
        return ""
    
    # Fix common UTF-8 encoding issues
    replacements = {
        'â€™': "'",    # Right single quotation mark
        'â€œ': '"',    # Left double quotation mark
        'â€': '"',     # Right double quotation mark
        'â€"': '–',    # En dash
        'â€"': '—',    # Em dash
        'â€¦': '...',  # Ellipsis
        'â€¢': '•',    # Bullet
        'â€°': '‰',    # Per mille sign
        'â€¹': '‹',    # Single left-pointing angle quotation
        'â€º': '›',    # Single right-pointing angle quotation
        'â€ž': '„',    # Double low-9 quotation mark
        'â€ ': '†',    # Dagger
        'â€¡': '‡',    # Double dagger
        'â€˜': ''',    # Left single quotation mark
        'â€™': ''',    # Right single quotation mark
        'â€š': '‚',    # Single low-9 quotation mark
        'â€¤': '․',    # One dot leader
        'â€¥': '‥',    # Two dot leader
        'â€¦': '…',    # Horizontal ellipsis
        'â€§': '‧',    # Hyphenation point
        'â€»': '※',    # Reference mark
        'Â': ' ',      # Non-breaking space
        'â': 'a',      # a with circumflex
        'ê': 'e',      # e with circumflex
        'î': 'i',      # i with circumflex
        'ô': 'o',      # o with circumflex
        'û': 'u',      # u with circumflex
    }
    
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    
    # Fix double encoding issues
    text = re.sub(r'â€™', "'", text)
    text = re.sub(r'â€œ', '"', text)
    text = re.sub(r'â€', '"', text)
    
    return text

def cleanup_temp_files():
    """Clean up temporary audio files from the temp directory"""
    
    try:
        # Get the path to the temp directory in the project
        temp_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "temp")
        
        if os.path.exists(temp_dir):
            for file in os.listdir(temp_dir):
                if file.endswith('.wav') and os.path.isfile(os.path.join(temp_dir, file)):
                    try:
                        os.remove(os.path.join(temp_dir, file))
                    except Exception as e:
                        print(f"Failed to remove file {file}: {e}")
    except Exception as e:
        print(f"Error cleaning up temp files: {e}")