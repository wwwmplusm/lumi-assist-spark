"""Tests for the Telegram bot module."""

import asyncio
import os
from types import SimpleNamespace

import pytest

os.environ.setdefault("TELEGRAM_TOKEN", "123456:ABC")
os.environ.setdefault("OPENAI_API_KEY", "dummy")
from app import telegram_bot


def test_generate_answer(monkeypatch: pytest.MonkeyPatch) -> None:
    """generate_answer should return model output."""

    async def fake_create(*args, **kwargs):
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content="test"))]
        )

    monkeypatch.setattr(
        telegram_bot.openai_client.chat.completions, "create", fake_create
    )

    result = asyncio.run(telegram_bot.generate_answer("hi"))

    assert result == "test"
