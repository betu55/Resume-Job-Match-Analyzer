import re

def clean_text(text):
    """
    Convert text into a lowercase, simplified format for matching.
    Keeps useful tech characters like +, #, and . for skills like C++, C#, and Node.js.
    """
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9+#. ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
