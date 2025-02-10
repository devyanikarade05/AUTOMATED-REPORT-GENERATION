import pandas as pd
from fpdf import FPDF

def load_data(file_path):
    return pd.read_csv(file_path)

def generate_pdf_report(df, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, "Data Report of Savitrimai Phule", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", size=12)

    for index, row in df.iterrows():
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(0, 8, f"{row['Field']}:", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 8, f"{row['Details']}")
        pdf.ln(2)

    pdf.output(output_file)

def main():
    file_path = r"C:\Users\HP\Desktop\task 2 auto report generation\savitrimai_phule.csv"
    output_pdf = "savitrimai.phule_report.pdf"
    df = load_data(file_path)
    generate_pdf_report(df, output_pdf)
    print(f"Report generated successfully: {output_pdf}")

if __name__ == "__main__":
    main()
