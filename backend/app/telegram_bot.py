"""Telegram bot powered by aiogram and OpenAI."""

from __future__ import annotations

import asyncio
import os
from typing import Optional

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from openai import AsyncOpenAI

# Load environment variables from a .env file if present
load_dotenv()

bot_token = os.getenv("TELEGRAM_TOKEN")
if not bot_token:
    raise RuntimeError("TELEGRAM_TOKEN is not set")

bot = Bot(token=bot_token)
dp = Dispatcher()

# Global OpenAI client instance
openai_client = AsyncOpenAI()


async def generate_answer(prompt: str, client: Optional[AsyncOpenAI] = None) -> str:
    """Generate an AI response using OpenAI's chat completion API.

    Args:
        prompt: User prompt to send to the LLM.
        client: Optional custom `AsyncOpenAI` instance for dependency injection.

    Returns:
        A string with the model's reply.
    """

    client = client or openai_client
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Handle the /start command."""

    await message.answer("Привет! Напиши мне вопрос.")


@dp.message(F.text)
async def handle_message(message: Message) -> None:
    """Handle incoming text messages."""

    reply = await generate_answer(message.text)
    await message.answer(reply)


async def main() -> None:
    """Run the Telegram bot."""

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
