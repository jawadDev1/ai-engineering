import os

from langchain_community.document_loaders import (
    DirectoryLoader,
    PyMuPDFLoader,
    PyPDFLoader,
    TextLoader,
)
from langchain_core.documents import Document
from langchain_excel_loader import StructuredExcelLoader


def generate_text_file():
    os.makedirs("data/text_files", exist_ok=True)

    sample_texts = {
        "data/text_files/python_intro.txt": """
        Python is a high-level, interpreted programming language that has become one of the most popular languages in the world. Created by Guido van Rossum and first released in 1991, it was designed with a core philosophy centered on code readability and simplicity. Its syntax closely resembles standard English, which allows developers to write clear, logical code for both small and large-scale projects. By reducing the complexity of the code structure, Python enables programmers to focus on solving problems rather than wrestling with intricate language rules.

        One of Python’s greatest strengths is its incredible versatility. It serves as a general-purpose language, meaning it can be used to build almost anything. Developers rely on Python for web development, software creation, system scripting, and automating repetitive tasks. Because it is an interpreted language, code is executed line by line, which makes debugging much faster and allows for rapid prototyping. This adaptability makes it a go-to choice across a vast array of industries, from finance to entertainment.

        In recent years, Python has established itself as the undisputed leader in data science, machine learning, and artificial intelligence. Its extensive ecosystem includes powerful, specialized libraries like NumPy and Pandas for data manipulation, and TensorFlow and PyTorch for building complex neural networks. Researchers and data analysts favor Python because it simplifies the process of cleaning data, calculating complex mathematical formulas, and training predictive algorithms, turning massive datasets into actionable insights.

        Beyond enterprise and scientific applications, Python is widely considered the ideal entry point for beginners learning how to code. Traditional programming languages often require pages of boilerplate code—reusable setup code—just to display text on a screen. In contrast, Python can achieve the same result in a single, intuitive line. This low barrier to entry builds immediate confidence in new programmers, letting them grasp fundamental concepts like loops and variables without getting discouraged by dense, unforgiving syntax.

        Supporting all of this is a massive, global community of developers who continuously contribute to Python's growth. This open-source community maintains an expansive repository of third-party modules that can be easily installed to add new capabilities to any project. Whether a developer is stuck on a logic bug or trying to implement a rare feature, a wealth of documentation, forums, and tutorials is readily available. This robust network ensures that Python remains modern, secure, and continuously adapted to meet the demands of tomorrow's technology.
        """,
        "data/text_files/machine_learning.txt": """
        Machine learning is a subset of artificial intelligence that empowers computers to learn from data and improve their performance over time without being explicitly programmed. Instead of relying on rigid, pre-written rules to perform a task, machine learning algorithms analyze massive datasets to identify underlying patterns and make autonomous decisions. This paradigm shift transforms computers from passive execution tools into adaptive systems capable of processing complex, real-world information much like a human would.

        At the core of this technology are three primary types of learning methods: supervised, unsupervised, and reinforcement learning. Supervised learning uses labeled datasets to teach algorithms how to classify data or predict outcomes, similar to a student learning from a teacher’s answer key. Unsupervised learning, by contrast, analyzes unlabeled data to uncover hidden structures or groupings on its own. Reinforcement learning takes a behavioral approach, training an algorithm through trial and error using a system of rewards and penalties to achieve an optimal goal.

        The practical applications of machine learning have quietly woven themselves into the fabric of daily life. E-commerce platforms and streaming services use recommendation engines to predict what products or shows a user might enjoy next based on past behavior. Spam filters automatically shield email inboxes by recognizing the shifting patterns of junk mail, while financial institutions rely on anomalies in transaction data to detect and halt credit card fraud in real time.

        Beyond consumer conveniences, machine learning is driving breakthroughs in complex fields like healthcare and autonomous transportation. In medicine, algorithms trained on millions of medical images can detect anomalies such as tumors with an accuracy that rivals or exceeds human specialists, allowing for earlier intervention. Meanwhile, self-driving cars utilize machine learning to process simultaneous data streams from cameras and radar, enabling the vehicle to recognize pedestrians, interpret traffic signs, and make split-second navigational choices.

        As machine learning continues to advance, it brings both immense potential and significant ethical responsibilities. Because these models learn strictly from historical data, they can inadvertently absorb and amplify human biases present within that data, leading to unfair or discriminatory outcomes. Ensuring algorithmic fairness, protecting data privacy, and making complex models more transparent—a concept known as explainable AI—are critical challenges that developers and policymakers must solve as the technology shapes the future.
        """,
    }

    for filepath, content in sample_texts.items():
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    print("Sample text file created")


def load_document(path):
    loader = TextLoader(path, encoding="utf-8")
    return loader.load()


def load_directory(path, doc_type="txt"):

    if doc_type == "pdf":
        dir_loader = DirectoryLoader(
            path,
            glob="**/*.pdf",  # pattern to match the files
            loader_cls=PyMuPDFLoader,  # Loader class to use like pdf loader, csv loader etc
            show_progress=False,
        )

        return dir_loader.load()

    else:
        dir_loader = DirectoryLoader(
            path,
            glob="**/*.txt",  # pattern to match the files
            loader_cls=TextLoader,  # Loader class to use like pdf loader, csv loader etc
            loader_kwargs={"encoding": "utf-8"},
            show_progress=False,
        )

        return dir_loader.load()


def load_excel(path):
    loader = StructuredExcelLoader(path)
    return loader.load()
