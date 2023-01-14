import typing
import openai
import logging

# Using OpenAI's chat GPT to create a story/world

# ! Definitions
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

def createResponse(config:dict, feature:str) -> typing.Tuple[str, str]:
    """
    Use OpenAI's API to generate a response based on the aspect and prompt from the config.json file.

    Args:
        config (dict): The configuration of the prompt.
        feature (str): The feature of the prompt you wish create a description for. It should be plural form and work with the default prompt "Describe the {feature} of a ...".

    Returns:
        tuple [str, str]: The prompt, The Model's response.
    """

    prompt = config.get("prompt", "Describe the {feature} of a village.")
    prompt = prompt.replace("{feature}", feature)

    model = config.get("model", "text-davinci-003")
    temp = clamp((int)(config.get("temperature", 1)))
    max_tokens = (int)(config.get("max_tokens", 64))

    logging.info(
        f"""Generating completion:
        Model: {model}
        Prompt: {prompt}
        Temperature: {temp}
        Max Tokens: {max_tokens}
        """)

    try:
        response = openai.Completion.create(
            model=model, 
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temp
        )

        logging.info(f"Response: {response.choices[0].text}")
        return prompt, response.choices[0].text
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return (f"{e}", "")

if __name__ == "__main__":
    # Imports
    import json
    import os
    from dotenv import load_dotenv

    # Logging
    logging.basicConfig(level=logging.WARNING)

    # Config
    config = {}
    with open("config.json", "r") as f:
        config = json.loads(f.read())

    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    print(createResponse(config, ""))
