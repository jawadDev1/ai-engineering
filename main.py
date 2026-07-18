from langchain_core.documents import Document

from document_loaders import (
    generate_text_file,
    load_directory,
    load_document,
    load_excel,
)


def main():
    doc = Document(
        page_content="Ore no nawa Monkey D. Luffy, Kaizok ni ore wa naru",
        metadata={
            "source": "example.txt",
            "pages": 1,
            "author": "Nami",
            "date_created": "2026-01-02",
        },
    )

    # Generate dummy files
    # generate_text_file()
    # print(doc)

    # Load the document
    # document = load_document("data/text_files/python_intro.txt")

    # print(document)

    # Director loader
    # documents = load_directory("data/pdf", doc_type="pdf")
    doc = load_excel("data/excel/anime.xlsx")
    print(doc)


if __name__ == "__main__":
    main()
