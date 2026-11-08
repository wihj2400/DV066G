import ollama
import csv

model1 = "llama3.2:3b"
model2 = "gemma3:1b"

prompt = "What is the largest country by size in the European Union?"

response1 = ollama.chat(model=model1, messages=[{"role": "user", "content": prompt}])
output1 = response1['message']['content']
print(model1, output1)

response2 = ollama.chat(model=model2, messages=[{"role": "user", "content": prompt}])
output2 = response2['message']['content']
print(model2, output2)

def add_to_csv(filename, row, new=False):
    mode = 'w' if new else 'a+'
    with (open(filename, mode=mode, newline='') as file):
        writer = csv.writer(file, delimiter=';')
        writer.writerow(row)



add_to_csv("assignment1.csv", ['Prompt', 'Llama3.2', 'Gemma3'],
           new=True)

add_to_csv('assignment1.csv', [prompt, output1, output2])