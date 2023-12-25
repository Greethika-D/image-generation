# Image Generation Application with CLIPDrop API and Streamlit

## Overview

This repository contains a Python-based image generation application that leverages the CLIPDrop API for text-to-image generation. The application provides both a command line interface (CLI) and a user-friendly interface powered by Streamlit.

## Prerequisites

Before using the application, ensure you have the following installed:

- Python 3.x
- Required Python packages (install via `pip install -r requirements.txt`)
- CLIPDrop API key (obtain from [CLIPDrop website](https://clipdrop.co/))



## Usage - Command Line Interface (CLI)

1. **Modify Prompt:**
   Open `app.py` in your preferred Python IDE.
   Modify the `prompt` variable with your desired text prompt.

2. **Run the Script:**
   Execute the script to generate an image.
 

## Usage - Streamlit Interface

1. **Run Streamlit App:**
   ```bash
   streamlit run streamlit_app.py
   ```
2. **Access Interface:**
   Open your browser and navigate to the link it provides you.

3. **Generate Image:**
   - Enter a text prompt in the input box.
   - Click the "Generate Image" button.

4. **View Results:**
   The generated image will be displayed on the interface.

## Usage - Streamlit with Text History

1. **Run Streamlit App:**
   ```bash
   streamlit run text.py
   ```

2. **Access Interface:**
     Open your browser and navigate to the link it provides you.

3. **Generate Image with Text History:**
   - Enter a text prompt in the input box.
   - Click the "Generate Image" button.

4. **View Results and History:**
   The generated image will be displayed, and your previous questions and responses will be saved in the text area below.

## Notes

- Ensure your CLIPDrop API key is valid and configured in `config.py`.
- Streamlit interfaces can be customized based on your requirements.

Feel free to explore and customize the application to meet your specific needs.
