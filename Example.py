#WARNING this is AI generated, this is how it interpreted our final structure to look

from level_manager import LevelManager
from ai_interface import AIInterface

class AIStoryGame:
    def __init__(self):
        """
        Initializes the AI-driven story game, setting up the level manager and AI interface.
        """
        self.messages = []  # Stores chat logs sequentially
        self.running = True  # Controls the main loop
        self.level_manager = LevelManager()
        self.ai_interface = AIInterface()

        # Generate initial story introduction
        initial_context = self.level_manager.generate_initial_context()
        self.messages.append({"role": "system", "content": initial_context})

    def main(self):
        """
        Main game loop handling user input and AI-driven story progression.
        """
        while self.running:
            # Display last AI message (if any)
            if self.messages:
                print(f"\n{self.messages[-1]['content']}")

            # Get user input
            user_input = input("\nWhat do you do? (or type 'exit' to quit) ")

            if user_input.lower() == "exit":
                self.running = False
                break

            # Store player's response
            self.messages.append({"role": "player", "content": user_input})

            # Generate new level context
            new_context = self.level_manager.generate_level_context(self.messages)

            # AI generates the next part of the story
            ai_response = self.ai_interface.generate_story(self.messages, new_context)

            # Store AI response
            self.messages.append(ai_response)


# Run the game
if __name__ == "__main__":
    game = AIStoryGame()
    game.main()
