from pydantic import BaseModel


class AnthropicSettings(BaseModel):
    api_key: str
    model: str = "claude-3-opus-20240229"
    max_tokens: int = 1000
    temperature: float = 0.5

    class Config:
        env_prefix = "ANTHROPIC_"
        env_file = "env/config.env"
        extra = "ignore"
