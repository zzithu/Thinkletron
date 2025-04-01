# We handle core logic here, so we can place everything necessary in here

#This is the skeleton for how I sort of expect code flow to go

# On intialization
def __init__():
    #yada yada
    #likely setup the chat interface and AI
    #and we can introduce the player to their world with an initial scenario free of context


#I forget how control works in python, this will be changed
def main():
    #Enter a while loop (until we determine some condition where we end)

    #First, we must store the chatlogs
    messages = {}
    
    #We are best to update that with the shorthand from gemini or whatever LLM you choose
    
    #We want to pass messages as context to Level Control
    #Then we can store that as a variable
    #newContext = GenerateLevelContext(messages)

    #From there, we want to pass both the current shorthand chat history and new context into api
    #temp = APICALL(messages, newContext)

    #and add that message to messages 
    #messages.add(temp) #I forget proper format but this is the idea
    #and then we repeat
    