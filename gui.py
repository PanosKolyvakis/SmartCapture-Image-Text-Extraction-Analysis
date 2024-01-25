import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def run_gui():
    def get_selected_prompt():
        selected_value = prompt_var.get()
        if selected_value in prompts_instructions.keys():
            return selected_value
        else:
            return ''

    def get_custom_prompt():
        return custom_prompt_text.get("1.0", tk.END).strip()
        
    def get_selected_model():
        return gpt_var.get() 

    def submit_and_close():
        global selected_prompt , selected_model , custom_prompt
        selected_prompt = get_selected_prompt()
        selected_model = get_selected_model()
        custom_prompt = get_custom_prompt()
        root.destroy()

    root = tk.Tk()
    root.geometry("500x600+0+0")
    style = ttk.Style(root)
    style.theme_use('clam') 
    root.title("OpenAI - GPT Response")
    root.configure(bg = '#FAF0E6')
    gpt_var = tk.StringVar(root)
    gpt_models = {'GPT-4' : 'GPT-4' , 'GPT-4-Turbo' : 'gpt-4-1106-preview' ,  'GPT-3.5' : 'gpt-3.5-turbo-1106'}

    prompt_menu = ttk.Combobox(root, textvariable=gpt_var ,values=list(gpt_models.keys()) )

    gpt_var.set('GPT-4-Turbo' )

    prompt_menu.pack(pady=5, padx=8)
    image_path = '/Users/panoskolyvakis/VSprojects/ImageToText/ImageGraphic.png'
    image = Image.open(image_path)

    # Resize the image to desired size, e.g., (width, height)
    image = image.resize((380, 350))
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    image_label = tk.Label(root, image=photo , bg = '#FAF0E6' , fg = 'black')
    image_label.image = photo 
    image_label.pack()
    prompt_var = tk.StringVar(root)
    question_label = tk.Label(root, text="What do you want to know? - Select from the dropdown box " , bg = '#FAF0E6' , fg= 'black')

    question_label.pack(pady=5, padx=5)
    
    prompts_instructions = {
        'Verbal reasoning test': "Verbal reasoning test: if this contains many letters or possible answers please answer only from the text and return the best answer deduced only from the text",
        'General overview': "Give me a general overview of this text, what does the author mean",
        'Coding question': "this is a coding question, please return your best effort in writing code to solve the question",
        'Rewrite this Text': 'Rewrite the following text',
        'Explain code': 'write this code line by line in different boxes and explain each line of the code separately. Use ``` line of code ``` and then explanation in formatting'
        # these ``` are used on how the IDE.py works. please do not edit
    }

    prompt_menu = ttk.Combobox(root, textvariable=prompt_var, values=list(prompts_instructions.keys()))
    prompt_menu.pack(pady=5, padx=5)

    custom_prompt_label = tk.Label(root, text = "  Enter your custom prompt below, or supplement selected prompt  " , bg = '#FAF0E6' , fg = 'black')
    custom_prompt_label.pack()
    custom_prompt_text = tk.Text(root, height=5, width=40, bg='#F0F0F0', fg='black')
    custom_prompt_text.pack(pady=10, padx=5)

    submit_button = ttk.Button(root, text="Submit", command=submit_and_close, style="TButton")
    submit_button.pack(pady=5, padx=5)

    # configure the submit button 
    style.configure("TButton", background="#F5F5F5", foreground="black", font=('Helvetica', 14))
    submit_button.pack(pady=5, padx=5)


    root.mainloop()


    # building the final prompt (dropbox , textbox or combined)
    if selected_prompt and not custom_prompt:
        final_prompt = prompts_instructions.get(selected_prompt, '')
        if custom_prompt != '':
            final_prompt = custom_prompt
    else:
        
        final_prompt = prompts_instructions.get(selected_prompt, '') + ' ' + custom_prompt


    return final_prompt , gpt_models[selected_model]

if __name__ == '__main__':

    print(run_gui())
