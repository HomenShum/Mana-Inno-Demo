# GovAssist AI Tool

GovAssist AI Tool is designed to enhance government service websites by providing an AI-driven chatbot for citizen inquiries. The tool supports PDF upload, chat functionalities, and web scraping data to assist citizens with tasks such as renewing driver's licenses and completing baby registration action items.

## Features

- **PDF Upload and Chat**: Allows users to upload PDFs and interact with the chatbot to extract and summarize information.
- **Web Scraping**: Extracts relevant data from specified web pages to provide up-to-date information.
- **Local Data Processing**: Ensures all data is processed and stored locally within the Kingdom of Saudi Arabia, with data deletion after user sessions.
- **Language Support**: Fully supports Arabic language for all functionalities.

## Deliverables

1. A functional demo with PDF upload and chat functionalities.
2. Web scraping functionality for relevant data.
3. Framework and documentation for switching from OpenAI to a local open-source LLM for production usage.
4. Documentation on usage and backend architecture, including a high-level tutorial.

## Infrastructure

All infrastructure is built and maintained locally within the Kingdom of Saudi Arabia to comply with data storage and deletion requirements.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Streamlit
- BeautifulSoup
- Requests
- Other dependencies as listed in `requirements.txt`

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/govassist-ai-tool.git
    ```

2. Change to the project directory:
    ```sh
    cd govassist-ai-tool
    ```

3. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and navigate to the URL provided by Streamlit, typically `http://localhost:8501`.

### Usage

1. Enter the URL to extract links from in the text input box.
2. Select the URLs you want to process from the multi-select dropdown.
3. View and process the selected HTML files.

## Documentation

### Objective

The GovAssist AI Tool is designed to enhance government service websites by providing an AI-driven chatbot for citizen inquiries. It supports PDF upload, chat functionalities, and web scraping data.

### Key Features

- PDF Upload and Chat: Allows users to upload PDFs and interact with the chatbot to extract and summarize information.
- Web Scraping: Extracts relevant data from specified web pages to provide up-to-date information.
- Local Data Processing: Ensures all data is processed and stored locally within the Kingdom of Saudi Arabia, with data deletion after user sessions.
- Language Support: Fully supports Arabic language for all functionalities.

### Examples and Tutorials

#### Example 1: GovAssist AI Tool in Action
This is a video demonstration of the GovAssist AI Tool in action. The tool allows you to extract text from images, PDFs, and Excel files. It also enables users to interact with the chatbot for summarization and translation.

[Video Placeholder]

If you have any questions, feel free to reach out to us at [contact email here].

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to reach out to us at [contact email here].
