from autogen import ConversableAgent

OPENAI_API_KEY = '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'

llm_config = {
    "config_list": [
        {
            "model": "llama3-70b-8192",
            "base_url": "https://api.groq.com/openai/v1",
            "api_key": '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',
            "api_type": "groq"
        }
    ],
}

 
agent = ConversableAgent(
    name="chatbot",
    llm_config=llm_config,
    human_input_mode="NEVER",
)
 
 
reply = agent.generate_reply(
    messages=[{"content": "Tell me a joke.", "role": "user"}]
)

print(reply)
 
reply = agent.generate_reply(
    messages=[{"content": "Repeat the joke.", "role": "user"}]
)

print(reply)
 