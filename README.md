# Gemini Explorer

## Overview
Rapid advancements in machine learning have led to the development of sophisticated large language models, such as Google's Gemini. However, the complexity of these models can make them quite inaccessible to many users who lack technical backgrounds. There is a need for an intuitive and user-friendly platform that allows users to interact with and explore the capabilities of these advanced language models.

The primary goal of this project is to develop a chat interface using Streamlit that integrates with Google's Gemini large language model. This interface aims to provide an accessible and interactive platform for users to experience and explore the capabilities of advanced language models. By creating this application, we aim to offer an educational and practical introduction to the fusion of large language models and user-friendly interfaces, making cutting-edge AI technology more approachable to a broader audience.

## Key Features
The key features of the Gemini Explorer project are listed below:

- Streamlit ensures the chat interface is simple, interactive, and easy to use, even for those with minimal technical knowledge.

- Google's Gemini powerful large language model is leveraged to generate sophisticated and contextually appropriate responses.

- A record of the chat is kept within the session, allowing users to refer back to previous messages and ensuring context is preserved.

- The model's behavior can be fine-tuned through configuration settings such as temperature, enhancing the quality and relevance of responses.

- The model introduces itself with a unique personality, using emojis and Shakespearean language to create a memorable and engaging interaction.

## Set Up
To set up the Gemini Explorer project, follow these steps:
1. [Prerequisites](#1-prerequisites)
2. [Clone the Repository](#2-clone-the-repository)
3. [Set Up Virtual Environment](#3-set-up-a-virtual-environment-optional-but-recommended)
4. [Install Dependencies](#4-install-dependencies)
5. [Configure the Project](#5-configure-the-project)
6. [Start The Server](#6-start-the-server)
7. [Access the Server](#7-access-the-server)

### 1. Prerequisites
Before you begin, ensure you have the following installed on your system:
- Python 3.8 or higher
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install-sdk)
- A [google cloud project](https://console.cloud.google.com/) called **gemini-explorer** with all recommended APIs enabled.

### 2. Clone the Repository
To clone the repository, run the following command in your terminal replacing the **your-username** and **your-repository** variables:
```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 3. Set Up a Virtual Environment (Optional but recommended)
It's a good practice to create a virtual environment for your Python projects. This keeps your project dependencies isolated. If you have `virtualenv` installed, create a new environment with:

```bash
virtualenv venv
source venv/bin/activate
```

### 4. Install Dependencies
Install all necessary dependencies by running:
```bash
pip install google-cloud-aiplatform streamlit
```

### 5. Configure the Project
Before starting the server, configure the project by editing **line 6** on the [gemini_explorer.py](gemini_explorer.py) file to your actual project ID.

### 6. Start the Server
After the installation, you can start the server using Streamlit. Navigate to the project directory and run:
```bash
streamlit run gemini_explorer.py
```

### 7. Access the Server
With the server running, you can access the Server at the URL provided in your terminal which should  default to `http://127.0.0.1:8501`.
