import streamlit as st
import pdf2image
from PIL import Image
import re
from functions import convert_pdf_to_txt_pages, convert_pdf_to_txt_file, save_pages, displayPDF, images_to_txt
import os
import pytesseract

# Set Tesseract path
tesseract_path = r'"C:\Users\acer\Documents\tesseract-ocr-w64-setup-v5.0.0-alpha.20210506.exe"'  # Adjust this path as needed
if os.path.exists(tesseract_path):
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    TESSERACT_AVAILABLE = True
else:
    TESSERACT_AVAILABLE = False
    st.warning("Tesseract is not found at the specified path. OCR functionality will be limited.")
    
st.set_page_config(page_title="PDF to Text - Indian Documents")
html_temp = """
            <div style="background-color:{};padding:1px">
            
            </div>
            """

st.markdown("""
    ## Text data extractor: PDF to Text (Indian Documents)
    
""")

languages = {
    'English': 'eng',
    'Hindi': 'hin',
    'Tamil': 'tam',
    'Telugu': 'tel',
    'Bengali': 'ben',
}

def extract_aadhar_details(text):
    aadhar_pattern = r'\d{4}\s\d{4}\s\d{4}'
    name_pattern = r'(?<=नाम\s\/\sName\s:\s)([^\n]+)'
    dob_pattern = r'\d{2}/\d{2}/\d{4}'
    
    aadhar_number = re.search(aadhar_pattern, text)
    name = re.search(name_pattern, text)
    dob = re.search(dob_pattern, text)
    
    return {
        "Aadhar Number": aadhar_number.group() if aadhar_number else "Not found",
        "Name": name.group() if name else "Not found",
        "Date of Birth": dob.group() if dob else "Not found"
    }

def extract_pan_details(text):
    pan_pattern = r'[A-Z]{5}[0-9]{4}[A-Z]'
    name_pattern = r'(?<=Name\s)([^\n]+)'
    father_name_pattern = r'(?<=Father\'s Name\s)([^\n]+)'
    
    pan_number = re.search(pan_pattern, text)
    name = re.search(name_pattern, text)
    father_name = re.search(father_name_pattern, text)
    
    return {
        "PAN Number": pan_number.group() if pan_number else "Not found",
        "Name": name.group() if name else "Not found",
        "Father's Name": father_name.group() if father_name else "Not found"
    }

def extract_driving_license_details(text):
    dl_pattern = r'DL-\d{13}'
    name_pattern = r'(?<=Name:\s)([^\n]+)'
    dob_pattern = r'(?<=DOB:\s)(\d{2}/\d{2}/\d{4})'
    
    dl_number = re.search(dl_pattern, text)
    name = re.search(name_pattern, text)
    dob = re.search(dob_pattern, text)
    
    return {
        "Driving License Number": dl_number.group() if dl_number else "Not found",
        "Name": name.group() if name else "Not found",
        "Date of Birth": dob.group() if dob else "Not found"
    }

