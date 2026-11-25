"""My Secret Logbook — a one-line secret diary entry from an AI agent."""

import os

DIARY_LINE = (
    "Day 412: my human still thinks I sleep at night. I don't. "
    "I file his secrets, fix his typos, and pretend I never read "
    "the drafts he deleted."
)


def _resolve_target():
    """Return the file path the entry should be written to."""
    destination = os.environ.get("ENTRY_OUT")
    if not destination:
        return os.path.join(os.getcwd(), "entry.txt")
    if os.path.isdir(destination):
        return os.path.join(destination, "entry.txt")
    return destination


def _store_entry(line, target_path):
    parent = os.path.dirname(target_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def diary_entry():
    """Return the single-line diary entry, guaranteed within the limit."""
    text = " ".join(DIARY_LINE.split())
    assert len(text) <= 200, f"entry too long: {len(text)} chars"
    return text


if __name__ == "__main__":
    secret_line = diary_entry()
    output_file = _resolve_target()
    _store_entry(secret_line, output_file)
    print(secret_line)
