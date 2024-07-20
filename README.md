# PDF to Text Converter for Indian Documents

This Streamlit application allows users to extract text from PDF files and images, with special features for Indian identity documents like Aadhar Card, PAN Card, and Driving License.

## Features

1. **PDF to Text Conversion**: Convert PDF files to text format.
2. **OCR Capability**: Extract text from scanned documents and images using Optical Character Recognition (OCR).
3. **Multiple Output Options**: 
   - Generate a single text file for the entire PDF.
   - Create individual text files for each page (provided as a ZIP file).
4. **Indian Document Processing**:
   - Extract specific details from Aadhar Card, PAN Card, and Driving License.
5. **Multi-language Support**: Process documents in various Indian languages including English, Hindi, Tamil, Telugu, and Bengali.
6. **User-friendly Interface**: Easy-to-use Streamlit interface for uploading and processing documents.

## Requirements

- Python 3.7+
- Streamlit
- pdf2image
- Pillow
- pytesseract
- Tesseract OCR engine (must be installed separately)

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/pdf-to-text-indian-documents.git
   cd pdf-to-text-indian-documents
   ```

2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR engine:
   - For Windows: Download and install from [here](https://github.com/UB-Mannheim/tesseract/wiki)
   - For macOS: `brew install tesseract`
   - For Linux: `sudo apt-get install tesseract-ocr`

4. Ensure Tesseract is in your system PATH or update the `tesseract_path` variable in the script.

## Usage

Run the Streamlit app with the following command:

```sh
streamlit run app.py
```

Then, open your web browser and go to `http://localhost:8501` to use the application.

## Deployment

This app can be deployed on Streamlit Sharing for free. Visit [Streamlit Sharing](https://streamlit.io/sharing) for more information on how to deploy your Streamlit app.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/pdf-to-text-indian-documents/issues).

## License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

## Screenshots

[]

## Contact

Your Name - [@your_twitter](https://twitter.com/your_twitter) - email@example.com

Project Link: [https://github.com/yourusername/pdf-to-text-indian-documents](https://github.com/yourusername/pdf-to-text-indian-documents)
