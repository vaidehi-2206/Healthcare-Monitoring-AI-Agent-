from pathlib import Path

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter


# Find the project root folder
PROJECT_ROOT = Path(__file__).resolve().parents[2]
HEALTH_GUIDE = PROJECT_ROOT / "assets" / "health_guide.txt"


def load_health_guide():
    """Reads the health guide text file."""

    if not HEALTH_GUIDE.exists():
        return [
            Document(
                page_content="Health guide not found.",
                metadata={"source": "missing"},
            )
        ]

    with open(HEALTH_GUIDE, "r", encoding="utf-8") as file:
        data = file.read()

    return [
        Document(
            page_content=data,
            metadata={"source": str(HEALTH_GUIDE)},
        )
    ]


def create_vector_store():
    """Creates the FAISS vector store."""

    raw_docs = load_health_guide()

    text_splitter = CharacterTextSplitter(
        separator="###",
        chunk_size=500,
        chunk_overlap=50,
    )

    split_docs = text_splitter.split_documents(raw_docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(
        split_docs,
        embeddings,
    )

    return vector_store.as_retriever(search_kwargs={"k": 2})
