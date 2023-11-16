from flask import Flask, render_template, request, jsonify
import openai

# Set your OpenAI API key
openai.api_key = 'my-key'

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/prompt', methods=['POST'])
def handle_prompt():
    try:
        # Get the input prompt from the request
        data = request.get_json()
        prompt = data['prompt']

        # Call the OpenAI API using the correct method and parameters
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can choose a different engine
            prompt=prompt,
            temperature=0.7,  # You can adjust this based on your needs
            max_tokens=100
        )

        # Get the generated text from the OpenAI response
        generated_text = response['choices'][0]['text']

        # Return the generated text as a JSON response
        return jsonify({'generated_text': generated_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
