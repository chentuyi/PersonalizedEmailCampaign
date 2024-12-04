import openai
import re

class LinkedinProcessor:

    # Constructor
    def __init__(self, api_key, linkedin):
        openai.api_key = api_key
        self.linkedin = linkedin

    # Step 0: Make an OpenAI call
    def call_openai(self, question):
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": question}])
        content = chat_completion.choices[0].message.content
        return content

    # Step 1: Check if a user input is a valid linkedin, return True if it is valid
    def is_valid_linkedin(self):
        # Regular expression for matching LinkedIn profile URLs and job URLs
        linkedin_pattern = r"^(https?:\/\/)?(www\.)?linkedin\.com\/(in\/[a-zA-Z0-9_-]+|company\/[a-zA-Z0-9_-]+|job\/[a-zA-Z0-9_-]+)(\/|\?)?.*$"
        
        # If the pattern matches the input URL, return True
        return bool(re.match(linkedin_pattern, self.linkedin))

    # TODO: Step 2: Extract information from linkedin profile using crawlers
    
    # Step 3: Generate personalized email campaign

    def generate_email_campaign(self, product, customer):
        question = f"Please generate personalized email campaign for {customer} to promote product {product}"
        content = self.call_openai(question)
        return content

    def process_linkedin(self):
        if not self.is_valid_linkedin():
            return "Invalid linkedin"

        # Dummy customer data
        customer = "Tuyi Chen is an experienced ETL Developer with a demonstrated history of working in the information technology and services industry. She has skills in Oracle, Teradata, Snowflake, Microsoft Azure, Amazon Redshift, Linux/Unix commands, shell scripts, Python, Java 8, SQL Query Optimization, Data Analysis, and Machine Learning. She likes playing League of Legends. She can speak English and Mandarin."
        
        # Dummy product data
        product1 = self.generate_email_campaign("ThinkPad P14s Gen 5 AMD (14″) Mobile Workstation", customer)
        product2 = self.generate_email_campaign("ThinkPad X1 Carbon Gen 11 Intel (14”) - Black", customer)
        product3 = self.generate_email_campaign("Legion Pro 7i Gen 9 Intel (16″) with RTX™ 4090", customer)

        result = {
            "product1": product1,
            "product2": product2,
            "product3": product3
        }

        return result
