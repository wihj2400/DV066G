I used the models Llama3.2:3b and Gemma3:1b in order to try to see the difference between model sizes.

You run the code simply by running the Python script.
It submits the prompt, gets the responses, and adds them to the csv document.
Before running, you must have the Ollama pip package installed, and also the models themselves installed from Ollama.

The speed was definitely slower than running an LLM in a dedicated app or website, but surprisingly the 3b model was faster than the 1b model.
The 3b model was accurate whereas the 1b model was inaccurate, which is not surprising.
More extensive tests would be needed to determine whether a local model is better or worse than a commercial model, but for this simple test it's about equal if you run a model with a large enough size, provided you ignore the time needed to install Ollama and the model locally.