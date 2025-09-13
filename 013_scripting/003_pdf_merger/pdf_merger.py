import sys
from pathlib import Path
import PyPDF2

def pdf_merger(pdf_list, output_path=None):
    if not pdf_list:
        print("No input PDFs provided.")
        return

    # Resolve input paths and validate
    inputs = []
    for p in pdf_list:
        fp = Path(p).expanduser().resolve()
        if not fp.exists():
            print(f"Skipping (not found): {fp}")
            continue
        if fp.suffix.lower() != ".pdf":
            print(f"Skipping (not a PDF): {fp}")
            continue
        inputs.append(fp)

    if not inputs:
        print("No valid PDFs to merge.")
        return

    # Default: put merged.pdf next to the first input
    if output_path is None:
        output_path = inputs[0].parent / "merged.pdf"
    else:
        output_path = Path(output_path).expanduser().resolve()

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    merger = PyPDF2.PdfMerger()
    try:
        for pdf in inputs:
            merger.append(str(pdf))  # PyPDF2 accepts str paths
        with open(output_path, "wb") as f:
            merger.write(f)
        print(f"✔ Merged {len(inputs)} file(s) → {output_path}")
    finally:
        merger.close()

if __name__ == "__main__":
    # Usage:
    #   python merge.py in1.pdf in2.pdf in3.pdf
    # or specify output:
    #   python merge.py in1.pdf in2.pdf --out merged.pdf
    args = sys.argv[1:]
    if "--out" in args:
        idx = args.index("--out")
        out = args[idx + 1] if idx + 1 < len(args) else None
        pdfs = args[:idx]
    else:
        out = None
        pdfs = args
    pdf_merger(pdfs, out)

# python pdf_merger.py "C:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\013_scripting\003_pdf_merger\dummy.pdf" "C:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\013_scripting\003_pdf_merger\twopager.pdf" --out "C:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\013_scripting\003_pdf_merger\merged.pdf"