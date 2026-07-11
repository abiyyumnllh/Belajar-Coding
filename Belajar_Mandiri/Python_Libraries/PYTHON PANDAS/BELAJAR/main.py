import pandas as pd

data = {
    "nama_model" : ["GPT-4", "Claude-3", "Llama-3"],
    "perusahaan" : ["OpenAI", "Anthropic", "Meta"]
}

df = pd.DataFrame(data)

print(df)