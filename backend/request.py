import os
from llama_api_client import LlamaAPIClient

client = LlamaAPIClient(
    base_url="https://api.llama.com/",
    api_key=os.environ.get("LLAMA_API_KEY"),
)

response = client.chat.completions.create(
    messages=[
      {
        "role": "system",
        "content": "You are a geography expert."
      },
      {
        "role": "user",
        "content": [
          {
            "type": "image_url",
            "image_url": {
              "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAAAXNSR0IArs4c6QAAAiBJREFUaEPtWU1KQ0EMnt7DG1RpeSIqLryH4qIoFIoLQY+h4EIKBUsXovdwIepGLOp5lAgDY5jJzzTvD99blpkkX/Ilk6S9tX7x7Vr89ToANUevi0DNAXD/JwIXpxNXDAdusLFeqtOXH5/u7X3pLm+mIj1sBPZ3d9z0+kokzPrQ5OzcPT6/kGJZAF+vT9Z2qeRxIEgAQJvR0aFKofXhlQA83M7+cH5xdy/mZi4Q7DTIiYOTcVIcGQFMn/72Xq5dqnsavUkAseStCwBFIzEALpQqFzOHMXWzAGAuxvgfnrHMj0oAxCqUFQiJ83wQkxTihKTeB4s8wflH0TcJgAtj6wGUSaFKIgAcLCuJTQBoHhPLEuplSfUnc0AqoAzjQaZUf+UAgB7j49Fvj0WV3UYC0CR+4wBQrXksEo0CIJkrMIiVAeCHDL+wnsuQcNQMKzHeF4IQhDmAsCOUcjllPBgKX2za8yBKA8B51BtAGe83Dqkz0PuE2w+zXmhrsxDNyNiAGEX8b5xD4FwWgNhsGtsJpYzFDxxV8zkQJgBiLy5HF8rzWJ62zKrnAYlHpcmdaj8keYPvimfi8CJHB1hBwjebL9jNmiQSlD41AKuxkWoCuWEqvKsCUIXxsU40ayuhaWmtW2rpIwZ6yc1c61eLda7WpSWYjEATAHBrGvb/gTpBcKt1NgfC5GztX0zWFcZaHksha4XW8joA1h7VyusioPWY9fkfQM0LzylMtisAAAAASUVORK5CYII="
            }
          },
          {
            "type": "text",
            "text": "Tell me about the distinctive features in this picture that help determine what country this is in. Determine which side of road people are driving on in the picture, then eliminate countries that don'\''t match that information according to the following json dictionary:\n{\n\"Botswana\": \"left\",\n\"Eswatini\": \"left\",\n\"Kenya\": \"left\",\n\"Lesotho\": \"left\",\n\"Malawi\": \"left\",\n\"Mauritius\": \"left\",\n\"Mozambique\": \"left\",\n\"Namibia\": \"left\",\n\"South Africa\": \"left\",\n\"Tanzania\": \"left\",\n\"Uganda\": \"left\",\n\"Zambia\": \"left\",\n\"Zimbabwe\": \"left\",\n\"Bangladesh\": \"left\",\n\"Bhutan\": \"left\",\n\"Brunei\": \"left\",\n\"Hong Kong\": \"left\",\n\"India\": \"left\",\n\"Indonesia\": \"left\",\n\"Japan\": \"left\",\n\"Malaysia\": \"left\",\n\"Nepal\": \"left\",\n\"Pakistan\": \"left\",\n\"Singapore\": \"left\",\n\"Sri Lanka\": \"left\",\n\"Thailand\": \"left\",\n\"Timor-Leste\": \"left\",\n\"Cyprus\": \"left\",\n\"Ireland\": \"left\",\n\"Malta\": \"left\",\n\"United Kingdom\": \"left\",\n\"Australia\": \"left\",\n\"Fiji\": \"left\",\n\"Kiribati\": \"left\",\n\"New Zealand\": \"left\",\n\"Papua New Guinea\": \"left\",\n\"Samoa\": \"left\",\n\"Solomon Islands\": \"left\",\n\"Tonga\": \"left\",\n\"Tuvalu\": \"left\",\n\"Barbados\": \"left\",\n\"Bahamas\": \"left\",\n\"Jamaica\": \"left\",\n\"Saint Kitts and Nevis\": \"left\",\n\"Saint Lucia\": \"left\",\n\"Saint Vincent and the Grenadines\": \"left\",\n\"Trinidad and Tobago\": \"left\",\n\"Macau\": \"left\",\n\"Suriname\": \"left\",\n\"Afghanistan\": \"right\",\n\"Albania\": \"right\",\n\"Algeria\": \"right\",\n\"Andorra\": \"right\",\n\"Angola\": \"right\",\n\"Antigua and Barbuda\": \"right\",\n\"Argentina\": \"right\",\n\"Armenia\": \"right\",\n\"Austria\": \"right\",\n\"Azerbaijan\": \"right\",\n\"Bahrain\": \"right\",\n\"Belarus\": \"right\",\n\"Belgium\": \"right\",\n\"Belize\": \"right\",\n\"Benin\": \"right\",\n\"Bolivia\": \"right\",\n\"Bosnia and Herzegovina\": \"right\",\n\"Brazil\": \"right\",\n\"Bulgaria\": \"right\",\n\"Burkina Faso\": \"right\",\n\"Burundi\": \"right\",\n\"Cabo Verde\": \"right\",\n\"Cambodia\": \"right\",\n\"Cameroon\": \"right\",\n\"Canada\": \"right\",\n\"Central African Republic\": \"right\",\n\"Chad\": \"right\",\n\"Chile\": \"right\",\n\"China\": \"right\",\n\"Colombia\": \"right\",\n\"Comoros\": \"right\",\n\"Congo (Congo-Brazzaville)\": \"right\",\n\"Costa Rica\": \"right\",\n\"Croatia\": \"right\",\n\"Cuba\": \"right\",\n\"Czech Republic\": \"right\",\n\"Democratic Republic of the Congo\": \"right\",\n\"Denmark\": \"right\",\n\"Djibouti\": \"right\",\n\"Dominica\": \"right\",\n\"Dominican Republic\": \"right\",\n\"Ecuador\": \"right\",\n\"Egypt\": \"right\",\n\"El Salvador\": \"right\",\n\"Equatorial Guinea\": \"right\",\n\"Eritrea\": \"right\",\n\"Estonia\": \"right\",\n\"Ethiopia\": \"right\",\n\"Finland\": \"right\",\n\"France\": \"right\",\n\"Gabon\": \"right\",\n\"Gambia\": \"right\",\n\"Georgia\": \"right\",\n\"Germany\": \"right\",\n\"Ghana\": \"right\",\n\"Greece\": \"right\",\n\"Grenada\": \"right\",\n\"Guatemala\": \"right\",\n\"Guinea\": \"right\",\n\"Guinea-Bissau\": \"right\",\n\"Guyana\": \"right\",\n\"Haiti\": \"right\",\n\"Honduras\": \"right\",\n\"Hungary\": \"right\",\n\"Iceland\": \"right\",\n\"Iran\": \"right\",\n\"Iraq\": \"right\",\n\"Israel\": \"right\",\n\"Italy\": \"right\",\n\"Ivory Coast\": \"right\",\n\"Jordan\": \"right\",\n\"Kazakhstan\": \"right\",\n\"Kuwait\": \"right\",\n\"Kyrgyzstan\": \"right\",\n\"Laos\": \"right\",\n\"Latvia\": \"right\",\n\"Lebanon\": \"right\",\n\"Liberia\": \"right\",\n\"Libya\": \"right\",\n\"Liechtenstein\": \"right\",\n\"Lithuania\": \"right\",\n\"Luxembourg\": \"right\",\n\"Madagascar\": \"right\",\n\"Maldives\": \"right\",\n\"Mali\": \"right\",\n\"Marshall Islands\": \"right\",\n\"Mauritania\": \"right\",\n\"Mexico\": \"right\",\n\"Micronesia\": \"right\",\n\"Moldova\": \"right\",\n\"Monaco\": \"right\",\n\"Mongolia\": \"right\",\n\"Montenegro\": \"right\",\n\"Morocco\": \"right\",\n\"Myanmar\": \"right\",\n\"Nauru\": \"right\",\n\"Netherlands\": \"right\",\n\"Nicaragua\": \"right\",\n\"Niger\": \"right\",\n\"Nigeria\": \"right\",\n\"North Korea\": \"right\",\n\"North Macedonia\": \"right\",\n\"Norway\": \"right\",\n\"Oman\": \"right\",\n\"Palau\": \"right\",\n\"Palestine\": \"right\",\n\"Panama\": \"right\",\n\"Paraguay\": \"right\",\n\"Peru\": \"right\",\n\"Philippines\": \"right\",\n\"Poland\": \"right\",\n\"Portugal\": \"right\",\n\"Qatar\": \"right\",\n\"Romania\": \"right\",\n\"Russia\": \"right\",\n\"Rwanda\": \"right\",\n\"San Marino\": \"right\",\n\"Sao Tome and Principe\": \"right\",\n\"Saudi Arabia\": \"right\",\n\"Senegal\": \"right\",\n\"Serbia\": \"right\",\n\"Seychelles\": \"right\",\n\"Sierra Leone\": \"right\",\n\"Slovakia\": \"right\",\n\"Slovenia\": \"right\",\n\"Somalia\": \"right\",\n\"South Korea\": \"right\",\n\"South Sudan\": \"right\",\n\"Spain\": \"right\",\n\"Sudan\": \"right\",\n\"Sweden\": \"right\",\n\"Switzerland\": \"right\",\n\"Syria\": \"right\",\n\"Tajikistan\": \"right\",\n\"Togo\": \"right\",\n\"Tunisia\": \"right\",\n\"Turkey\": \"right\",\n\"Turkmenistan\": \"right\",\n\"Ukraine\": \"right\",\n\"United Arab Emirates\": \"right\",\n\"United States\": \"right\",\n\"Uruguay\": \"right\",\n\"Uzbekistan\": \"right\",\n\"Vanuatu\": \"right\",\n\"Vatican City\": \"right\",\n\"Venezuela\": \"right\",\n\"Vietnam\": \"right\",\n\"Yemen\": \"right\"\n}\nFinally please respond with your guess for the top three countries in the format.\n[1] Top guess\n[2] second guess\n[3] third guess\n"
          }
        ]
      },
      {
        "role": "assistant",
        "content": "The image shows a street view of a residential area with a car parked on the right side of the road. The car'\''s position indicates that drivers drive on the left side of the road in this country.\n\nAccording to the provided JSON dictionary, countries where drivers drive on the left side of the road include Australia, Bangladesh, Bhutan, Brunei, Hong Kong, India, Indonesia, Ireland, Japan, Kenya, Lesotho, Malaysia, Malta, Mauritius, Mozambique, Nepal, New Zealand, Pakistan, Singapore, South Africa, Sri Lanka, Tanzania, Thailand, Uganda, United Kingdom, Zambia, and Zimbabwe.\n\nTo narrow down the possibilities, let'\''s examine the image for other clues:\n\n*   The houses appear to be well-maintained and have a suburban or residential feel.\n*   The presence of a van and a car suggests a relatively modern and developed economy.\n*   The vegetation and climate appear to be temperate or subtropical.\n\nConsidering these factors, here are my top three guesses for the country:\n\n[1] **Australia**: The architecture, vegetation, and overall aesthetic of the image are consistent with Australian suburbs. The presence of a Honda car also supports this guess, as Honda is a popular brand in Australia.\n[2] **New Zealand**: The image could also be from New Zealand, given the similar climate and architectural styles.\n[3] **United Kingdom**: Although less likely due to the climate and vegetation, the image could potentially be from a region in the UK with a similar temperate climate, such as southern England.\n\nThese guesses are based on the available information and the process of elimination using the provided JSON dictionary.",
        "stop_reason": "stop"
      }
    ],
    model="Llama-4-Maverick-17B-128E-Instruct-FP8",
    stream=True,
    temperature=0.6,
    max_completion_tokens=2048,
    top_p=0.9,
    repetition_penalty=1,
    tools=[
    ],
)

for chunk in response:
    print(chunk)