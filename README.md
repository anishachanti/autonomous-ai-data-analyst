# autonomous-ai-data-analyst

Autonomous AI Data Analyst is an AI-powered analytics platform that allows users to upload datasets, ask questions in natural language, generate SQL queries automatically, perform forecasting, and visualize results through charts.

The system combines Large Language Models (LLMs), DuckDB, FastAPI, React, and Model Context Protocol (MCP) to provide an intelligent data analysis experience.

### **MCP (Model Context Protocol) Integration**

The project uses MCP to expose analytics capabilities as tools.

Available MCP tools:

health_check
query_dataset
forecast_dataset
create_chart

This enables agent-based orchestration and tool execution through a standardized protocol.


Architecture
React Frontend
       │
       ▼
FastAPI Backend
       │
       ▼
SQL Agent
       │
       ▼
MCP Client
       │
       ▼
MCP Server
       │
 ┌─────┼──────────────┬
 ▼     ▼              ▼
Query  Forecast       Chart
Tool   Tool           Tool
       │
       ▼
Services Layer
       │
       ▼
DuckDB + LLM



**Technology Stack**


#### Frontend

* React
* Axios
* Recharts

#### Backend
* FastAPI
* Python

#### AI & Analytics
* Groq LLM
* DuckDB
* Pandas
* Scikit-Learn

#### Agent Framework
* MCP (Model Context Protocol)