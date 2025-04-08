from diffusers import StableDiffusionPipeline
import torch


from diffusers import StableDiffusionPipeline
import torch

class PhotoAI:
    def __init__(self):
        # Initialize model and move to GPU in half-precision
        self.model_id = "sd-legacy/stable-diffusion-v1-5"
        self.pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16)
        self.pipe = self.pipe.to("cuda")  # Move model to GPU
    
    def genImage(self, prompt, save_path="generated_image.png"):
        # Generate an image from the provided prompt
        image = self.pipe(prompt).images[0]  # Get the first image in case of batch
        
        # Save the generated image
        image.save(save_path)
        print(f"Image saved as: {save_path}")


# Example usage:
if __name__ == "__main__":
    # Create an instance of the PhotoAI class
    photo_ai = PhotoAI()
    
    # Generate image with a prompt and save it
    prompt = "a photo of an astronaut riding a horse on mars"
    photo_ai.genImage(prompt, "astronaut_rides_horse.png")
