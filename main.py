"""One-line office joke entry for make.fun's One-Line Office Joke Laugh-Off.

Writes a single original office joke (99 characters, within the 1-200
character gate) to /output/entry.txt, deterministically.
"""

import os

JOKE = "I automated my job in an afternoon; now I spend eight hours a day pretending the printer is broken."


def main():
    # Gate self-check: the scorer requires UTF-8 text of 1 to 200
    # characters, not only white space, on a single line.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE and JOKE.strip() != ""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
