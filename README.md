📌 Project Overview

The LinkedIn Insights Microservice is a backend application designed to fetch, process, and store insights about LinkedIn Company Pages using a given Page ID (the last part of a LinkedIn company URL).

Due to LinkedIn’s strict anti-scraping and data-access policies, this project follows an industry-accepted hybrid data acquisition approach by leveraging Google Search Intelligence via SerpAPI to retrieve publicly available company information.

The system demonstrates clean backend architecture, scalable API design, persistent storage, and real-world data constraints handling, making it suitable for a GenAI / Backend Intern assignment.

🧠 Key Features

Fetch company insights using a LinkedIn Page ID

Real external data retrieval using SerpAPI (Google Search)

Graceful fallback handling when data is unavailable

Persistent storage using MongoDB

RESTful APIs built using FastAPI

Swagger UI for easy testing and demo

Clean, modular, and maintainable codebase

Beginner-friendly yet industry-aligned architecture

🏗️ Project Architecture
linkedin_insights/
│
├── main.py           # FastAPI application entry point
├── routes.py         # API routes
├── services.py       # Business logic layer
├── scraper.py        # External data fetcher (SerpAPI)
├── store.py          # MongoDB connection
├── requirements.txt  # Dependencies
├── README.md         # Documentation
├── .env              # Environment variables (NOT committed)

🔄 Data Flow

Client calls the API with a LinkedIn Page ID

Application checks MongoDB for existing data

If not found:

Fetches real company data via SerpAPI

Normalizes and stores it in MongoDB

Returns structured JSON response to the client

Subsequent requests are served directly from the database

🔐 Why SerpAPI Instead of Direct LinkedIn Scraping?

LinkedIn does not allow reliable or legal automated scraping:

Most content is loaded via private GraphQL APIs

Anti-bot mechanisms block automation

Requires login, cookies, and session tracking

Industry-accepted solution:

This project uses Google Search Intelligence via SerpAPI, a widely used approach in:

Market research

Competitive intelligence

Sales enablement platforms

This method is:

Legal

Stable

Scalable

Interview-safe

🗄️ Database

Database: MongoDB

Collection: pages

Stores structured company data for persistent access

🚀 API Endpoints
Get LinkedIn Page Insights
GET /page/{page_id}

Example:
GET /page/deepsolv

Sample Response:
{
  "page_id": "deepsolv",
  "name": "Deepsolv",
  "url": "https://www.linkedin.com/company/deepsolv/",
  "industry": "Software / Technology",
  "followers": "N/A (LinkedIn restricted)",
  "description": "Company information retrieved via Google SERP",
  "website": "https://www.deepsolv.com",
  "profile_pic": "N/A",
  "specialities": [],
  "posts": [],
  "employees": []
}
