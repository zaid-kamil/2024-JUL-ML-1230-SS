# gradio application
import gradio as gr

def add_3_values(a,b,c):
    return a+b+c

ui = gr.Interface(
    fn = add_3_values,
    inputs=[gr.Slider(), gr.Number(), gr.Slider()],
    outputs=gr.Text(),
    examples=[
        [2,3,4],
        [1,2,3],
        [11,23,45],
    ]
)

def authenticate(username, password):
    return username == "admin" and password == "admin"

ui.launch(auth=authenticate)