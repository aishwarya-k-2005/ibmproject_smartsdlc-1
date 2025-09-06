import gradio as gr

def greet(name):
    return f"Hello {name}, welcome to SmartSDLC!"

# Create Gradio interface
iface = gr.Interface(fn=greet, inputs="text", outputs="text", title="SmartSDLC Demo")

# Launch
if __name__ == "__main__":
    iface.launch()
