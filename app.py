from flask import Flask, request, jsonify,send_file
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from happytransformer import HappyTextToText, TTSettings
import google.generativeai as genai

genai.configure(api_key="AIzaSyCIiPD6eIAeCPGef2YBPcpST0EQ7BPfx3g")

app = Flask(__name__)

# Humming Face Models
tokenizer_spell = AutoTokenizer.from_pretrained("ai-forever/T5-large-spell")
model_spell = AutoModelForSeq2SeqLM.from_pretrained("ai-forever/T5-large-spell")

summarizer = pipeline("summarization", model="Falconsai/text_summarization")
happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")

# genai model
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # 


@app.route("/", methods=["GET"])
def index():
    return send_file("index.html")


@app.route("/process_spelling", methods=["POST"])
def process_spelling():
    input_text = request.json.get('text')

    inputs = tokenizer_spell(input_text, return_tensors="pt", padding=True, truncation=True, max_length=1000)
    outputs = model_spell.generate(inputs["input_ids"], max_new_tokens=1000)
    decoded_output = tokenizer_spell.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"spelling_corrected": decoded_output})

@app.route("/process_summarization", methods=["POST"])
def process_summarization():
    input_text = request.json.get('text')
    summary = summarizer(input_text, max_length=400, min_length=30, do_sample=False)
    summary_text = summary[0]['summary_text']

    return jsonify({"summarized": summary_text})

@app.route("/process_grammar", methods=["POST"])
def process_grammar():
    input_text = request.json.get('text')
    args = TTSettings(num_beams=10, min_length=1, max_length=1000)
    grammar_result = happy_tt.generate_text("grammar:" + input_text, args=args)

    return jsonify({"grammar_corrected": grammar_result.text})

@app.route("/process_suggestions", methods=["POST"])
def process_suggestions():
    input_text = request.json.get('text')
    prompt = f"""Please provide suggestions to improve the following text, only provide the imroved text do no give any lines
    such as "here is the improved text" etc:
    
    {input_text}
    """

    try:
        response = model.generate_content(prompt)
        if response.text:
            return jsonify({"suggestions": response.text})
        else:
            return jsonify({"suggestions": "No suggestions available."})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
