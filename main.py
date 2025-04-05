from AIcontroller import AIcontroller
import gradio as gr

class AIStoryGame:
    #Create context and AI instance for the user.
    def __init__(self):
        #Feel free to add your initialization here

        
        #### Create Dungeon Master ####

        self.messages = []  # Stores chat logs sequentially
        self.context = [] # We store shorthand context here
        #Store as such for built in model: history.append({"role": "assistant", "content": reply})

        self.running = True  # Controls the main loop
        self.ai = AIcontroller() 

        #Create a personality for the chatbot
        AI_context = {"role": "system", "content": "[ROLE]: Dungeon Master\n[RESPONSIBILITIES]: Respond to the player with vivid descriptions and engaging scenarios.\n[STYLE]: Witty, dark fantasy, concise.\n[NOTES]: Never control the player character."}
        self.context.append(AI_context)

        #Generate a creative introduction
        intro_Context = [
            AI_context,
            {"role": "system", "content": "Key context:\n- The player is exploring a ruined magical tower.\n- The world is mysterious and slightly whimsical.\n- You should describe environments vividly and ask the player what they do next."},
            {"role": "system", "content": "You control all characters except the player.\nBe imaginative and concise.\nAvoid making decisions for the player."}
        ]

        #And we can begin
        intro = self.ai.prompt(intro_Context, 1024)
        introCleaned = ({"role": "system", "content": intro})
        self.messages.append(introCleaned)
        
    


        
    #Main runner, interact with the user and paint their journey
    def main(self):
        while self.running:
            # Display last AI message (if any)
            if self.messages:
                print(f"\n{self.messages[-1]['content']}")

            # Get user input / control flow
            user_input = input("\nWhat do you do? \nControls: \n-Type 'exit' to quit  \n-Type 'context' to view current bot understanding)")
            if user_input.lower() == "exit":
                self.running = False
                break

            if user_input.lower() == "context":
                show_context()
                

            # Add user input to context and visible messages
            user_message = ({"role": "user", "content": user_input})
            self.messages.append(user_message)

            #AI Determines fate!
            user_context = self.ai.prompt(user_message, 1024)

            # Generate AI response
            ai_response_content = user_input #Here you can put your shorthand call
            ai_message = ({"role": "system", "content": ai_response_content})

            # Store AI response in both message log and hidden context
            self.context.append(ai_message)


#Here the player can view context          
def show_context(self):
    print("\n--- Current Dungeon Context ---")
    for msg in self.context:
        if msg['role'] != 'system':  # You can include or exclude system msgs
            print(f"{msg['role'].capitalize()}: {msg['content']}")
    print("\n--- End of Context ---")



# Run the game
if __name__ == "__main__":
    game = AIStoryGame()
    game.main()