# CINEIQ 🎬 — Version 2.0

<div align="center">

![CineIQ Banner](https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1200&auto=format&fit=crop&q=80)

### **Next-Generation AI-Powered Movie Recommendation & Social Discovery Platform**

[![ECSoC26](https://img.shields.io/badge/Event-ECSoC26-6f42c1?style=for-the-badge&logo=github)](https://github.com/apps/ecsoc-sentinel)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Next.js 15](https://img.shields.io/badge/Next.js-15.5-black.svg?style=for-the-badge&logo=next.js&logoColor=white)](https://nextjs.org)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6.svg?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)

</div>

---

## 🌟 What's New in CineIQ v2.0?

CineIQ v2.0 is a complete reimagining of the platform designed to transition from a conceptual prototype into a **production-ready, high-performance streaming & discovery ecosystem** for real users.

- 🚀 **10,000+ Real Movie Catalog**: Pre-populated using the open MovieLens dataset with high-resolution posters, genre tags, emotional arcs, and popularity rankings — zero external API keys required to start developing!
- ⚡ **Dual Database Engine**: Zero-config local development powered by **async SQLite (`aiosqlite`)** and production-grade **PostgreSQL (`asyncpg`)** support.
- 🧠 **AI Semantic Search & Mood Mapping**: Natural language query extraction with Google Gemini and vector similarity search.
- 🍿 **Real-Time Watch Party Sync**: WebSocket-driven synchronized viewing rooms with instant messaging and participant state management.
- 📊 **Dynamic Taste Profile Radar**: Interactive Recharts radar visualization evaluating user preferences across 18 genres based on ratings and watchlist activity.
- 🎨 **Cinematic Glassmorphism UI**: Next.js 15 App Router, React 19, dark/light theme switching with zero flash of unstyled content, and accessible responsive layouts.
- 🔒 **Clerk Authentication & Role Security**: Secure OAuth, protected profile routes, and JWT authorization headers across API endpoints.

---

## 🏆 ECSoC26 & ECSOC Sentinel Scoring Guide

This repository is an official participant in **ECSoC 2026**. All contributions are automatically evaluated and scored by **ECSOC Sentinel**.

### 🏷️ Mandatory PR Label
> [!IMPORTANT]
> **Every pull request MUST include the label: `ECSoC26`** before merging to be processed by the automated scoring system.

### 💯 Points Breakdown by Difficulty

| Difficulty Level | Label | Points Awarded | Description |
| :--- | :--- | :---: | :--- |
| **Easy** | `ECSoC26-L1` | **5 Points** | Small bug fixes, documentation, CSS tweaks, UI formatters, accessibility tags |
| **Medium** | `ECSoC26-L2` | **10 Points** | Multi-facet search filters, database pagination, new API routes, responsive layouts, CI/CD |
| **Difficult** | `ECSoC26-L3` | **15 Points** | Real-time WebRTC sync, vector embeddings, ML recommendation engines, E2E test suites |

### 🎁 Project Admin (PA) Bonus XP

Project Admins can award additional Bonus XP labels for exemplary pull requests:

| Bonus Label | Bonus XP | Applicable Contributions |
| :--- | :---: | :--- |
| `good-issue` | **+10 XP** | Exceptionally detailed, reproducible bug reports or architectural RFCs |
| `good-pr` | **+15 XP** | Clean code, thorough unit tests, and comprehensive PR descriptions |
| `good-ui` | **+25 XP** | High-polish UI components, micro-interactions, responsive refinements |
| `good-backend` | **+50 XP** | Complex algorithmic improvements, caching architectures, database migrations |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Next.js 15 Frontend                      │
│   (App Router, SSR, Framer Motion, Recharts, Clerk Auth)    │
└──────────────────────────────┬──────────────────────────────┘
                               │ HTTP / WebSockets (Port 3000 -> 8001)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                     FastAPI Backend                         │
│   (Async Routes, Rate Limiting, Structlog, Lifespan Seed)   │
└──────────────┬───────────────┬───────────────┬──────────────┘
               │               │               │
               ▼               ▼               ▼
     ┌──────────────────┐┌───────────┐┌─────────────────┐
     │ SQLite / Postgres││  Upstash  ││ Google Gemini / │
     │ (SQLAlchemy ORM) ││   Redis   ││ Qdrant VectorDB │
     │  10k+ Movies DB  ││  (Cache)  ││ (Semantic LLM)  │
     └──────────────────┘└───────────┘└─────────────────┘
```

---

## 🚀 Quick Start Guide

### Prerequisites
- **Node.js**: v20.x or v22.x
- **Python**: 3.11, 3.12, or 3.13
- **Git**: Installed and configured

---

### Option 1: Local Development (Recommended — Zero External Config)

#### 1. Clone Repository
```bash
git clone https://github.com/RamK2006/cineiq.git
cd cineiq
```

#### 2. Backend Setup
```bash
cd backend

# Create and activate Python virtual environment
python -m venv venv

# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Linux / macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Bulk import 9,700+ movies from MovieLens
python -m app.services.bulk_import

# Start FastAPI server on port 8001
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```
*API will be live at `http://localhost:8001` (Interactive docs at `http://localhost:8001/docs`).*

#### 3. Frontend Setup
In a new terminal window:
```bash
cd frontend

# Install Node dependencies
npm install

# Start Next.js development server on port 3000
npm run dev
```
*Open `http://localhost:3000` in your browser.*

---

### Option 2: Docker Compose (Production Stack)

```bash
# Build and run all services
docker-compose up --build

# Run in detached mode
docker-compose up -d
```

---

## 📡 API Endpoints Overview

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :---: |
| `GET` | `/health` | Live health probe (Postgres, Redis, Gemini) | ❌ |
| `GET` | `/api/v1/recommend/trending` | Fetch trending movies by popularity rank | ❌ |
| `GET` | `/api/v1/search/semantic?q={query}` | AI semantic & keyword movie search | ❌ |
| `GET` | `/api/v1/movie/{id}` | Detailed movie metadata & emotional arc | ❌ |
| `GET` | `/api/v1/movies/{id}/reviews` | Paginated reviews & aggregate rating breakdown | ❌ |
| `POST` | `/api/v1/movies/{id}/reviews` | Submit user movie review & 1-5 star rating | ✅ |
| `GET` | `/api/v1/profile/stats` | Compute user taste profile & genre scores | ✅ |
| `WS` | `/api/v1/room/{id}/ws` | Real-time Watch Party synchronization socket | ❌ |

---

## 🗺️ CineIQ v2.0 Roadmap

- [x] **Zero-Config Local Setup**: Native async SQLite database with MovieLens seed.
- [x] **Full-Stack Integration**: Homepage, Search, Detail, and Reviews wired to backend APIs.
- [x] **Dark / Light Theme**: Zero-flicker CSS variable color tokens.
- [ ] **Multi-Facet Search**: Filter by genres, release year range, and minimum rating. 🚧
- [ ] **Watchlist & Favorites**: Persistent user lists synced with Clerk accounts. 🚧
- [ ] **WebRTC Video Sync**: Host playback synchronization for Watch Parties. 🚧
- [ ] **Vector Search Pipeline**: Sentence-transformers embeddings indexed in Qdrant. 🚧
- [ ] **Automated CI/CD**: GitHub Actions workflows for pytest, ruff, ESLint, and Vitest. 🚧
- [ ] **Mobile PWA**: Progressive Web App offline caching and installation prompts. 🚧

---

## 🤝 Contributing Guidelines

We love contributions! Follow these steps to submit your work for **ECSoC26**:

1. **Find an Open Issue**: Browse our [Issue Tracker](https://github.com/RamK2006/cineiq/issues) and find an issue tagged with `ECSoC26` and your desired difficulty level (`ECSoC26-L1`, `ECSoC26-L2`, `ECSoC26-L3`).
2. **Fork & Branch**:
   ```bash
   git checkout -b feat/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```
3. **Follow Code Quality Standards**:
   - Backend: Format with `ruff` and type-check with `mypy`.
   - Frontend: Verify with `npm run lint` and ensure clean builds with `npm run build`.
4. **Commit with Conventional Commits**:
   ```bash
   git commit -m "feat(search): add genre and year filters to semantic search"
   ```
5. **Submit Pull Request**:
   - Link the issue in your PR body: `Fixes #<issue_number>`.
   - Ensure the `ECSoC26` label is applied.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

<div align="center">
  <sub>Built with ❤️ for ECSoC 2026 by RamK2006 & the CineIQ Open Source Community.</sub>
</div>