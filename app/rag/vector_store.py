from pathlib import Path

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


# --------------------------------------------------
# Project paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

HEALTH_GUIDE = PROJECT_ROOT / "assets" / "health_guide.txt"
MEDICAL_BOOKS = PROJECT_ROOT / "assets" / "medical_books"


# --------------------------------------------------
# Load health guide
# --------------------------------------------------

def load_health_guide():
    """Load the existing health guide text file."""

    documents = []

    if HEALTH_GUIDE.exists():

        with open(HEALTH_GUIDE, "r", encoding="utf-8") as file:
            data = file.read()

        documents.append(
            Document(
                page_content=data,
                metadata={
                    "source": str(HEALTH_GUIDE),
                    "type": "health_guide",
                },
            )
        )

    return documents


# --------------------------------------------------
# Load medical PDF files
# --------------------------------------------------

def load_medical_books():
    """Load all PDF files from assets/medical_books."""

    documents = []

    if not MEDICAL_BOOKS.exists():
        return documents

    pdf_files = list(MEDICAL_BOOKS.glob("*.pdf"))

    print(f"Found {len(pdf_files)} medical PDF(s).")

    for pdf_file in pdf_files:

        print(f"Loading PDF: {pdf_file.name}")

        try:
            loader = PyPDFLoader(str(pdf_file))

            pdf_documents = loader.load()

            for document in pdf_documents:
                document.metadata["source"] = pdf_file.name
                document.metadata["type"] = "medical_book"

            documents.extend(pdf_documents)

            print(
                f"Loaded {len(pdf_documents)} pages "
                f"from {pdf_file.name}"
            )

        except Exception as e:

            print(
                f"Could not load {pdf_file.name}: {e}"
            )

    return documents


# --------------------------------------------------
# Create vector store
# --------------------------------------------------

def create_vector_store():
    """Create a FAISS vector store from health guide and PDFs."""

    print("Loading medical knowledge...")

    # Load health guide
    health_docs = load_health_guide()

    # Load medical PDFs
    medical_docs = load_medical_books()

    # Combine everything
    raw_docs = health_docs + medical_docs

    print(f"Total documents/pages loaded: {len(raw_docs)}")

    if not raw_docs:
        raw_docs = [
            Document(
                page_content="No medical knowledge was found.",
                metadata={"source": "missing"},
            )
        ]

    # --------------------------------------------------
    # Split documents into smaller chunks
    # --------------------------------------------------

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            "",
        ],
    )

    split_docs = text_splitter.split_documents(raw_docs)

    print(f"Created {len(split_docs)} text chunks.")

    # --------------------------------------------------
    # Create embeddings
    # --------------------------------------------------

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # --------------------------------------------------
    # Create FAISS vector database
    # --------------------------------------------------

    vector_store = FAISS.from_documents(
        split_docs,
        embeddings,
    )

    print("FAISS vector store created successfully.")

    return vector_store.as_retriever(
        search_kwargs={"k": 4}
    )
