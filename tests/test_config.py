from lemonsqueezy.config import settings


def test_settings():
    assert settings.api_key is not None, "API Key is not set"
    assert isinstance(settings.api_key, str), "API Key is not a string"
