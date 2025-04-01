#THis is ai generated, but this is sort of what I expect my final code to look like

class LevelManager:
    def __init__(self):
        """
        Initializes the LevelManager, which is responsible for dynamically generating 
        story contexts based on player interactions.
        """
        self.presets = [
            "You find yourself in a ruined castle, its halls echoing with whispers of the past.",
            "A dense fog rolls in as you stand at the crossroads of an unfamiliar town.",
            "The ground trembles beneath you as an ancient force awakens in the distance.",
        ]

    def generate_initial_context(self):
        """
        Returns a predefined introduction to set the stage for the player's adventure.
        This can be expanded to support randomization or specific story arcs.
        """
        return "You awaken in a dark forest with no memory of how you got here..."

    def generate_level_context(self, context):
        """
        Generates a new level scenario based on the given context.

        Parameters:
        - context (str): A summary of previous events or decisions.

        Returns:
        - str: The next scenario based on the context.
        """
        # If no prior context, select a preset
        if not context or context.strip() == "":
            return self.presets[0]

        # Construct a dynamic prompt
        prompt = f"""Context: {context} 
        You are a storyteller responsible for determining what happens next in this interactive adventure.
        Generate a compelling next scenario based on the current events.
        """

        # Here, we’d call an AI model (stubbed for now)
        new_scenario = self.call_ai_model(prompt)

        return new_scenario

    def call_ai_model(self, prompt):
        """
        Placeholder for calling an AI model to generate a response.
        This would typically be an API request to an LLM.
        """
        # Example stubbed response (Replace with real API call)
        return f"[AI-Generated] The world shifts, responding to your choices... {prompt[:50]}..."
