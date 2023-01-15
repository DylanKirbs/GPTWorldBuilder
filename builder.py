import json
import API

# Set the API key
API.connectOpenAI()

# Read through the builder.json file and get the configuration
with open("builder.json", "r") as file:
    builder = json.load(file)

config = builder["config"]
features = builder["features"]
responses = builder["responses"]

# Create the text response
for feature in features:
    responses[feature] = API.createTextResponse(
        prompt=config["prompt"].replace("{feature}", feature),
        engine=config["engine"],
        temperature=config["temperature"],
        max_tokens=config["max_tokens"],
    )
    print(f"Successfully built the response for {feature}!")

# Write the responses to the builder.json file
with open("builder.json", "w") as file:
    json.dump(builder, file, indent=4)

print("Successfully built the responses!")