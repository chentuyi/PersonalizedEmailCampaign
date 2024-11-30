# Personalized Email Campaign

Need to run both portal and server!

### email-campaign-portal
1. Front-end using React and TypeScript
2. Note that you may need to install some packages to run the front-end
- cd email-campaign-portal
- npm install
- npm run dev
3. If you want to modify front-end, please refers to email-campaign-portal/README.md for more details

### email-campaign-server
1. Back-end using Python, OpenAI
2. Note that you may need to install some packages to run the back-end, such as flask, openai, langchain, etc.
- cd email-campaign-server
- python3 server.py
3. The entry point of the server: server.py
- Note that the OPENAI_API_KEY is private and not able to share in GitHub, please create .env file at same level of server.py and have OPENAI_API_KEY there.
- API routes are generated here. Front-end need to call same API routes, i.e http://localhost:5000/process_linkedin, if you are running server on port 5000.
4. The other two classes linkedin_processor.py and chat_processor.py are examples to call openai
