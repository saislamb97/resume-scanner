import fitz  # PyMuPDF
import docx
from transformers import pipeline
import re
import os
from docx2pdf import convert
from pdf2docx import parse

# Load the pre-trained NER model
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", tokenizer="dslim/bert-base-NER")

def convert_to_pdf(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension in ['.doc', '.docx']:
        # Convert DOC or DOCX to PDF
        convert(file_path, file_path.replace(file_extension, '.pdf'))
        return file_path.replace(file_extension, '.pdf')
    elif file_extension == '.pdf':
        return file_path
    else:
        raise ValueError("Unsupported file format")

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    full_text = []
    for page in doc:
        full_text.append(page.get_text())
    return '\n'.join(full_text)

def extract_information(text):
    # Use NER model to extract entities
    ner_results = ner_pipeline(text)

    # Debug: Print NER results
    print("NER Results:", ner_results)

    # Organize extracted information
    extracted_info = {
        "names": set(),
        "emails": set(),
        "phones": set(),
        "skills": set(),
        "experience": [],
        "education": [],
        "training": [],
        "languages": []
    }
    
    for entity in ner_results:
        if entity['entity'] == 'B-PER' or entity['entity'] == 'I-PER':
            extracted_info["names"].add(entity['word'])
        elif entity['entity'] == 'B-ORG' or entity['entity'] == 'I-ORG':
            extracted_info["skills"].add(entity['word'])
    
    # Extract emails using regex
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    extracted_info["emails"].update(emails)

    # Extract phone numbers using regex
    phones = re.findall(r'\+?\d[\d -]{8,}\d', text)
    extracted_info["phones"].update(phones)

    # Extract sections from the resume
    experience_section = re.findall(r'Experience\s+(.*?)(?=Technical Skills|Education|Training|Language|$)', text, re.DOTALL)
    if experience_section:
        extracted_info["experience"] = experience_section[0].strip().split('\n')

    education_section = re.findall(r'Education\s+(.*?)(?=Technical Skills|Experience|Training|Language|$)', text, re.DOTALL)
    if education_section:
        extracted_info["education"] = education_section[0].strip().split('\n')

    training_section = re.findall(r'Training\s+(.*?)(?=Technical Skills|Experience|Education|Language|$)', text, re.DOTALL)
    if training_section:
        extracted_info["training"] = training_section[0].strip().split('\n')

    languages_section = re.findall(r'Language\s+(.*?)(?=Technical Skills|Experience|Education|Training|$)', text, re.DOTALL)
    if languages_section:
        extracted_info["languages"] = languages_section[0].strip().split('\n')
    
    return extracted_info

def generate_resume(extracted_info):
    resume = ""
    resume += f"Names: {', '.join(extracted_info['names'])}\n"
    resume += f"Emails: {', '.join(extracted_info['emails'])}\n"
    resume += f"Phone Numbers: {', '.join(extracted_info['phones'])}\n"
    resume += f"Skills: {', '.join(extracted_info['skills'])}\n"
    resume += "Experience:\n" + '\n'.join(extracted_info['experience']) + "\n"
    resume += "Education:\n" + '\n'.join(extracted_info['education']) + "\n"
    resume += "Training:\n" + '\n'.join(extracted_info['training']) + "\n"
    resume += "Languages:\n" + '\n'.join(extracted_info['languages']) + "\n"
    return resume

def main(file_path):
    pdf_file_path = convert_to_pdf(file_path)
    text = extract_text_from_pdf(pdf_file_path)
    
    # Debug: Print extracted text
    print("Extracted Text:", text)
    
    extracted_info = extract_information(text)
    resume = generate_resume(extracted_info)

    # Print generated resume
    print("Generated Resume:")
    print(resume)

if __name__ == "__main__":
    file_path = r"resume.docx"  # Replace with the actual file path
    main(file_path)
