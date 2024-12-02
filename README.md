# Wordsmith Documentation

## Overview
The Text Processing API is designed to provide multiple features for text enhancement, including spelling correction, text summarization, grammar correction, and suggestions to improve written content. This API leverages advanced models like T5, Falcon, and Google Gemini for natural language processing tasks. The front-end interface allows users to input text and receive processed results through simple HTTP POST requests.

## Running the Application

### Requirements:
- Python 3.10 or above
- Install required packages:
  ```bash
  pip install flask transformers happytransformer google-generativeai
  ```

---
### Steps:
1. **Set up the Flask Application**: Ensure the provided Python script (`app.py`) is saved in your project directory.
2. **Configure Google API**: Make sure to set up your Google API key in the script. Replace the placeholder in `genai.configure(api_key="YOUR_API_KEY")`.
3. **Run the Application**:
   In your terminal, navigate to the project folder and run:
   
   ```bash
   flask run
   ```
   
5. **Access the Application**: Open a web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/). You will be able to interact with the interface and test the text processing features.

---

## API Endpoints

### GET /  
**Description:**  
This endpoint serves the main interface HTML file that contains the text input fields and buttons for the user to interact with the various text processing features.

**Response:**
- Content-Type: `text/html`
- Status: 200 OK  
- The `index.html` file is served to the client.

### POST /process_spelling  
**Description:**  
This endpoint is used to process and correct the spelling of the provided input text using the T5 large spelling model.

**Request Body (JSON):**
```json
{
  "text": "Input text with spelling errors."
}
```

**Response Body (JSON):**
```json
{
  "spelling_corrected": "Corrected text with proper spelling."
}
```

**Notes:**
- The input text is truncated to a maximum of 1000 characters.
- The output will be the spelling-corrected text.

process_summarization(), process_suggestions() and process_grammar() work in the same way.

## Front-End Interface

The front-end interface is a web page that interacts with the above API endpoints. It provides an easy-to-use form where users can input text and select the desired processing option. The page also displays the output of the text processing tasks.

### Features:
1. **Text Input**: Users can enter text into a large text area.
2. **Buttons**: There are four buttons to trigger different operations:
   - Fix Spelling
   - Summarize Text
   - Fix Grammar
   - Get Suggestions
3. **Result Display**: The output for each operation is displayed in a separate area below the buttons. The processed results can also be copied to the clipboard.

### How to Use:
- **Step 1:** Enter the text to be processed in the provided textarea.
- **Step 2:** Choose the desired operation by clicking one of the buttons.
- **Step 3:** The result will be displayed in the output box.
- **Step 4:** Optionally, you can copy the result to your clipboard.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
