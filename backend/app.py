import os
import json
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
UPLOAD_FOLDER = (
    "api_uploads"  # Folder where uploaded images will be stored for processing
)
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}  # Allowed image extensions
# Get current date for logging or other purposes if needed
# from datetime import datetime
# CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB max upload size

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
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


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

    road_map = {
        "Botswana": "left",
        "Eswatini": "left",
        "Kenya": "left",
        "Lesotho": "left",
        "Malawi": "left",
        "Mauritius": "left",
        "Mozambique": "left",
        "Namibia": "left",
        "South Africa": "left",
        "Tanzania": "left",
        "Uganda": "left",
        "Zambia": "left",
        "Zimbabwe": "left",
        "Bangladesh": "left",
        "Bhutan": "left",
        "Brunei": "left",
        "Hong Kong": "left",
        "India": "left",
        "Indonesia": "left",
        "Japan": "left",
        "Malaysia": "left",
        "Nepal": "left",
        "Pakistan": "left",
        "Singapore": "left",
        "Sri Lanka": "left",
        "Thailand": "left",
        "Timor-Leste": "left",
        "Cyprus": "left",
        "Ireland": "left",
        "Malta": "left",
        "United Kingdom": "left",
        "Australia": "left",
        "Fiji": "left",
        "Kiribati": "left",
        "New Zealand": "left",
        "Papua New Guinea": "left",
        "Samoa": "left",
        "Solomon Islands": "left",
        "Tonga": "left",
        "Tuvalu": "left",
        "Barbados": "left",
        "Bahamas": "left",
        "Jamaica": "left",
        "Saint Kitts and Nevis": "left",
        "Saint Lucia": "left",
        "Saint Vincent and the Grenadines": "left",
        "Trinidad and Tobago": "left",
        "Macau": "left",
        "Suriname": "left",
        "Afghanistan": "right",
        "Albania": "right",
        "Algeria": "right",
        "Andorra": "right",
        "Angola": "right",
        "Antigua and Barbuda": "right",
        "Argentina": "right",
        "Armenia": "right",
        "Austria": "right",
        "Azerbaijan": "right",
        "Bahrain": "right",
        "Belarus": "right",
        "Belgium": "right",
        "Belize": "right",
        "Benin": "right",
        "Bolivia": "right",
        "Bosnia and Herzegovina": "right",
        "Brazil": "right",
        "Bulgaria": "right",
        "Burkina Faso": "right",
        "Burundi": "right",
        "Cabo Verde": "right",
        "Cambodia": "right",
        "Cameroon": "right",
        "Canada": "right",
        "Central African Republic": "right",
        "Chad": "right",
        "Chile": "right",
        "China": "right",
        "Colombia": "right",
        "Comoros": "right",
        "Congo (Congo-Brazzaville)": "right",
        "Costa Rica": "right",
        "Croatia": "right",
        "Cuba": "right",
        "Czech Republic": "right",
        "Democratic Republic of the Congo": "right",
        "Denmark": "right",
        "Djibouti": "right",
        "Dominica": "right",
        "Dominican Republic": "right",
        "Ecuador": "right",
        "Egypt": "right",
        "El Salvador": "right",
        "Equatorial Guinea": "right",
        "Eritrea": "right",
        "Estonia": "right",
        "Ethiopia": "right",
        "Finland": "right",
        "France": "right",
        "Gabon": "right",
        "Gambia": "right",
        "Georgia": "right",
        "Germany": "right",
        "Ghana": "right",
        "Greece": "right",
        "Grenada": "right",
        "Guatemala": "right",
        "Guinea": "right",
        "Guinea-Bissau": "right",
        "Guyana": "right",
        "Haiti": "right",
        "Honduras": "right",
        "Hungary": "right",
        "Iceland": "right",
        "Iran": "right",
        "Iraq": "right",
        "Israel": "right",
        "Italy": "right",
        "Ivory Coast": "right",
        "Jordan": "right",
        "Kazakhstan": "right",
        "Kuwait": "right",
        "Kyrgyzstan": "right",
        "Laos": "right",
        "Latvia": "right",
        "Lebanon": "right",
        "Liberia": "right",
        "Libya": "right",
        "Liechtenstein": "right",
        "Lithuania": "right",
        "Luxembourg": "right",
        "Madagascar": "right",
        "Maldives": "right",
        "Mali": "right",
        "Marshall Islands": "right",
        "Mauritania": "right",
        "Mexico": "right",
        "Micronesia": "right",
        "Moldova": "right",
        "Monaco": "right",
        "Mongolia": "right",
        "Montenegro": "right",
        "Morocco": "right",
        "Myanmar": "right",
        "Nauru": "right",
        "Netherlands": "right",
        "Nicaragua": "right",
        "Niger": "right",
        "Nigeria": "right",
        "North Korea": "right",
        "North Macedonia": "right",
        "Norway": "right",
        "Oman": "right",
        "Palau": "right",
        "Palestine": "right",
        "Panama": "right",
        "Paraguay": "right",
        "Peru": "right",
        "Philippines": "right",
        "Poland": "right",
        "Portugal": "right",
        "Qatar": "right",
        "Romania": "right",
        "Russia": "right",
        "Rwanda": "right",
        "San Marino": "right",
        "Sao Tome and Principe": "right",
        "Saudi Arabia": "right",
        "Senegal": "right",
        "Serbia": "right",
        "Seychelles": "right",
        "Sierra Leone": "right",
        "Slovakia": "right",
        "Slovenia": "right",
        "Somalia": "right",
        "South Korea": "right",
        "South Sudan": "right",
        "Spain": "right",
        "Sudan": "right",
        "Sweden": "right",
        "Switzerland": "right",
        "Syria": "right",
        "Tajikistan": "right",
        "Togo": "right",
        "Tunisia": "right",
        "Turkey": "right",
        "Turkmenistan": "right",
        "Ukraine": "right",
        "United Arab Emirates": "right",
        "United States": "right",
        "Uruguay": "right",
        "Uzbekistan": "right",
        "Vanuatu": "right",
        "Vatican City": "right",
        "Venezuela": "right",
        "Vietnam": "right",
        "Yemen": "right",
    }
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{image}"},
                    },
                    {
                        "type": "text",
                        "text": (
                            "Tell me about the distinctive features in this picture "
                            "that help determine what country this is in. Determine "
                            "which side of road people are driving on in the picture, "
                            "then eliminate countries that don't match that "
                            "information according to the following json dictionary:\n"
                            f"{json.dumps(road_map)}\n"
                            "Finally please respond with your guess for the top three "
                            "countries in the format.\n"
                            "[1] Top guess\n[2] second guess\n[3] third guess\n"
                        ),
                    },
                ],
            },
        ],
        model="Llama-4-Maverick-17B-128E-Instruct-FP8",
        # stream=True,
        temperature=0.6,
        max_completion_tokens=2048,
        top_p=0.9,
        repetition_penalty=1,
        tools=[],
    )

    print(response.completion_message.content.text)
    # for chunk in response:
    #     print(chunk)

    processing_result = {
        "status": "success",
        "message": response.completion_message.content.text,
        "processed_filepath": filepath,
    }
    logger.info(
        f"'know' function processing complete for {filepath}. Result: {processing_result}"
    )
    return processing_result


