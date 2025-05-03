import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import logging # For better logging

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

# --- Your Processing Function ---
def know(filepath):
    """
    This function is called after an image is successfully uploaded and saved.
    It receives the path to the saved image file.

    Args:
        filepath (str): The absolute or relative path to the saved image file.
    """
    logger.info(f"Function 'know' called with filepath: {filepath}")
    #
    # --- YOUR IMAGE PROCESSING LOGIC GOES HERE ---
    #
    # For example, you might:
    # 1. Load the image using a library like Pillow (PIL) or OpenCV:
    #    from PIL import Image
    #    try:
    #        img = Image.open(filepath)
    #        logger.info(f"Successfully loaded image: {filepath}, format: {img.format}, size: {img.size}")
    #        # Perform analysis, recognition, etc.
    #    except FileNotFoundError:
    #        logger.error(f"Image file not found at path: {filepath}")
    #        return {"status": "error", "message": "Processed file not found server-side."}
    #    except Exception as e:
    #        logger.error(f"Error processing image {filepath} in 'know' function: {e}")
    #        return {"status": "error", "message": f"Error during image processing: {str(e)}"}
    #
    # 2. Call another service or model with this image.
    # 3. Update a database.
    #
    # For this example, we'll just log that it was called.
    # Replace this with your actual image processing tasks.
    #
    # This function could return a result that the API then sends back,
    # or it could trigger background tasks.
    processing_result = {"status": "success", "message": "Image received and 'know' function was called.", "processed_filepath": filepath}
    logger.info(f"'know' function processing complete for {filepath}. Result: {processing_result}")
    return processing_result
    #
    # --- END OF YOUR IMAGE PROCESSING LOGIC ---
    #

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
    app.run(host='0.0.0.0', port=5000, debug=True) # Set debug=False for production