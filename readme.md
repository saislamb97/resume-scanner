```markdown
# Resume Scanner

This project is a Resume Scanner that extracts information from resumes in PDF, DOC, or DOCX formats. It uses the `transformers` library for Named Entity Recognition (NER) to identify and extract key details from resumes.

## Features

- Extract text from PDF, DOC, and DOCX files.
- Identify and extract names, emails, phone numbers, skills, experience, education, training, and languages.
- Generate a summary of the resume with the extracted information.

## Requirements

- Python 3.x
- fitz (PyMuPDF)
- docx
- transformers
- docx2pdf
- pdf2docx

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/resume-scanner.git
   cd resume-scanner
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Place your resume file in the project directory. Supported formats are PDF, DOC, and DOCX.

2. Update the `file_path` variable in `main.py` with the path to your resume file.

3. Run the script:
   ```sh
   python main.py
   ```

4. The script will extract information from the resume and print a summary.

## Project Structure

```
resume-scanner/
├── main.py            # Main script to run the resume scanner
├── requirements.txt   # List of dependencies
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Creating the `requirements.txt` File

To generate a `requirements.txt` file with the necessary dependencies, you can run:

```sh
pip freeze > requirements.txt
```

Make sure to include all required packages in your environment before running the above command.

### Final Steps

1. Create the `.gitignore` and `README.md` files in your project directory.
2. Run `pip freeze > requirements.txt` to generate the `requirements.txt` file.
3. Commit these files to your repository.

Now, your project is ready to be shared, and others can easily set up and use your Resume Scanner.