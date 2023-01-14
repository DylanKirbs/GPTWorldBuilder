I generated these images using OpenAI's DALL-E and a variation of this prompt:
> Describe the {feature} of a magical kingdom with tall walls of stone and great lakes of pure water. Ivy covered buildings and a magnificent castle with a crooked mage tower in it's shadow. There are powerful runes inscribed on the enormous iron framed wooden gates that provide protection to the city within. Large fields of wheat and beautiful flowing rivers surround the walls.

I used GPT-3 to fill in the `{feature}` of the prompt as well.
> The great machines of this magical kingdom are powered by a combination of magic and technology. The most impressive of these machines are the giant clockwork automatons that patrol the city walls and guard the gates. These automatons are made of a combination of metal and stone and are powered by a combination of magical and mechanical energy. They are capable of understanding and responding to commands from their masters and can be programmed to perform a variety of tasks.The city also has a number of magical machines that are powered by the same combination of magic and technology.
> 
> The mage of this magical kingdom has a variety of powers, including the ability to manipulate the elements of nature, such as wind, water, fire, and earth. They can also cast powerful spells to protect the kingdom from harm, as well as summon creatures from other realms. They can also use their powers to heal the sick and injured, and to create powerful magical artifacts. The mage also has the ability to communicate with the spirits of the dead, and to use their knowledge to gain insight into the future. Finally, the mage can use their powers to create illusions and manipulate the minds of others.
> 
> The runes of this magical kingdom are intricate and powerful. They are inscribed on the walls, gates, and buildings of the city, and are used to protect the city from harm. The runes are inscribed in a variety of shapes and sizes, and each rune has a specific purpose. Some runes are used to ward off evil, while others are used to bring luck and prosperity. The runes are also used to control the weather, to bring rain when needed and to keep the sun shining when it is too hot.The runes are also used to control the flow of energy within the city.
> 
> The local language of this magical kingdom is a complex and beautiful one, with intricate patterns and uses. It is a language of symbols and metaphors, of hidden meanings and secret codes. It is a language of power and knowledge, of magic and mystery. It is a language of the heart and soul, of the spirit and the mind.The language is used to communicate with the gods and goddesses, to cast spells and to invoke powerful forces. It is used to create powerful charms and talismans, to protect and to heal. It is used to tell stories and to share wisdom, to express love and to create.
> 
> The streets are lined with cobblestone and the buildings are made of white marble and gold. The roofs are made of slate and the windows are made of stained glass. The castle is the centerpiece of the kingdom, with its grand towers and spires reaching up to the sky. The lake is a deep blue and the water is so clear that you can see the bottom. The air is filled with the smell of fresh flowers and the sound of birds singing. The magical kingdom is a place of beauty and wonder, a place of dreams and adventure.
> 
> The air is filled with the sweet smell of wildflowers and the sound of birds singing in the trees. The sun shines brightly on the cobblestone streets and the people of the kingdom go about their daily lives. The castle stands tall and proud, a beacon of hope and strength for the people of the kingdom. The lake is a deep blue and the water is so clear that you can see the bottom. The magical kingdom is a place of beauty and wonder, a place of dreams and adventure.
> 
> Beyond the walls lies a dark and dangerous land. The shadows are filled with creatures of the night, from giant spiders to dark and twisted creatures of the underworld. The air is thick with the smell of death and decay, and the ground is littered with bones and the remains of those who have ventured too far. The trees are twisted and gnarled, and the sky is filled with a thick fog that never seems to lift. The creatures of the night lurk in the shadows, waiting for unsuspecting travelers to stumble upon them. They are powerful and cunning, and they will stop at nothing to get what they want.

And it was as simple as a few lines of code in `python`.
```python
import openai

response = openai.Completion.create(
    model=model, 
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=temp
)

print(response.choices[0].text)
```

This is a stripped down version, for more visit the OpenAI beta. https://openai.com/api/