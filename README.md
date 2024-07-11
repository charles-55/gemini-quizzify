# Gemini Explorer

## Overview
The Gemini Explorer project is an interactive AI chat system called Horatio, built using Streamlit and Google's Gemini AI. Horatio was designed to sound like William Shakespeare and to be more friendly by interacting using the user's name.

The project's goal is to demo the use of large language models (LLMs) in a customized environment.

## Key Features
The key features of the Gemini Explorer project are listed below:

- An interactive AI chat system, Horatio, that uses Streamlit and Google's Gemini AI.

- A personalized AI, designed to sound like William Shakespeare and to be more friendly by interacting using the user's provided name.

- Horatio is able to respond to a variety of basic and complex questions.

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
- A [google cloud project](https://console.cloud.google.com/) called **gemini-explorer**.

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