# --- API Endpoint ---
@app.route("/api/push/know", methods=["POST"])
def handle_image_push():
    """
    API endpoint to receive an image file.
    It expects a multipart/form-data request with a file part named 'image'.
    """
    logger.info(
        f"Received request at /api/push/know at {app.config.get('CURRENT_DATE', 'N/A')}"
    )  # Example of using date

    if request.method == "POST":
        # Check if the post request has the file part
        if "image" not in request.files:  # Ensure the key matches what the client sends
            logger.warning("No 'image' part in the request files.")
            return jsonify({"error": "No image part in the request"}), 400

        file = request.files["image"]

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            logger.warning("No selected file (filename is empty).")
            return jsonify({"error": "No selected file"}), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # Sanitize the filename
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

            try:
                file.save(filepath)
                logger.info(f"Image saved successfully to: {filepath}")

                # Call your know(filepath) function
                processing_status = know(filepath)

                # You can customize the response based on what `know` returns
                if processing_status.get("status") == "success":
                    return (
                        jsonify(
                            {
                                "message": "Image uploaded and processed successfully.",
                                "filename": filename,
                                "details": processing_status.get("message", ""),
                            }
                        ),
                        200,
                    )
                else:
                    # If know() indicates an error during its processing
                    return (
                        jsonify(
                            {
                                "error": "Image uploaded, but processing failed.",
                                "filename": filename,
                                "details": processing_status.get(
                                    "message", "Unknown processing error."
                                ),
                            }
                        ),
                        500,
                    )

            except Exception as e:
                logger.error(
                    f"Error saving file or in 'know' function: {e}", exc_info=True
                )
                return jsonify({"error": f"An error occurred: {str(e)}"}), 500
        else:
            logger.warning(f"File type not allowed: {file.filename}")
            return (
                jsonify(
                    {
                        "error": f"File type not allowed. Allowed types are: {', '.join(ALLOWED_EXTENSIONS)}"
                    }
                ),
                400,
            )

    # Should not be reached if only POST is allowed, but as a fallback:
    return jsonify({"error": "Method not allowed"}), 405


# --- Main Execution ---
if __name__ == "__main__":
    logger.info("Starting Flask server...")
    # For production, use a proper WSGI server like Gunicorn or uWSGI
    # Example: gunicorn -w 4 -b 0.0.0.0:5000 app:app
    app.run(host="0.0.0.0", port=8000, debug=True)  # Set debug=False for production
