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
                "input": """
Orshline: The Galactic Fuel of the Future

Orshline is much more than just a fuel. It is the very essence of interstellar exploration. Discovered by the enigmatic alien species known as the Estra, Orshline is a remarkably versatile and energy-dense compound that powers starships, space stations, and entire civilizations across galaxies. This extraordinary substance is more than a simple power source— it serves as the key to unlocking the future of space travel and possibly even the secrets of the universe.

The Origins of Orshline
Orshline was first encountered by the Estra, a highly advanced and mysterious alien race from the distant Elyon System. While exploring the far reaches of the universe, the Estra discovered Orshline within the heart of a dying star. The star's cataclysmic implosion created the ideal conditions for Orshline to form—a rare combination of high-energy radiation, magnetic fields, and intense gravitational pressure.

Upon recognizing the substance’s potential, the Estra realized that Orshline’s energy output was unlike any known material. It surpasses even the most advanced human-made fuels, including antimatter. Orshline produces vast amounts of energy from just a small amount of matter, making it perfect for powering starships that travel vast distances across the cosmos.

Key Features of Orshline
Interdimensional Energy Source
Orshline is a multi-dimensional energy source, meaning it can tap into the energy of parallel dimensions to produce power. This ability makes it highly efficient, as it draws energy from not only the physical universe but also from alternate planes of existence. With this property, Estra starships can achieve speeds that far exceed conventional space travel.

Pressure-Activated Transformation
While in its natural state as a dark matter-based fluid, Orshline can undergo a transformation into a gaseous form when exposed to specific environmental pressures. In the high-pressure environments of starship engines, it changes into a high-energy gas similar to gasoline. In this form, it can be combusted in a controlled manner to produce massive amounts of energy for propulsion.

Energy Density
Orshline’s energy density is beyond measure. It is 10,000 times more efficient than Earth’s best fuels, making it possible for starships to travel nearly endlessly without refueling. Just a gram of Orshline can power an Estra vessel for months, or even years, depending on the size and needs of the ship.

Adaptive Combustion
Orshline has the unique ability to adapt to different propulsion systems. Whether a ship uses conventional combustion engines, a fusion-powered drive, or even an advanced quantum drive, Orshline’s properties can be tuned to meet the specific demands of each propulsion system.

Self-Sustaining Fuel Cycle
One of the most fascinating aspects of Orshline is its self-sustaining fuel cycle. When used as fuel, Orshline releases energy that can be harnessed to create more Orshline through a complex process known as gravitational extraction. This means that ships and space stations can generate their own fuel while traveling, ensuring they will never run out of power.

Uses Beyond Space Travel
Though Orshline is primarily known for its role in powering alien starships, its potential extends far beyond space exploration:

Energy Production for Planets
On advanced Estra planets, Orshline is used in energy plants to provide clean, infinite energy. This has helped the Estra build a utopian society where the scarcity of energy is no longer an issue. Other alien civilizations are now investigating ways to replicate this boundless energy source.

Medical Applications
Orshline’s energy output is also harnessed for cutting-edge medical technologies. The Estra have developed devices that use Orshline’s energy to manipulate gravitational fields, enabling quantum healing. This has revolutionized healthcare, allowing Estra to cure diseases that are beyond the reach of conventional medicine.

Energy Weapons
Due to Orshline’s immense energy density, it has become an essential ingredient in energy-based weapons. Starships powered by Orshline can fire devastating energy blasts, capable of destroying entire fleets with a single shot. These weapons are highly regulated, as their destructive power is feared by many, including the Estra.

Terraforming
Orshline is also used in terraforming projects. Its ability to manipulate gravitational fields enables it to accelerate the process of turning inhospitable planets into livable worlds. By carefully adjusting gravitational forces, Orshline can alter a planet’s atmosphere, temperature, and even its geological structure, making it suitable for habitation in mere years.

The Orshline Crisis
Despite Orshline’s vast benefits, its power comes with a dark side. The Estra’s dependence on Orshline has led to the rise of powerful corporations and black markets centered around the substance. Rogue factions and pirates are constantly searching for ways to steal Orshline from alien systems, sparking intergalactic conflicts. There have been several incidents where rival factions attempted to hijack Orshline shipments, escalating tensions that threaten to engulf entire star systems.

To prevent Orshline from falling into the wrong hands, the Estra have established strict regulations governing its trade and use. Only select, trusted entities are authorized to access Orshline reserves, and many of the largest starships are equipped with state-of-the-art security systems to protect against theft.

The Future of Orshline
As humanity makes its first contact with the Estra and other alien races, the discovery of Orshline could have a profound impact on human history. Will Orshline unlock the vast possibilities of space exploration for humanity, or will it lead to catastrophic consequences in the hands of those who seek to exploit its power?

In Conclusion:
Orshline represents the pinnacle of alien innovation, offering unlimited potential for space travel, energy production, and technological progress. However, with great power comes great responsibility. As civilizations across the galaxy begin to discover Orshline’s potential, it could become the most valuable and dangerous commodity in existence.

Additional Ideas to Enhance Orshline’s Story:
Special Effects: Orshline may emit a pulsating glow that shifts in color depending on its state, pressure, or energy charge. The glow could indicate whether it’s in a fluid, gaseous, or charged state, making it a visually captivating substance.

Mystery Element: There could be a deeper mystery about Orshline’s origin—perhaps it was not formed naturally, but rather engineered by an ancient alien civilization that disappeared long ago. This could lead to a quest to discover the truth behind its creation and its purpose.

Artifacts and Relics: The Estra might have left behind Orshline-powered artifacts, some of which could contain ancient artificial intelligence or advanced knowledge from the Estra’s distant past. These relics could play a pivotal role in understanding Orshline’s true potential.
                        """,
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
