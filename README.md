# GPT World Builder

## Description

A `python` library that uses OpenAI's API's to generate **worlds**.

## Installation

Download the files and make sure to obtain an API key from OpenAI's beta.
Add a `.env` file to your directory with the contents:
> OPENAI_API_KEY=secrets

Obviously replace "secrets" with your API key :)

## Usage

There are two scripts to mess around with, the `builder.py` and the `main.py`. <br>
In the `main.py` you will be able to mess around with the API methods from OpenAI's text and image generators.
> API.createTextResponse("A poem about the sky")

Will generate a poem about the sky... hopefully, and return the string.

> API.createImageResponse("A drawing of a cat")

Will return a URL to the generated Image of a cat.

*Consider running the programs in a python venv...*

## Contributing

If you want to contribute please feel free to reach out to me or create an issue and we can chat about contributions. :)

## License

                     GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

Get the rest in the [License](LICENSE.md) file.