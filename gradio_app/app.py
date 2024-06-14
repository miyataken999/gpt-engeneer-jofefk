import gradio as gr

def create_app():
    with gr.Blocks() as app:
        file_input = gr.inputs.File(type="file")
        btn = gr.inputs.Button("Upload")
        output = gr.outputs.Textbox(label="Output")

        def upload_file(file):
            # Call the FastAPI endpoint to upload the file
            response = requests.post("http://localhost:8000/upload_file", files={"file": file})
            return response.text

        btn.click(fn=upload_file, inputs=file_input, outputs=output)

    return app

if __name__ == "__main__":
    app = create_app()
    app.launch()