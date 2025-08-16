import time
import uuid


def generate_blocks_from_text_stub(source_text: str, prompt: str | None) -> list:
    """Simulates a call to an AI model."""
    time.sleep(2)
    return [
        {
            "id": str(uuid.uuid4()),
            "type": "mcq",
            "prompt": "Based on the text, what is the capital of France?",
            "options": ["Berlin", "Paris", "London", "Madrid"],
            "answer": "Paris",
        },
        {
            "id": str(uuid.uuid4()),
            "type": "open_answer",
            "prompt": "In your own words, explain the main topic of the text.",
            "keywords": ["summary", "main idea"],
        },
    ]
