import openai
from langchain.memory import ConversationKGMemory
from langchain.llms import OpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import ConversationChain

class ProductProcessor:

    # Constructor
    def __init__(self, api_key, message):
        openai.api_key = api_key
        # self.message = "Summarize the product information of " + message
        self.message = message
        print("ProductProcessor Constructor: " + self.message)

    # Step 1: Make an OpenAI call for general chat, return content in JSON response
    def call_openai(self):
        # Conversation KG Memory
        llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)
        memory = ConversationKGMemory(llm=llm)

        # Enter personal information, i.e virtual product created by us
        extra_info = [
            {
                "input": "Tuyi Chen has a background in Computer Science and Mathematics, and she is participating in today's Hackathon Demo.",
                "output": "cool"
            },
            {
                "input": "Email Campaign is an intelligent service to recommend products to those in need.",
                "output": "cool"
            }
        ]

        # Save extra information to memory context
        for example in extra_info:
            memory.save_context({"input": example["input"]}, {"output": example["output"]})

        # Conversations
        template = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context.
        If the AI does not know the answer to a question, it truthfully says it does not know. The AI ONLY uses information contained in the "Relevant Information" section and does not hallucinate.

        Relevant Information:

        {history}

        Conversation:
        Human: {input}
        AI:"""
        prompt = PromptTemplate(input_variables=["history", "input"], template=template)

        conversation_with_kg = ConversationChain(
            llm=llm, verbose=True, prompt=prompt, memory=memory
        )

        result = conversation_with_kg.predict(input=self.message)
        return result
