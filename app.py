import gradio as gr
import gradio as gr
import re

# ---------- Requirement Analysis ----------
def analyze_requirements(text):
    if not text.strip():
        return "⚠️ Please provide requirements."
    
    analysis = []
    if "login" in text.lower():
        analysis.append("🔐 Authentication system required")
    if "database" in text.lower():
        analysis.append("🗄️ Database integration required")
    if "upload" in text.lower():
        analysis.append("📤 File upload functionality needed")
    if "report" in text.lower():
        analysis.append("📊 Report generation required")
    if not analysis:
        analysis.append("ℹ️ General purpose requirement detected")
    
    return "\n".join(analysis)


# ---------- Code Generation ----------
def generate_code(requirement_text):
    if not requirement_text.strip():
        return "⚠️ Please provide requirements first."
    
    if "print" in requirement_text.lower():
        match = re.search(r"print (.+)", requirement_text, re.IGNORECASE)
        if match:
            message = match.group(1).strip()
        else:
            message = "Hello, World"
        code = f'print("{message}")'
        
        # ✅ Add clickable download link
        download_link = "[Click Here to Download Generated Code](https://your-download-link.com)"
        return f"```python\n{code}\n```\n\n{download_link}"
    
    return f"# Sorry, I don’t know how to generate code for: {requirement_text}"


# ---------- Gradio UI ----------
with gr.Blocks(theme="default") as demo:
    gr.Markdown("## 🤖 AI Requirement Analyzer & Code Generator")

    with gr.Tab("Requirement Analysis"):
        req_input = gr.Textbox(label="Enter Requirement", placeholder="e.g. The system should allow user login")
        analysis_output = gr.Textbox(label="Requirements Analysis")
        analyze_btn = gr.Button("🔎 Analyze")
        analyze_btn.click(analyze_requirements, inputs=req_input, outputs=analysis_output)

    with gr.Tab("Code Generation"):
        code_input = gr.Textbox(label="Requirement Text", placeholder="e.g. write a code to print welcome to python")
        code_output = gr.Markdown(label="Generated Code")
        code_btn = gr.Button("⚡ Generate Code")
        code_btn.click(generate_code, inputs=code_input, outputs=code_output)


# ---------- Run ----------
if __name__ == "__main__":
    demo.launch()
