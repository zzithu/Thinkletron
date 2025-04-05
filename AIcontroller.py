from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

#I just seperated this to make it cleaner to call
class AIcontroller:
    #intialize the model
    def __init__(self, model_name="Qwen/Qwen2.5-0.5B-Instruct"):
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto"
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    #And we can control different values here, and we can pass message history
    def prompt(self, messages: list[dict], max_new_tokens: int = 512) -> str:
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

        generated_ids = self.model.generate(
            **model_inputs,
            max_new_tokens=max_new_tokens
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]
        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response


# If you want to continue the conversation, just add the assistant's reply to history:
# history.append({"role": "assistant", "content": reply}) This is the ideal form