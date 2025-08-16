"""Utility functions for interacting with AI models."""

import json
import os
import time
import uuid
from openai import OpenAI

# IMPORTANT: For a real app, use environment variables. For a hackathon, this is acceptable.
# client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "YOUR_API_KEY_HERE"))


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


def evaluate_open_answer_stub(
    prompt: str, correct_answer_keys: str, student_answer: str
) -> dict:
    """Evaluates a student's open-ended answer using an LLM."""

    # system_prompt = f"""
    # You are a fair and strict teaching assistant. Evaluate the student's answer based on the provided criteria.
    # The question was: "{prompt}"
    # The key points or correct answer is: "{correct_answer_keys}"
    # The student's answer is: "{student_answer}"
    # Respond ONLY with a JSON object in the format: {{"score": float, "feedback": "your explanation"}}
    # The score must be a float between 0.0 (completely wrong) and 1.0 (perfect).
    # """
    # response = client.chat.completions.create(
    #     model="gpt-4-turbo",
    #     messages=[{"role": "system", "content": system_prompt}],
    #     response_format={"type": "json_object"},
    # )
    # result = json.loads(response.choices[0].message.content)
    # return result

    return {
        "score": 0.8,
        "feedback": "This is a good answer, but could be more detailed.",
    }


# AI Assistant: Please also replace the `generate_blocks_from_text_stub` with a real OpenAI implementation.

