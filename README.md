# PDF to Text Converter for Indian Documents

## Table of Contents
- [About the Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## About the Project

**PDF to Text Converter for Indian Documents** is a Streamlit application designed to extract text and specific details from PDF documents, especially Indian identity documents like Aadhar Cards, PAN Cards, and Driving Licenses. Whether dealing with general text documents or scanned images, this tool leverages OCR (Optical Character Recognition) to provide accurate text extraction.

[Add a screenshot of your application here]

### Built With

This project is built using the following technologies:

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [pdf2image](https://github.com/Belval/pdf2image)
- [Pillow](https://python-pillow.org/)

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.7+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and added to your PATH
- pip (Python package installer)

### Installation

1. Clone the repo:
   ```sh
   git clone https://github.com/your-username/pdf-to-text-indian-documents.git
   ```
2. Change to the project directory:
   ```sh
   cd pdf-to-text-indian-documents
   ```
3. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
4. Activate the virtual environment:
   * On Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   * On MacOS/Linux:
     ```sh
     source venv/bin/activate
     ```
5. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

[Add a screenshot of the installation process here]

## Usage

1. Run the Streamlit application:
   ```sh
   streamlit run app.py
   ```
2. Open your web browser and navigate to:
   ```
   http://localhost:8501
   ```
3. Upload your PDF or image file and select the type of document and desired language.
4. If OCR is enabled, Tesseract will process the image and extract text details.

[Add a screenshot of the application usage here]

## Features

* **Multi-Language Support**: Extract text in English, Hindi, Tamil, Telugu, and Bengali.
* **Document Type Selection**: Specialized extraction for Aadhar Card, PAN Card, and Driving License.
* **OCR for Scanned Documents**: Enable OCR for accurate text extraction from images.
* **Text Output Options**: Download extracted text as a single file or per page in a ZIP archive.
* **User-Friendly Interface**: Easy-to-use Streamlit interface with sidebar options and explanations.

[Add a screenshot showing features here]

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

[Add a screenshot of contributing process here]

## License

Distributed under the MIT License. See `LICENSE` for more information.

## DEPLOYMENT

Project Link: [https://github.com/your-username/pdf-to-text-indian-documents]
(https://jyrpuzduadb3vyszaqmbmb.streamlit.app/)

## Acknowledgments

* Streamlit Community
* Tesseract OCR Contributors
* pdf2image Library
* Pillow Library