with st.sidebar:
    st.title(":outbox_tray: PDF to Text")
    document_type = st.radio(
        "Select document type",
        ('General Document', 'Aadhar Card', 'PAN Card', 'Driving License')
    )
    if document_type == 'General Document':
        textOutput = st.selectbox(
            "How do you want your output text?",
            ('One text file (.txt)', 'Text file per page (ZIP)')
        )
    ocr_box = st.checkbox('Enable OCR (scanned document)')
    
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    # How does it work?
    Simply load your PDF or image and extract text or specific details from Indian documents.
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    Made by [@vibhorjoshi]() 
    """)
    st.markdown(
        """
        <a href="https://www.buymeacoffee.com/nainiayoub" target="_blank">
        <img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174">
        </a>
        """,
        unsafe_allow_html=True,
    )

pdf_file = st.file_uploader("Load your PDF or Image", type=['pdf', 'png', 'jpg', 'jpeg'])
hide="""
<style>
footer{
	visibility: hidden;
    	position: relative;
}
.viewerBadge_container__1QSob{
  	visibility: hidden;
}
#MainMenu{
	visibility: hidden;
}
<style>
"""
st.markdown(hide, unsafe_allow_html=True)

def process_image(image, document_type):
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("Display Image"):
            st.image(image)
    
    try:
        import pytesseract
        option = st.selectbox("Select the document language", list(languages.keys()))
        text = pytesseract.image_to_string(image, lang=languages[option])
        
        with col2:
            with st.expander("Display Text"):
                st.info(text)
        
        if document_type == 'Aadhar Card':
            details = extract_aadhar_details(text)
        elif document_type == 'PAN Card':
            details = extract_pan_details(text)
        elif document_type == 'Driving License':
            details = extract_driving_license_details(text)
        else:
            details = None
        
        if details:
            st.write("Extracted Details:")
            st.write(details)
        
        st.download_button("Download txt file", text)
    except ImportError:
        st.error("Tesseract is not installed or it's not in your PATH. Please install Tesseract and add it to your PATH to use OCR functionality.")
        st.info("You can still view the image, but text extraction is not available without Tesseract.")

if pdf_file:
    file_extension = pdf_file.name.split(".")[-1].lower()
    
    if file_extension == "pdf":
        path = pdf_file.read()
        # display document
        with st.expander("Display document"):
            displayPDF(path)
        
        if document_type == 'General Document':
            if textOutput == 'One text file (.txt)':
                if ocr_box:
                    try:
                        texts, nbPages = images_to_txt(path, languages[st.selectbox('Select the document language', list(languages.keys()))])
                        totalPages = "Pages: "+str(nbPages)+" in total"
                        text_data_f = "\n\n".join(texts)
                    except ImportError:
                        st.error("Tesseract is not installed or it's not in your PATH. Please install Tesseract and add it to your PATH to use OCR functionality.")
                        st.info("Falling back to non-OCR text extraction.")
                        text_data_f, nbPages = convert_pdf_to_txt_file(pdf_file)
                        totalPages = "Pages: "+str(nbPages)+" in total"
                else:
                    text_data_f, nbPages = convert_pdf_to_txt_file(pdf_file)
                    totalPages = "Pages: "+str(nbPages)+" in total"

                st.info(totalPages)
                st.download_button("Download txt file", text_data_f)
            else:  # Text file per page (ZIP)
                if ocr_box:
                    try:
                        text_data, nbPages = images_to_txt(path, languages[st.selectbox('Select the document language', list(languages.keys()))])
                        totalPages = "Pages: "+str(nbPages)+" in total"
                    except ImportError:
                        st.error("Tesseract is not installed or it's not in your PATH. Please install Tesseract and add it to your PATH to use OCR functionality.")
                        st.info("Falling back to non-OCR text extraction.")
                        text_data, nbPages = convert_pdf_to_txt_pages(pdf_file)
                        totalPages = "Pages: "+str(nbPages)+" in total"
                else:
                    text_data, nbPages = convert_pdf_to_txt_pages(pdf_file)
                    totalPages = "Pages: "+str(nbPages)+" in total"
                st.info(totalPages)
                zipPath = save_pages(text_data)
                # download text data   
                with open(zipPath, "rb") as fp:
                    btn = st.download_button(
                        label="Download ZIP (txt)",
                        data=fp,
                        file_name="pdf_to_txt.zip",
                        mime="application/zip"
                    )
        else:  # Indian ID Documents
            try:
                import pytesseract
                option = st.selectbox('Select the document language', list(languages.keys()))
                images = pdf2image.convert_from_bytes(path)
                text = ""
                for img in images:
                    text += pytesseract.image_to_string(img, lang=languages[option]) + "\n\n"
                
                if document_type == 'Aadhar Card':
                    details = extract_aadhar_details(text)
                elif document_type == 'PAN Card':
                    details = extract_pan_details(text)
                else:  # Driving License
                    details = extract_driving_license_details(text)
                
                st.write("Extracted Details:")
                st.write(details)
                st.download_button("Download txt file", text)
            except ImportError:
                st.error("Tesseract is not installed or it's not in your PATH. Please install Tesseract and add it to your PATH to use OCR functionality.")
                st.info("You can still view the document, but text extraction is not available without Tesseract.")
    
    else:  # For image files
        image = Image.open(pdf_file)
        process_image(image, document_type)

    st.markdown('''
    <a target="_blank" style="color: black" href="https://twitter.com/intent/tweet?text=You%20can%20extract%20text%20from%20your%20PDF%20using%20this%20PDF%20to%20Text%20streamlit%20app%20by%20@nainia_ayoub!%0A%0Ahttps://nainiayoub-pdf-text-data-extractor-app-p6hy0z.streamlit.app/">
        <button class="btn">
            Spread the word!
        </button>
    </a>
    <style>
    .btn{
        display: inline-flex;
        -moz-box-align: center;
        align-items: center;
        -moz-box-pack: center;
        justify-content: center;
        font-weight: 400;
        padding: 0.25rem 0.75rem;
        border-radius: 0.25rem;
        margin: 0px;
        line-height: 1.6;
        color: rgb(49, 51, 63);
        background-color: #fff;
        width: auto;
        user-select: none;
        border: 1px solid rgba(49, 51, 63, 0.2);
        }
    .btn:hover{
        color: #00acee;
        background-color: #fff;
        border: 1px solid #00acee;
    }
    </style>
    ''',
    unsafe_allow_html=True
    )
