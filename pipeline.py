import gradio as gr
from gtts import gTTS

def callBack1(Record, Recorded_File):
    return f"Welcome to Gradio!"

def callBack2(txt_inp):
	aud = gTTS(text=txt_inp, lang='en', slow=False)
	aud.save("test.mp3")
	print("Over")
	return "test.mp3"

with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Stage 1: Speech ➡️ Text ➡️ Animation!
    Start recording to see the output.
    """)
    
    with gr.Row():
    	mic = gr.Audio(sources=["microphone"], label="Speech")
    	aud_file = gr.File(label="Recorded Speech")
    	out = gr.Textbox(label="Text")

    with gr.Row():
    	clr_btn = gr.ClearButton([mic, aud_file])
    	run_btn = gr.Button("Run")
    	run_btn.click(fn=callBack1, inputs=[mic, aud_file], outputs=out)
    
    
    gr.Markdown(
    """
    # Stage 2: Action ➡️ Text ➡️ Speech!
    Start camera to see the output.
    """)
    
    with gr.Row():
#    	input_img = gr.Image(sources=["webcam"], streaming=True)
 #   	output_img = gr.Image()
    	#input_img.stream(flip, input_img, output_img)
    	txt_inp = gr.Textbox(
    		label="Text", 
    		value="The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a gr.Interface, the label will be the name of the parameter this component is assigned to.")
    	aud_out = gr.Audio(label="Speech")
    	
    with gr.Row():
    	clr_btn = gr.ClearButton([txt_inp, aud_out])
    	run_btn = gr.Button("Run")
    	run_btn.click(fn=callBack2, inputs=[txt_inp], outputs=aud_out)
    	
demo.launch(share=True)
