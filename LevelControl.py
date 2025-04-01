#This program is responsible for controlling the flow of the player. It generates
#unique environments

#This is skeleton / starter code


#Here we can pass any degree of context into the level
def generateLevelContext(string Context):
    #Call AI model, as it to generate a scenario given context, the context being the shorthand text
    #from your calls or if we plan on creating presets
    prompt = """Context: {Context} You are a chatbot responsible for determining the outcome of whatever 
            scenario the player has found themselves in"""
    
    #Do Generation

    #Return the string
