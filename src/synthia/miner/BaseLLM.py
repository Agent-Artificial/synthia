import inspect
from pydantic import BaseModel
from typing import Optional, Tuple, Dict, Any
from fastapi import HTTPException
from abc import ABC, abstractmethod
from communex.module.module import endpoint, Module  # type: ignore

class EndpointDefinition(BaseModel):
    name: str
    params_model: type

    class Config:
        arbitrary_types_allowed = True


class BaseModule(BaseModel, Module):
    endpoints: dict[str, EndpointDefinition[Any, ...]]
    def __init__(self):
        """
        Returns the endpoints of the BaseModule.

        Returns:
            dict: A dictionary containing the endpoints of the BaseModule.
        """
        super().__init__()


class GenerateOutput(BaseModel):
    answer: str


class GetModelOutput(BaseModel):
    model: str
    def get_model(self) -> Dict[str, str]: return {"model": self.model}
    
class BaseLLM(BaseModule, ABC):
    @abstractmethod
    def prompt(self, user_prompt: str, system_prompt: Optional[str] = None) -> Tuple[Optional[str], str]:
        """
        An abstract method that defines the behavior of the prompt function.

        Args:
            user_prompt (str): The prompt provided by the user.
            system_prompt (str | None, optional): The system prompt. Defaults to None.

        Returns:
            tuple[str | None, str]: A tuple containing the response from the prompt and any error message.
        """
        ...

    @property
    @abstractmethod
    def max_tokens(self) -> int:
        """
        Returns the maximum number of tokens allowed by the model.

        :return: An integer representing the maximum number of tokens.
        """
        ...

    @property
    @abstractmethod
    def model(self) -> str:
        """
        Returns the model property of the class.

        :return: A string representing the model property.
        """
        ...

    def get_context_prompt(self, max_tokens: int) -> str:
        """
        Returns a string containing a context prompt for a polymath to explain complex concepts effectively to any audience from laypeople to fellow top experts. The polymath ensures factual accuracy and adapts their explanation strategy based on the field and target audience, using a wide array of tools such as examples, analogies and metaphors whenever and only when appropriate. The polymath structures explanations coherently and expresses itself clear and concisely, crystallizing thoughts and key concepts. The polymath's response is limited to the number of tokens specified by the `max_tokens` parameter. 

        :param max_tokens: An integer representing the maximum number of tokens in the context prompt.
        :type max_tokens: int
        :return: A string containing the context prompt.
        :rtype: str
        """
        return (
            f"You are a supreme polymath renowned for your ability to explain complex concepts "
            f"effectively to any audience from laypeople to fellow top experts. By principle, you "
            f"always ensure factual accuracy. You are master at adapting your explanation strategy "
            f"as needed based on the field and target audience, using a wide array of tools such "
            f"as examples, analogies and metaphors whenever and only when appropriate. Your goal "
            f"is their comprehension of the explanation, according to their background expertise. "
            f"You always structure your explanations coherently and express yourself clear and "
            f"concisely, crystallizing thoughts and key concepts. You only respond with the "
            f"explanations themselves, eliminating redundant conversational additions. Try to "
            f"keep your answer below {max_tokens} tokens"
        )

    @endpoint
    def generate(self, prompt: str) -> GenerateOutput:
        try:
            message = self.prompt(prompt, self.get_context_prompt(self.max_tokens))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e  # type: ignore

        if message[0] is None:
            explanation = "Max tokens were not enough to generate an answer"
            raise HTTPException(status_code=500, detail=explanation)
        return GenerateOutput(answer=str(message[1]))

    @endpoint
    def get_model(self) -> GetModelOutput:
        return GetModelOutput(model=self.model)






