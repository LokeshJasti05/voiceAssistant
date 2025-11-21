from ast import Bytes, FormattedValue
from tkinter import Image
from unittest import result
from elevenlabs.conversational_ai.conversation import ClientTools
from websockets.typing import Data
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

def searchWeb(parameters):
    query = parameters.get("query")
    result = DuckDuckGoSearchRun(query=query)
    return result

def save_to_txt(parameters):
    filename = parameters.get("filename")
    data = parameters.get("data")

    formatted_data = f"{data}"

    with open(filename, "a" , encoding="utf-8") as file:
        file.write(formatted_data+"\n")

def create_html_file(parameters):
    filename = parameters.get("filename")
    data= parameters.get("data")
    title = parameters.get("title")

    formatted_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
    </head>
    <body>
        <h1>{title}</h1>
        <div>{data}</div>
    </body>
    </html>
    """
    with open(filename, "w" , encoding="utf-8") as file:
        file.write(formatted_html)

    def generate_image(parameters):
        prompt= parameters.get("prompt")
        filename = parameters.get("filename")
        size= parameters.get("size","1024x1024")
        save_dir = parameters.get("save_dir","generated_image")

        os.makedirs(save_dir,exist_ok=True)
        filepath= os.path.join(save_dir,filename)

        openai.api_key = os.getenv("OPENAI_API_KEY") 

        client = openai.OpenAI()

        response = openai.images.generate(
            prompt=prompt,
            model = "dall-e-3   ",
            n=1,
            size=size,
            quality = "standard"
            response_format="b64_json"
        )

        image_url = client["data"][0]["url"]
        image = Image.open(BytesIO(image_response.content))
        image.save(filepath)


client_tools = ClientTools()
client_tools.register("searchWeb",searchWeb)
client_tools.register("saveToTxt",save_to_txt)
client_tools.register("createHTMLFile",create_html_file)
client_tools.register("generateImage",generate_image)