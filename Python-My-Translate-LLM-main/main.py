from dotenv import load_dotenv
from langchain.chains.summarize.map_reduce_prompt import prompt_template
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import  StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes

load_dotenv()

model = ChatOpenAI(temperature=0.3)#0 a yaklaştıkça daha net kesin detaylı cevaplar verir 1 e yaklaştıkça saçmalayabilme ihtimali var

system_prompt="Translate the following into {language}"

prompt_template=ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),("user","{text}")
    ]
)
parser = StrOutputParser()
chain = prompt_template | model | parser

app = FastAPI(
    title="Chat OpenAI",
    description="OpenAI Chat",
    version="1.0",
)

add_routes(
    app,
    chain,
    path="/chain"
)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)