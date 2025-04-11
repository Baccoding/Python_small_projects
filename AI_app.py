from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import gradio as gr

model_name = "microsoft/phi-2"  # You can also try "gpt2" or any Hugging Face model

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def chat(prompt, history=[]):
    input_text = " ".join([f"User: {p}\nAI: {r}" for p, r in history] + [f"User: {prompt}\nAI:"])
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=150, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).split("AI:")[-1].strip()
    history.append((prompt, response))
    return response, history

gr.ChatInterface(fn=chat, title="Mini ChatGPT", description="A lightweight GPT-style chatbot using Hugging Face models").launch()