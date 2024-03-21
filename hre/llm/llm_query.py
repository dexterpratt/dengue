from hre.llm.openai_query import openai_chat

def llm_query(context, prompt, model, temperature, max_tokens,LOG_FILE):
    response = openai_chat(context, 
                       prompt, 
                       model,
                       temperature, 
                       max_tokens, 
                       LOG_FILE)
    return response

                      
