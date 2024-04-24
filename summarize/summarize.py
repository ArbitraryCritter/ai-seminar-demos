from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cpu" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen1.5-0.5B-Chat",
    device_map=device
)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen1.5-1.8B-Chat")

def generate_response(prompt, max_response_length=256):
  messages = [
      {"role": "system", "content": "Please write a short summary of the text"},
      {"role": "user", "content": prompt}
  ]
  text = tokenizer.apply_chat_template(
      messages,
      tokenize=False,
      add_generation_prompt=True
  )
  model_inputs = tokenizer([text], return_tensors="pt").to(device)

  generated_ids = model.generate(
      model_inputs.input_ids,
      max_new_tokens=max_response_length
  )
  generated_ids = [
      output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
  ]

  return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

print("Please enter a text to summarize. Type exit to terminate session.")
while True:
    print("\n")
    user_input = input("Input text: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = generate_response(user_input)
    print("\n")
    print("Summary:", response)