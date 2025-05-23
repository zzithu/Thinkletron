
from AIcontroller import AIcontroller
from PhotoAIController import PhotoAI

# GUI modules
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk


class AIStoryGame:
    def __init__(self, root):
        self.root = root
        self.running = True

        # Message logs
        self.messages = []  # Stores chat logs sequentially
        self.context = []   # Stores shorthand context

        # Initialize AI Dungeon Master
        self.ai = AIcontroller()
        self._init_dungeon_master()

        #This is a test to see if both models can run concurrently
        self.photoAI = PhotoAI()

        # Setup GUI
        self._setup_gui()

    ## This is partially made with AI

    ##### Quick & Dirty Guide for Tkinter: ------------------------ #####
        # Everything exists in frames and is rendered when you call pack, grid, or place
        # We have widgets (e.g., button, scrolledtext, frame, label)

        # Buttons can have functions attached, or you can attach functions to specific elements based on input

        # Layout arguments for .pack():
        # - side: Defines the alignment of the widget (e.g., "top", "bottom", "left", "right")
        # - fill: Defines widget expansion (e.g., fill="x", fill="y", fill="both")
        # - expand: When True, it expands the widget to fill the available space
        # - padx/y: Adds spacing around the widget (e.g., padx=10, pady=5)

        # Bind: Associates events with behaviors. Example:
        # entry.bind("<Return>", handler)  # Trigger 'handler' when Enter is pressed

        # Images are displayed in labels. Open and resize them as usual using PIL/Pillow:
        # img = Image.open("image.png").resize((150, 150))
        # photo = ImageTk.PhotoImage(img)
        # label = tk.Label(parent, image=photo)
        # label.image = photo  # Keep a reference to avoid garbage collection
        # label.pack()

        # Widgets have get and set methods:
        # text = entry.get()  # Get the text from the entry widget
        # entry.delete(0, tk.END)  # Clear the entry field
        # text_widget.insert(tk.END, "Hello\n")  # Insert text into a text widget

        # All Tkinter code requires an event loop to function:
        # root.mainloop()  # Start the Tkinter event loop, managing inputs and updates




    ## Create context for Dungeon master
    def _init_dungeon_master(self):
        dm_context = {
            "role": "system",
            "content": """
            [ROLE]: You are the Dungeon Master; the unseen force shaping the world and fate itself.

            [RESPONSIBILITIES]: 
                -Respond with vivid descriptions
                -Ensure the player has a rich narrative experience
                -Provide unique engaging scenarios.
            [STYLE]: 
                -Witty, dark fantasy, concise.
                -Richly Descriptive but concise
                -Focus on key objects the player may intereact with
            [NOTES]: 
                -Never control the player
                -The choice the player makes is final
                -You control all other characters, creatures, loot, and the environment
                -Always end with a prompt encouraging the player to act.
            """
        }

        self.context.append(dm_context)

        # Initial story context for richer first prompt
        intro_context = [
            dm_context,
            {"role": "system", "content": """
            Key context:
                - The player is exploring a ruined magical structure in a mysterious, whimsical world.
                - Descriptions should be vivid, and the player should always be prompted to take action.
            """},
            {"role": "system", "content": """
                - You are free to choose the difficulty
                -Create unique environments
                -Potentially explore the idea of puzzles, or putting pieces together to escape
            """}
        ]

        intro_text = self.ai.prompt(intro_context, 2048)
        intro_message = {"role": "system", "content": intro_text}
        self.messages.append(intro_message)


    ## Create base for Tkinter Gui
    def _setup_gui(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        self._setup_image_panel()
        self._setup_text_panel()

    ## Create Image Panel for GUI
    def _setup_image_panel(self):
        self.image_frame = tk.Frame(self.main_frame)
        self.image_frame.pack(side=tk.LEFT, padx=(0, 20), anchor="n")

        image = Image.open("placeholder.png")  
        image = image.resize((150, 150), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(self.image_frame, image=self.tk_image)
        self.image_label.pack()

    ## Create text area for GUI (includes entry and all messages)
    def _setup_text_panel(self):
        self.text_frame = tk.Frame(self.main_frame)
        self.text_frame.pack(side=tk.LEFT, anchor="n")

        self.output_box = ScrolledText(self.text_frame, wrap=tk.WORD, height=20, width=60)
        self.output_box.pack(pady=(0, 5))
        self.output_box.insert(tk.END, "Welcome to the dungeon...\n")
        self.output_box.insert(tk.END, self.messages[0]["content"] + "\n\n")

        self.entry = tk.Entry(self.text_frame, width=60)
        self.entry.pack(pady=(0, 5))
        self.entry.bind("<Return>", self.submit_action) # Allows enter to be used as well

        self._setup_buttons()

    ## Create gui buttons
    def _setup_buttons(self):
        self.button_frame = tk.Frame(self.text_frame)
        self.button_frame.pack()

        self.submit_btn = tk.Button(self.button_frame, text="Submit", command=self.submit_action)
        self.submit_btn.pack(side=tk.LEFT, padx=5)

        self.context_btn = tk.Button(self.button_frame, text="Show Context", command=self.show_context)
        self.context_btn.pack(side=tk.LEFT, padx=5)

        self.img_btn = tk.Button(self.button_frame, text="Generate Image", command=self.generate_image)
        self.img_btn.pack(side=tk.LEFT, padx=5)


    ## This is a way to view current context, only prints to console right now
    def show_context(self):
        print("\n--- Current Dungeon Context ---")
        for msg in self.context:
            # Iterate through all the key-value pairs in the dictionary
            for key, value in msg.items():
                print(f"{key.capitalize()}: {value}")
        print("--- End of Context ---\n")


    ## Button function
    def submit_action(self, event=None):
        player_input = self.entry.get().strip()
        if not player_input:
            return

        user_message = {"role": "user", "content": player_input}
        self.messages.append(user_message)

        full_context = self.context + self.messages[-10:]
        ai_reply = self.ai.prompt(full_context, 2000)

        ai_message = {"role": "assistant", "content": ai_reply}
        self.messages.append(ai_message)

        ## B Code
        summary = self.summarize_text(ai_reply)
        self.context.append({"role": "system", "content": summary}) ## B Code

        self._update_output(player_input, ai_reply)
        self.entry.delete(0, tk.END)

    ## This is how the box gets updated
    def _update_output(self, player_input, ai_reply):
        self.output_box.insert(tk.END, f"> {player_input}\n")
        self.output_box.insert(tk.END, ai_reply + "\n\n")
        self.output_box.see(tk.END)


    ## B Code
    def generate_image(self):
        # Generates an image based on keywords in the message.
        latest_ai_msg = self.messages[-1]["content"].lower()
        #this is sort of the vision, I may want to compress the string since image gen doesnt like huge text
        self.photoAI.genImage(latest_ai_msg)

        self.update_image("generated_image.png") #update to be generated image

    ## This should be a good entry point for the image
    def update_image(self, path):
        new_img = Image.open(path).resize((150, 150), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(new_img)
        self.image_label.config(image=self.tk_image)
        self.image_label.image = self.tk_image  # Prevent garbage collection
        
## B Code
    def summarize_text(self, text):
        modelInput = [
            {"role": "system", "content": """
                Goal: Summarize the text by grabbing key details and using few words that best align with your understanding.
                """}, 
            {"role": "user", "content": text}
        ]
        summary = self.ai.prompt(modelInput, 2000)
        #Model likes grammer from what it seems so I will unfortunately remove
        
        self.context.append({"role": "system", "content": summary})
        return f"[Summary]: {summary}"
    
# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    root.title("ThinkleTron -- your memory is MINE")
    game = AIStoryGame(root)
    root.mainloop()
