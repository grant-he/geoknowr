import os
import base64
import logging
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from llama_api_client import LlamaAPIClient

client = LlamaAPIClient(
    base_url="https://api.llama.com/v1/",
    api_key=os.environ.get("LLAMA_API_KEY"),
)

# --- Configuration ---
UPLOAD_FOLDER = 'api_uploads'  # Folder where uploaded images will be stored for processing
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'} # Allowed image extensions
# Get current date for logging or other purposes if needed
# from datetime import datetime
# CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload size

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Ensure the upload folder exists ---
try:
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    logger.info(f"Upload folder '{UPLOAD_FOLDER}' is ready.")
except OSError as e:
    logger.error(f"Could not create upload folder '{UPLOAD_FOLDER}': {e}")
    # Depending on the severity, you might want to exit or handle this differently
    # For now, the application will continue, but uploads will likely fail.

# --- Helper Function ---
def allowed_file(filename):
    """Checks if the uploaded file has an allowed extension."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# --- Your Processing Function ---
def know(filepath):
    """
    This function is called after an image is successfully uploaded and saved.
    It receives the path to the saved image file.

    Args:
        filepath (str): The absolute or relative path to the saved image file.
    """
    logger.info(f"Function 'know' called with filepath: {filepath}")
    image = encode_image(filepath)
    
    response = client.chat.completions.create(
        messages=[
        {
            "role": "user",
            "content": [
            {
                "type": "image_url",
                "image_url": {
                "url": f"data:image/png;base64,{image}"
                }
            },
            {
                "type": "text",
                "text": "Tell me about the distinctive features in this picture that help determine what country this is in. Determine which side of road people are driving on in the picture, then eliminate countries that don'\''t match that information according to the following json dictionary:\n{\n\"Botswana\": \"left\",\n\"Eswatini\": \"left\",\n\"Kenya\": \"left\",\n\"Lesotho\": \"left\",\n\"Malawi\": \"left\",\n\"Mauritius\": \"left\",\n\"Mozambique\": \"left\",\n\"Namibia\": \"left\",\n\"South Africa\": \"left\",\n\"Tanzania\": \"left\",\n\"Uganda\": \"left\",\n\"Zambia\": \"left\",\n\"Zimbabwe\": \"left\",\n\"Bangladesh\": \"left\",\n\"Bhutan\": \"left\",\n\"Brunei\": \"left\",\n\"Hong Kong\": \"left\",\n\"India\": \"left\",\n\"Indonesia\": \"left\",\n\"Japan\": \"left\",\n\"Malaysia\": \"left\",\n\"Nepal\": \"left\",\n\"Pakistan\": \"left\",\n\"Singapore\": \"left\",\n\"Sri Lanka\": \"left\",\n\"Thailand\": \"left\",\n\"Timor-Leste\": \"left\",\n\"Cyprus\": \"left\",\n\"Ireland\": \"left\",\n\"Malta\": \"left\",\n\"United Kingdom\": \"left\",\n\"Australia\": \"left\",\n\"Fiji\": \"left\",\n\"Kiribati\": \"left\",\n\"New Zealand\": \"left\",\n\"Papua New Guinea\": \"left\",\n\"Samoa\": \"left\",\n\"Solomon Islands\": \"left\",\n\"Tonga\": \"left\",\n\"Tuvalu\": \"left\",\n\"Barbados\": \"left\",\n\"Bahamas\": \"left\",\n\"Jamaica\": \"left\",\n\"Saint Kitts and Nevis\": \"left\",\n\"Saint Lucia\": \"left\",\n\"Saint Vincent and the Grenadines\": \"left\",\n\"Trinidad and Tobago\": \"left\",\n\"Macau\": \"left\",\n\"Suriname\": \"left\",\n\"Afghanistan\": \"right\",\n\"Albania\": \"right\",\n\"Algeria\": \"right\",\n\"Andorra\": \"right\",\n\"Angola\": \"right\",\n\"Antigua and Barbuda\": \"right\",\n\"Argentina\": \"right\",\n\"Armenia\": \"right\",\n\"Austria\": \"right\",\n\"Azerbaijan\": \"right\",\n\"Bahrain\": \"right\",\n\"Belarus\": \"right\",\n\"Belgium\": \"right\",\n\"Belize\": \"right\",\n\"Benin\": \"right\",\n\"Bolivia\": \"right\",\n\"Bosnia and Herzegovina\": \"right\",\n\"Brazil\": \"right\",\n\"Bulgaria\": \"right\",\n\"Burkina Faso\": \"right\",\n\"Burundi\": \"right\",\n\"Cabo Verde\": \"right\",\n\"Cambodia\": \"right\",\n\"Cameroon\": \"right\",\n\"Canada\": \"right\",\n\"Central African Republic\": \"right\",\n\"Chad\": \"right\",\n\"Chile\": \"right\",\n\"China\": \"right\",\n\"Colombia\": \"right\",\n\"Comoros\": \"right\",\n\"Congo (Congo-Brazzaville)\": \"right\",\n\"Costa Rica\": \"right\",\n\"Croatia\": \"right\",\n\"Cuba\": \"right\",\n\"Czech Republic\": \"right\",\n\"Democratic Republic of the Congo\": \"right\",\n\"Denmark\": \"right\",\n\"Djibouti\": \"right\",\n\"Dominica\": \"right\",\n\"Dominican Republic\": \"right\",\n\"Ecuador\": \"right\",\n\"Egypt\": \"right\",\n\"El Salvador\": \"right\",\n\"Equatorial Guinea\": \"right\",\n\"Eritrea\": \"right\",\n\"Estonia\": \"right\",\n\"Ethiopia\": \"right\",\n\"Finland\": \"right\",\n\"France\": \"right\",\n\"Gabon\": \"right\",\n\"Gambia\": \"right\",\n\"Georgia\": \"right\",\n\"Germany\": \"right\",\n\"Ghana\": \"right\",\n\"Greece\": \"right\",\n\"Grenada\": \"right\",\n\"Guatemala\": \"right\",\n\"Guinea\": \"right\",\n\"Guinea-Bissau\": \"right\",\n\"Guyana\": \"right\",\n\"Haiti\": \"right\",\n\"Honduras\": \"right\",\n\"Hungary\": \"right\",\n\"Iceland\": \"right\",\n\"Iran\": \"right\",\n\"Iraq\": \"right\",\n\"Israel\": \"right\",\n\"Italy\": \"right\",\n\"Ivory Coast\": \"right\",\n\"Jordan\": \"right\",\n\"Kazakhstan\": \"right\",\n\"Kuwait\": \"right\",\n\"Kyrgyzstan\": \"right\",\n\"Laos\": \"right\",\n\"Latvia\": \"right\",\n\"Lebanon\": \"right\",\n\"Liberia\": \"right\",\n\"Libya\": \"right\",\n\"Liechtenstein\": \"right\",\n\"Lithuania\": \"right\",\n\"Luxembourg\": \"right\",\n\"Madagascar\": \"right\",\n\"Maldives\": \"right\",\n\"Mali\": \"right\",\n\"Marshall Islands\": \"right\",\n\"Mauritania\": \"right\",\n\"Mexico\": \"right\",\n\"Micronesia\": \"right\",\n\"Moldova\": \"right\",\n\"Monaco\": \"right\",\n\"Mongolia\": \"right\",\n\"Montenegro\": \"right\",\n\"Morocco\": \"right\",\n\"Myanmar\": \"right\",\n\"Nauru\": \"right\",\n\"Netherlands\": \"right\",\n\"Nicaragua\": \"right\",\n\"Niger\": \"right\",\n\"Nigeria\": \"right\",\n\"North Korea\": \"right\",\n\"North Macedonia\": \"right\",\n\"Norway\": \"right\",\n\"Oman\": \"right\",\n\"Palau\": \"right\",\n\"Palestine\": \"right\",\n\"Panama\": \"right\",\n\"Paraguay\": \"right\",\n\"Peru\": \"right\",\n\"Philippines\": \"right\",\n\"Poland\": \"right\",\n\"Portugal\": \"right\",\n\"Qatar\": \"right\",\n\"Romania\": \"right\",\n\"Russia\": \"right\",\n\"Rwanda\": \"right\",\n\"San Marino\": \"right\",\n\"Sao Tome and Principe\": \"right\",\n\"Saudi Arabia\": \"right\",\n\"Senegal\": \"right\",\n\"Serbia\": \"right\",\n\"Seychelles\": \"right\",\n\"Sierra Leone\": \"right\",\n\"Slovakia\": \"right\",\n\"Slovenia\": \"right\",\n\"Somalia\": \"right\",\n\"South Korea\": \"right\",\n\"South Sudan\": \"right\",\n\"Spain\": \"right\",\n\"Sudan\": \"right\",\n\"Sweden\": \"right\",\n\"Switzerland\": \"right\",\n\"Syria\": \"right\",\n\"Tajikistan\": \"right\",\n\"Togo\": \"right\",\n\"Tunisia\": \"right\",\n\"Turkey\": \"right\",\n\"Turkmenistan\": \"right\",\n\"Ukraine\": \"right\",\n\"United Arab Emirates\": \"right\",\n\"United States\": \"right\",\n\"Uruguay\": \"right\",\n\"Uzbekistan\": \"right\",\n\"Vanuatu\": \"right\",\n\"Vatican City\": \"right\",\n\"Venezuela\": \"right\",\n\"Vietnam\": \"right\",\n\"Yemen\": \"right\"\n}\nFinally please respond with your guess for the top three countries in the format.\n[1] Top guess\n[2] second guess\n[3] third guess\n"
            }
            ]
        },
        ],
        model="Llama-4-Maverick-17B-128E-Instruct-FP8",
        # stream=True,
        temperature=0.6,
        max_completion_tokens=2048,
        top_p=0.9,
        repetition_penalty=1,
        tools=[
        ],
    )

    print(response.completion_message.content.text)
    # for chunk in response:
    #     print(chunk)
    
    processing_result = {"status": "success", "message": response.completion_message.content.text, "processed_filepath": filepath}
    logger.info(f"'know' function processing complete for {filepath}. Result: {processing_result}")
    return processing_result

# --- API Endpoint ---
@app.route('/api/push/know', methods=['POST'])
def handle_image_push():
    """
    API endpoint to receive an image file.
    It expects a multipart/form-data request with a file part named 'image'.
    """
    logger.info(f"Received request at /api/push/know at {app.config.get('CURRENT_DATE', 'N/A')}") # Example of using date

    if request.method == 'POST':
        # Check if the post request has the file part
        if 'image' not in request.files: # Ensure the key matches what the client sends
            logger.warning("No 'image' part in the request files.")
            return jsonify({"error": "No image part in the request"}), 400

        file = request.files['image']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            logger.warning("No selected file (filename is empty).")
            return jsonify({"error": "No selected file"}), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename) # Sanitize the filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            try:
                file.save(filepath)
                logger.info(f"Image saved successfully to: {filepath}")

                # Call your know(filepath) function
                processing_status = know(filepath)

                # You can customize the response based on what `know` returns
                if processing_status.get("status") == "success":
                    return jsonify({
                        "message": "Image uploaded and processed successfully.",
                        "filename": filename,
                        "details": processing_status.get("message", "")
                    }), 200
                else:
                    # If know() indicates an error during its processing
                    return jsonify({
                        "error": "Image uploaded, but processing failed.",
                        "filename": filename,
                        "details": processing_status.get("message", "Unknown processing error.")
                    }), 500

            except Exception as e:
                logger.error(f"Error saving file or in 'know' function: {e}", exc_info=True)
                return jsonify({"error": f"An error occurred: {str(e)}"}), 500
        else:
            logger.warning(f"File type not allowed: {file.filename}")
            return jsonify({"error": f"File type not allowed. Allowed types are: {', '.join(ALLOWED_EXTENSIONS)}"}), 400

    # Should not be reached if only POST is allowed, but as a fallback:
    return jsonify({"error": "Method not allowed"}), 405

# --- Main Execution ---
if __name__ == '__main__':
    logger.info("Starting Flask server...")
    # For production, use a proper WSGI server like Gunicorn or uWSGI
    # Example: gunicorn -w 4 -b 0.0.0.0:5000 app:app
    app.run(host='0.0.0.0', port=8000, debug=True) # Set debug=False for production