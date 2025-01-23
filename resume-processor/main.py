import streamlit as st
from utils.extract_text import extract_text
from utils.detect_language import detect_language
from utils.extract_data import extract_data
import pandas as pd

def main():
    st.title("Resume Processing System")
    st.write("Upload resumes in English, Spanish, French, or Dutch.")

    uploaded_files = st.file_uploader("Upload Resumes", type=["pdf", "docx"], accept_multiple_files=True)
    
    if uploaded_files:
        st.success(f"{len(uploaded_files)} files uploaded successfully!")
        
        all_data = []

        for uploaded_file in uploaded_files:
            file_type = uploaded_file.name.split(".")[-1]
            try:
                with st.spinner(f"Processing {uploaded_file.name}..."):
                    # Extract text
                    text = extract_text(uploaded_file, file_type)
                    
                    # Detect language
                    language = detect_language(text)
                    language_map = {"en": "English", "es": "Spanish", "fr": "French", "nl": "Dutch"}
                    language_name = language_map.get(language, "Unknown")
                    
                    # Extract data
                    extracted_data = extract_data(text)
                    extracted_data["language"] = language_name
                    extracted_data["file_name"] = uploaded_file.name
                    all_data.append(extracted_data)
                    
                    # Display extracted text and language
                    st.text_area(f"Extracted Text from {uploaded_file.name}", text, height=300)
                    st.write(f"**Detected Language**: {language_name}")
                    
            except Exception as e:
                st.error(f"Error processing {uploaded_file.name}: {str(e)}")
        
        if all_data:
            st.write("### Extracted Data")
            # Create a DataFrame from the extracted data
            df = pd.DataFrame(all_data)
            # Drop 'file_name' column before displaying
            df = df.drop(columns=["file_name"])
            
            # Use st.dataframe to show the table with proper styling
            st.dataframe(df.style.set_table_styles(
                [{'selector': 'thead th', 'props': [('background-color', '#f0f0f0'), ('color', 'black')]},  # Header styling
                 {'selector': 'tbody td', 'props': [('background-color', '#ffffff'), ('color', 'black')]},   # Data row styling
                 {'selector': 'table', 'props': [('border-collapse', 'collapse'), ('width', '100%')]}  # Table width and border styling
                ]))

            # Download button for CSV
            st.write("### Download Extracted Data")
            st.download_button(
                label="Download CSV",
                data=create_csv(all_data),
                file_name="extracted_data.csv",
                mime="text/csv",
            )

def create_csv(data):
    """Convert extracted data into a CSV format."""
    import pandas as pd
    df = pd.DataFrame(data)
    return df.to_csv(index=False).encode("utf-8")

if __name__ == "__main__":
    main()
