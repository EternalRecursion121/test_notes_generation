import os
import httpx
import base64
import google.generativeai as genai
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from io import BytesIO

def get_chapter_pages(chapter_num):
    """Get the start and end pages for a given chapter number.
    
    Args:
        chapter_num (int): Chapter number
        
    Returns:
        tuple: (start_page, end_page) or None if chapter doesn't exist
    """
    chapter_ranges = {
        1: (4, 15),
        2: (16, 27),
        3: (28, 36),
        4: (37, 46),
        5: (47, 63),
        6: (64, 66),
        7: (67, 71)  # Appendix
    }
    return chapter_ranges.get(chapter_num)

def extract_chapter_pdf(pdf_content, chapter_num):
    """Extract specific pages for a chapter from the PDF content.
    
    Args:
        pdf_content (bytes): Raw PDF content
        chapter_num (int): Chapter number to extract
        
    Returns:
        bytes: PDF content for the specific chapter
    """
    page_range = get_chapter_pages(chapter_num)
    if not page_range:
        raise ValueError(f"Invalid chapter number: {chapter_num}")
        
    start_page, end_page = page_range
    
    # Convert to 0-based indexing
    start_idx = start_page - 1
    end_idx = end_page - 1
    
    # Create PDF reader object
    pdf = PdfReader(BytesIO(pdf_content))
    
    # Create a new PDF writer
    from PyPDF2 import PdfWriter
    pdf_writer = PdfWriter()
    
    # Add the specified pages
    for page_num in range(start_idx, end_idx + 1):
        pdf_writer.add_page(pdf.pages[page_num])
    
    # Save to bytes
    output = BytesIO()
    pdf_writer.write(output)
    return output.getvalue()

def create_notes_prompt(chapter_num):
    """Create prompt for generating comprehensive revision notes."""
    chapter_name = "Appendix" if chapter_num == 7 else f"Chapter {chapter_num}"
    return fr"""
    Please analyze {chapter_name} of this PDF and create comprehensive revision notes that:
    - Follow the natural flow of concepts but maintain complete mathematical rigor
    - Include ALL essential mathematical content with clear visual separation:
       * Key definitions in boxes (using markdown > for boxes)
       * ALL theorems with their complete statements
       * ALL lemmas and properties
       * Complete, step-by-step proofs with explanations
       * ALL corollaries and their implications
       * Important remarks and observations
    - Use proper markdown LaTeX syntax:
       * Inline math with $...$ (e.g., $\Omega$ for sample space)
       * Displayed equations with $$....$$
       * Proper spacing in equations
       * Numbered equations using $$\begin{{equation}}...\end{{equation}}$$
    - Structure with clear markdown headers and subheaders
    - Use bullet points and numbered lists for better readability
    - Add horizontal rules (---) between major sections
    - Include brief intuitive explanations where helpful
    - Use blockquotes (>) for important remarks or insights
    """

def create_quick_reference_prompt(chapter_num):
    """Create prompt for generating quick reference."""
    chapter_name = "Appendix" if chapter_num == 7 else f"Chapter {chapter_num}"
    return fr"""
    Please analyze {chapter_name} of this PDF and create a Quick Reference section containing:
    
    ## Quick Reference
    - Complete list of ALL formulas and results
    - ALL definitions in mathematical notation
    - ALL theorems (concisely stated)
    - ALL key relationships and implications
    - Important special cases
    - Key conditions and assumptions

    ## Common Patterns and Techniques
    - Key proof techniques used in the chapter
    - Common problem-solving strategies
    - Important connections between concepts
    - Typical applications of theorems

    Ensure all mathematical notation uses proper LaTeX syntax with $...$ for inline math and $$...$$ for displayed equations.
    """

def create_flashcards_prompt(chapter_num):
    """Create prompt for generating flashcards."""
    chapter_name = "Appendix" if chapter_num == 7 else f"Chapter {chapter_num}"
    return fr"""
    Please analyze {chapter_name} of this PDF and create flashcards following these rules:
    - Each card should test one simple concept (minimum information principle)
    - Use clear, unambiguous wording
    - Include context where necessary
    - Build upon basic concepts first
    - Use proper LaTeX formatting for all mathematical content
    - Avoid sets and long enumerations
    - Include source references where relevant
    - Use both basic and cloze deletion cards

    Format the flashcards in this structure:

    ## Flashcards

    ### Basic Cards
    START
    Basic
    What is $\mathbb{{P}}(A \cup B)$ when A and B are disjoint?
    Back: When A and B are disjoint, $\mathbb{{P}}(A \cup B) = \mathbb{{P}}(A) + \mathbb{{P}}(B)$
    Tags: chapter{chapter_num}, probability, addition_rule
    END

    ### Cloze Cards
    START
    Cloze
    For any events A and B, $\mathbb{{P}}(A \cup B) = {{{{c1::$\mathbb{{P}}(A) + \mathbb{{P}}(B) - \mathbb{{P}}(A \cap B)$}}}}$
    Tags: chapter{chapter_num}, probability, addition_rule
    END
    """

def process_pdf_with_gemini(pdf_path, output_dir, chapter_num, content_type='notes'):
    """Process PDF from local file with Gemini for specific content type.
    
    Args:
        pdf_path (str): Path to the local PDF file
        output_dir (str): Directory to save the markdown output
        chapter_num (int): Chapter number to process
        content_type (str): Type of content to generate ('notes', 'quick_reference', or 'flashcards')
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        load_dotenv()
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("Please set GEMINI_API_KEY in .env file")
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        generation_config = genai.GenerationConfig(
            max_output_tokens=7000,
        )
        model.generation_config = generation_config
        
        with open(pdf_path, 'rb') as file:
            pdf_content = file.read()
        chapter_content = extract_chapter_pdf(pdf_content, chapter_num)
        doc_data = base64.standard_b64encode(chapter_content).decode("utf-8")
        
        # Select prompt based on content type
        if content_type == 'notes':
            prompt = create_notes_prompt(chapter_num)
            suffix = 'revision_notes'
        elif content_type == 'quick_reference':
            prompt = create_quick_reference_prompt(chapter_num)
            suffix = 'quick_reference'
        else:  # flashcards
            prompt = create_flashcards_prompt(chapter_num)
            suffix = 'flashcards'
        
        response = model.generate_content([
            {'mime_type': 'application/pdf', 'data': doc_data},
            prompt,
        ])
        
        prefix = "appendix" if chapter_num == 7 else f"chapter{chapter_num}"
        filename = f"{prefix}_{suffix}.md"
        output_path = os.path.join(output_dir, filename)
        
        chapter_name = "Appendix" if chapter_num == 7 else f"Chapter {chapter_num}"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"# {chapter_name} {suffix.replace('_', ' ').title()}\n\n")
            f.write(response.text)
            
        print(f"{suffix.replace('_', ' ').title()} saved to {output_path}")
        
    except Exception as e:
        print(f"An error occurred with Gemini processing: {str(e)}")

def process_chapter_content(pdf_path, output_dir, chapter_num):
    """Process all content types for a specific chapter."""
    for content_type in ['notes', 'quick_reference', 'flashcards']:
        print(f"\nGenerating {content_type} for Chapter {chapter_num}...")
        process_pdf_with_gemini(pdf_path, output_dir, chapter_num, content_type)

if __name__ == "__main__":
    # Define paths
    pdf_path = "PrelimsProb_MT24_26Sep2024.pdf"
    notes_dir = "markdown_notes"
    
    # Process a single chapter with all content types
    for chapter_num in range(2, 8):
        process_chapter_content(pdf_path, notes_dir, chapter_num)
