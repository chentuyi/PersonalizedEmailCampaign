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
                "input": "Email Campaign is an intelligent service to recommend products to those in need.",
                "output": "cool"
            },
            {
                "input": "Haobing Chu is the mentor of AI Hackathon Team 5. He leads teams at 6sense, building targeted, personalized scalable marketing and sales campaigns for B2B enterprises using ML/AI.",
                "output": "cool"
            },
            {
                "input": "Tuyi Chen has an academic background in Computer Science and Mathematics. She works on front-end and openai calls of this project.",
                "output": "cool"
            },
            {
                "input": "Alisa Guo is a third-year software engineering student and she is interested in AI and cybersecurity. She works on Linkedin crawler of this project.",
                "output": "cool"
            },
            {
                "input": "Cynthia helps with Linkedin crawler of this project.",
                "output": "good"
            },
            {
                "input": "Sihui He is a fourth-year CS student from Western University. She previously worked at RBC, GM, and AudienceView as software developer intern.",
                "output": "good"
            },
            {
                "input": "Orsh is a virtual product invented by alien Estra. It is the fuel of alien starship and could be translate into gasoline under certain pressure.",
                "output": "good"
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
