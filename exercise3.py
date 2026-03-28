import requests, re, time, sys
from collections import Counter

URL = "https://pl.wikipedia.org/api/rest_v1/page/random/summary"
N = 100  
HEADERS = {
    "User-Agent": "wp-edu-wiki-stats/0.1 (contact: your-email@domain)",
    "Accept": "application/json",
}

WORD_RE = re.compile(r"[^\W\d_]+", re.UNICODE)


def selekcja(text: str):
    """
    Extracts words from text that:
    - consist of letters only
    - are converted to lowercase
    - have a length > 3 characters
    """
    raw_words = WORD_RE.findall(text)
    return [word.lower() for word in raw_words if len(word) > 3]


def ramka(text: str, width: int = 80) -> str:

    max_content_width = width - 2
    
    if len(text) > max_content_width:
        processed_text = text[:width - 3] + "…"
    else:
        processed_text = text
        
    centered = processed_text.center(max_content_width)
    return f"[{centered}]"


def main():
    cnt = Counter()
    word_count = 0
    fetched_count = 0

    print(ramka("Start"), end="", flush=True)

    while fetched_count < N:
        try:
            response = requests.get(URL, headers=HEADERS, timeout=10)
            data = response.json()
        except Exception:
            time.sleep(0.1)
            continue

        title = data.get("title") or ""
        status_line = "\r" + ramka(title, 80)
        print(status_line, end="", flush=True)

        extract = data.get("extract") or ""
        selected_words = selekcja(extract)
        
        cnt.update(selected_words)
        word_count += len(selected_words)
        fetched_count += 1
        
        time.sleep(0.05)

    print("\n" + "="*80)
    print(f"Fetched articles: {fetched_count}")
    print(f"Total words:      {word_count}")
    print(f"Unique words:     {len(cnt)}\n")

    print("Top 15 most frequent words:")
    for word, frequency in cnt.most_common(15):
        print(f"{word:15} : {frequency}")


if __name__ == "__main__":
    main()
