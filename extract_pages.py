import os
import fitz  # PyMuPDF

def extract_page_as_image(pdf_path, page_num, output_dir, dpi=300):
    """Extract a single page from PDF as image.
    
    Args:
        pdf_path (str): Path to the PDF file
        page_num (int): Page number to extract (0-based index)
        output_dir (str): Directory to save the image
        dpi (int): Resolution of the output image
        
    Returns:
        str: Path to the saved image file, or None if an error occurs
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Open the PDF
        doc = fitz.open(pdf_path)
        
        # Get the page
        page = doc[page_num]
        
        # Render page as image
        pix = page.get_pixmap(dpi=dpi)
        
        # Save the image
        image_path = os.path.join(output_dir, f"page_{page_num + 1}.png")
        pix.save(image_path)
        
        doc.close()
        print(f"Saved page {page_num + 1} as {image_path}")
        return image_path
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    # Define paths
    pdf_path = "PrelimsProb_MT24_26Sep2024.pdf"
    output_dir = "pdf_pages"
    
    # Extract page 5 (0-based index, so we use 4)
    page_num = 4
    image_path = extract_page_as_image(pdf_path, page_num, output_dir, dpi=300) 