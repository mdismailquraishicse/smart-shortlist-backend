# Resume Ranking Application

An AI-powered Resume Ranking System that allows users to upload multiple resumes and a Job Description (JD), automatically parses the documents, generates embeddings, stores them in Qdrant, and ranks resumes based on their relevance to the given JD.

## Features

* Upload multiple resumes
* Upload a Job Description (JD)
* Automatic document parsing
* Embedding generation
* Vector storage using Qdrant
* AI-powered resume ranking
* Dockerized deployment

---

# Prerequisites

Before running the application, make sure the following software is installed:

### 1. Docker

Verify installation:

```bash
docker --version
```

Install Docker:

* Ubuntu: https://docs.docker.com/engine/install/ubuntu/
* Windows: https://docs.docker.com/desktop/install/windows-install/
* Mac: https://docs.docker.com/desktop/install/mac-install/

---

### 2. Docker Compose

Verify installation:

```bash
docker compose version
```

Docker Compose is included in modern Docker Desktop installations.

---

### 3. Hugging Face Account

You need a Hugging Face account to generate and use the API token required by this application.

Create an account:

https://huggingface.co/join

---

# Environment Variables

Create a `.env` file in the project root directory.

Example:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

**Important:** The application will not start without this environment variable.

---

# How to Get Hugging Face API Token

### Step 1

Visit:

https://huggingface.co

### Step 2

Login to your account.

### Step 3

Click your profile picture in the top-right corner.

### Step 4

Navigate to:

Settings → Access Tokens

Direct URL:

https://huggingface.co/settings/tokens

### Step 5

Click **"Create new token"**

### Step 6

Provide:

* Token Name
* Permission: Read

### Step 7

Click **Create Token**

### Step 8

Copy the generated token.

### Step 9

Paste the token into your `.env` file:

```env
HUGGINGFACEHUB_API_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxx
```

---

# Project Setup

Clone the repository:

```bash
git clone https://github.com/mdismailquraishicse/smart-shortlist-backend.git
```

Move into the project directory:

```bash
cd smart-shortlist-backend
```

Create the `.env` file:

```bash
touch .env
```

Add:

```env
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

---

# Running the Application

Build and start all services:

```bash
docker compose up --build
```

The first build may take several minutes depending on your internet speed.

---

# Stopping the Application

Press:

```text
CTRL + C
```

Or run:

```bash
docker compose down
```

---

# Rebuilding After Code Changes

If dependencies or Docker configurations have changed:

```bash
docker compose up --build
```

To completely rebuild:

```bash
docker compose down
docker compose build --no-cache
docker compose up
```

---

# Data Persistence

The application stores:

* Uploaded resumes
* Uploaded JDs
* Qdrant vector database data

Ensure that Docker volumes are not removed if you want to retain previously indexed documents.

---

# Troubleshooting

### Missing Hugging Face Token

Error:

```text
HUGGINGFACEHUB_API_TOKEN not found
```

Solution:

Verify that `.env` exists and contains:

```env
HUGGINGFACEHUB_API_TOKEN=<your_token>
```

---

### Docker Not Found

Error:

```text
docker: command not found
```

Solution:

Install Docker and verify using:

```bash
docker --version
```

---

### Docker Compose Not Found

Error:

```text
docker compose: command not found
```

Solution:

Install Docker Compose or update Docker Desktop.

---

# Application Startup Command

```bash
docker compose up --build
```

Once the containers are running successfully, the Resume Ranking Application will be ready to accept resume and JD uploads.
