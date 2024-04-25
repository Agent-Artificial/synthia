
import os
import uvicorn
from typing_extensions import Any, Tuple
from anthropic import Anthropic
from anthropic._types import NotGiven
from communex.module.module import Module
from communex.key import generate_keypair
from communex.module.server import ModuleServer 
from loguru import logger
from .anthropic_miner import BaseLLM, EndpointDefinition
from dotenv import load_dotenv

from miner._config import AnthropicSettings


load_dotenv()

anthropic_endpoint = EndpointDefinition(
    name="anthropic",
    params_model=AnthropicSettings
)


class AnthropicModule(BaseLLM):
    """Anthropic Module Class"""
    def __init__(self, settings: AnthropicSettings | None = None) -> None:
        """
        Initializes an instance of the AnthropicModule class.

        Args:
            settings (AnthropicSettings | None, optional): The settings for the Anthropic API. Defaults to None.

        Returns:
            None: This function does not return anything.

        Initializes the following instance variables:
            - endpoints (dict): A dictionary containing the endpoint for the Anthropic API.
            - settings (AnthropicSettings): The settings for the Anthropic API.
            - client (Anthropic): An instance of the Anthropic client.
            - system_prompt (str): The system prompt for generating explanations.

        The system prompt is a string that describes the role of the Anthropic polymath and provides guidance on how to generate explanations. It includes a maximum token limit for the generated answer.

        The Anthropic client is initialized with the API key from the settings or the environment variable ANTHROPIC_API_KEY.

        If the settings parameter is None, the AnthropicSettings class is used to create the settings object.

        Note:
            - The Anthropic API key is retrieved from the settings object or the environment variable ANTHROPIC_API_KEY.
            - The maximum token limit for the generated answer is set using the settings.max_tokens attribute.
        """
        super().__init__(**anthropic_endpoint.model_dump())
        self.settings = settings or AnthropicSettings()  # type: ignore
        self.client = Anthropic(api_key=self.settings.api_key or os.getenv("ANTHROPIC_API_KEY")) 
        self.system_prompt = (
            "You are a supreme polymath renowned for your ability to explain "
            "complex concepts effectively to any audience from laypeople "
            "to fellow top experts. "
            "By principle, you always ensure factual accuracy. "
            "You are master at adapting your explanation strategy as needed "
            "based on the field and target audience, using a wide array of "
            "tools such as examples, analogies and metaphors whenever and "
            "only when appropriate. Your goal is their comprehension of the "
            "explanation, according to their background expertise. "
            "You always structure your explanations coherently and express "
            "yourself clear and concisely, crystallizing thoughts and "
            "key concepts. You only respond with the explanations themselves, "
            "eliminating redundant conversational additions. "
            f"Try to keep your answer below {self.settings.max_tokens} tokens"
        )

    def prompt(self, user_prompt: str, system_prompt: str | None | NotGiven = None) -> Tuple[str | None, str]:
        """
        Executes a prompt request to the Anthropic API.

        Args:
            user_prompt (str): The user's prompt.
            system_prompt (str | None | NotGiven, optional): The system's prompt. Defaults to None.

        Returns:
            tuple[str | None, str]: A tuple containing the response from the prompt and any error message.
        """
        if not system_prompt:
            system_prompt = self.system_prompt
        message = self.client.messages.create(
            model=self.settings.model,
            max_tokens=self.settings.max_tokens,
            temperature=self.settings.temperature,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt},
            ],
        )
        return self._treat_response(message)

    def _treat_response(self, message: Any):
        """
        Treats the response received from the Anthropic API.

        Args:
            message (Any): The response message received from the Anthropic API.

        Returns:
            Tuple[str, str]: A tuple containing the generated answer and an empty string.
                - If the response message has a non-null stop_sequence or stop_reason other than "end_turn",
                  returns None and a message indicating that the max tokens were not enough to generate an answer.
                - Otherwise, returns the generated answer as a string and an empty string.

        TODO:
            - Use a result ADT to handle the response message.
        """
        message_dict = message.dict()
        if (
            message_dict["stop_sequence"] is not None
            or message_dict["stop_reason"] != "end_turn"
        ):
            return None, "Max tokens were not enough to generate an answer"

        blocks = message_dict["content"]
        answer = "".join([block["text"] for block in blocks])
        return answer, ""

    @property
    def max_tokens(self) -> int:
        """
        Returns the maximum number of tokens allowed by the model.
        """
        return self.settings.max_tokens

    @property
    def model(self) -> str:
        """
        Returns the model property of the class.

        :return: A string representing the model property.
        :rtype: str
        """
        return self.settings.model


if __name__ == "__main__":
    key = generate_keypair()
    logger.info(f"Running module with key {key.ss58_address}")
    claude = AnthropicModule()
    server = ModuleServer(claude, key)
    app = server.get_fastapi_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)
