import typing
import openai
import logging
import os
from dotenv import load_dotenv


# Load the OpenAI API key
def connectOpenAI():
    """
    Connect to OpenAI's API.

    Raises:
        Exception: If the API key is not set.
    """

    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if openai.api_key is None:
        raise Exception("OpenAI API key is not set.")


# ! Define the methods

# Define the type of the number
number = typing.Union[int, float]
def clamp(x:number, minimum:number=0, maximum:number=1) -> number:
    """
    Clamp a number between an upper and lower bound.

    Args:
        x (number): The number to be clamped.
        minimum (number, optional): The lower bound. Defaults to 0.
        maximum (number, optional): The upper bound. Defaults to 1.

    Returns:
        number: The clamped number.
    """
    
    return min(max(x, minimum), maximum)

def createTextResponse(
        prompt:str,
        engine:str="text-davinci-003",
        temperature:number=0.5,
        max_tokens:number=100,
        top_p:number=1,
        frequency_penalty:number=0,
        presence_penalty:number=0,
        stop:str=""
    ) -> str:
    """
    Create a text response using OpenAI's API.

    Args:
        prompt (str): The prompt to be used.
        engine (str, optional): The engine to be used. Defaults to "text-davinci-003".
        temperature (number, optional): How much to model can vary. Defaults to 0.5.
        max_tokens (number, optional): The maximum number of tokens to be generated. Defaults to 100.
        top_p (number, optional): The probability of the next token being generated. Defaults to 1.
        frequency_penalty (number, optional): The frequency penalty. Defaults to 0.
        presence_penalty (number, optional): The presence penalty. Defaults to 0.
        stop (str, optional): The stop string. Defaults to "".

    Returns:
        str: The generated text.
    """
    
    # Clamp the values
    temperature = clamp(temperature)
    max_tokens = clamp(max_tokens, 1, 2048)
    top_p = clamp(top_p)
    frequency_penalty = clamp(frequency_penalty)
    presence_penalty = clamp(presence_penalty)

    # Create the response
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop
    )

    # Return the text
    return response.choices[0].text

def createImageResponse(
        prompt:str,
        num_results:int=1,
        size:int=1024
    ) -> str:
    """
    Create an image response using OpenAI's API.

    Args:
        prompt (str): The prompt to be used.
        num_results (int, optional): The number of images to generate. Defaults to 1.
        size (int, optional): The size of the images. Defaults to 1024.

    Returns:
        str: The URL of the generated image.
    """
    endpoint = "https://api.openai.com/v1/images/generations"

    # Clamp the values
    num_results = clamp(num_results, 1, 10)
    
    if size not in [256, 512, 1024]:
        size = 1024

    size_str = f"{size}x{size}"

    response = openai.Image.create(
        prompt=prompt,
        n=num_results,
        size=size_str
    )

    return response.data[0].url