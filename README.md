# CINEIQ 🎬 — Version 2.0

<div align="center">

![CineIQ Banner](https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1200&auto=format&fit=crop&q=80)

### **Next-Generation AI-Powered Movie Recommendation & Social Discovery Platform**
*Where artificial intelligence meets the magic of cinema, bringing movie lovers together in real-time synchronized Watch Parties.*

[![ECSoC26](https://img.shields.io/badge/Event-ECSoC26-6f42c1?style=for-the-badge&logo=github)](https://github.com/apps/ecsoc-sentinel)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Next.js 15](https://img.shields.io/badge/Next.js-15.5-black.svg?style=for-the-badge&logo=next.js&logoColor=white)](https://nextjs.org)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6.svg?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

</div>

---

## 🌟 The CineIQ Vision

Ever spent 45 minutes scrolling through streaming platforms just to pick a movie, or struggled to watch a film with long-distance friends while counting down *"3, 2, 1, hit play"*?

**CineIQ v2.0** solves this with an all-in-one cinematic ecosystem:
1. 🧠 **AI Semantic Search & Mood Discovery**: Search naturally (e.g. *"mind-bending space thriller with deep emotional twists"*) powered by Google Gemini and vector embeddings.
2. 🍿 **Synchronized Watch Parties**: Real-time WebSocket playback synchronization with live chat, emojis, and voice chat.
3. 📊 **Dynamic Taste Profile Radar**: Interactive genre preferences computed from genuine user ratings and watch history.
4. 🚀 **10,000+ Real Movie Catalog**: Pre-populated using the open MovieLens dataset with high-res imagery, emotional arcs, and popularity scores — **zero external API keys required to start developing!**
5. ⚡ **Dual Database Engine**: Zero-config local development powered by **async SQLite (`aiosqlite`)** and production-ready **PostgreSQL (`asyncpg`)** support.

---

## 🗺️ Project Structure

CineIQ is organized as a clean, decoupled monorepo:

```
cineiq/
├── backend/                        # FastAPI Async Python Backend
│   ├── app/
│   │   ├── api/v1/                 # Modular REST & WebSocket Route Handlers
│   │   │   ├── movie.py            # Movie details, backdrops, emotional arcs
│   │   │   ├── recommend.py        # Trending & personalized recommendation feeds
│   │   │   ├── reviews.py          # User ratings, reviews, and histograms
│   │   │   ├── room.py             # WebSocket watch party rooms & host sync
│   │   │   ├── search.py           # AI semantic search & keyword query routing
│   │   │   └── profile.py          # User taste radar analytics & watch history
│   │   ├── core/                   # Security, Rate Limiting, & Pydantic Config
│   │   ├── db/                     # SQLAlchemy Models & Async Session Factory
│   │   ├── services/               # Background Workers, MovieLens Sync, ML
│   │   └── main.py                 # FastAPI Application Lifecycle & Middleware
│   ├── tests/                      # Automated Pytest Suite with SQLite Fixtures
│   └── requirements.txt            # Python Dependencies
│
├── frontend/                       # Next.js 15 App Router Frontend
│   ├── src/
│   │   ├── app/                    # Page Routes (SSR + React 19)
│   │   │   ├── page.tsx            # Cinematic Home Landing & Movie Carousels
│   │   │   ├── movie/[id]/         # Dynamic Movie Detail, Emotional Graph, Reviews
│   │   │   ├── search/             # Semantic Search & Interactive Multi-Facet Filters
│   │   │   ├── room/[id]/          # Real-Time Watch Party Player & Live Chat
│   │   │   └── profile/            # User Taste Profile Radar & Watchlist
│   │   ├── components/             # Reusable UI (Skeletons, Nav, Custom Cursor, Theme)
│   │   ├── context/                # React Context Providers (ThemeContext)
│   │   ├── hooks/                  # Custom React Hooks (Debounce, Media Queries)
│   │   └── lib/                    # API Client, Type Definitions, Formatters
│   └── package.json                # Frontend Dependencies & Scripts
│
├── .github/                        # Workflows (CI/CD) & Issue Templates
│   └── workflows/ci.yml            # Automated Ruff, Pytest, ESLint & Build Checks
└── docker-compose.yml              # Production Container Orchestration
```

---

## 🎯 What We Are Looking For (Call for Collaborators!)

We are inviting contributors across all skill levels to help transform CineIQ into the ultimate open-source streaming platform! Here are key areas where your contributions will make a huge impact:

### 1. 🎬 Movie Quality & Metadata Enrichment
- **Real Posters & Backdrop Hydration**: Connecting TMDB/OMDb APIs or Wikipedia scrapers to upgrade MovieLens titles with authentic studio posters, verified cast photos, and official trailers.
- **Top 250 Curated Classics**: Seeding hand-verified metadata for all-time greatest cinema masterpieces.
- **Streaming Availability**: Adding "Where to Watch" badges (Netflix, Prime, Disney+, AppleTV) using provider schemas.

### 2. 🔍 Real-World Search Optimization
- **Fuzzy Typo-Tolerance**: Implementing Trigram / Levenshtein distance matching so misspelled queries (e.g. *"Insepshun"*) return accurate results with *"Did you mean...?"* suggestions.
- **Hybrid Search Ranking**: Combining dense semantic embeddings with sparse BM25 keyword relevance using Reciprocal Rank Fusion (RRF).
- **Search History & Quick Chips**: Client-side query history and one-click trending suggestion tags.

### 3. 🍿 Real-World Watch Party Enhancements
- **Synchronized Video Player**: Integrating custom HTML5/HLS players with millisecond-accurate playhead buffer sync.
- **Host Moderation Tools**: Room passcodes, host transfer, mute/kick controls, and participant capacity limits.
- **Voice & Video Chat Mesh**: Optional WebRTC audio/video mesh for small friend groups watching together.
- **Full-Screen Cinema Mode**: Translucent floating chat overlay and floating emoji reactions.

### 4. 🎨 Glassmorphic UI/UX Elegance
- **Micro-Interactions**: Smooth Framer Motion transitions, responsive tablet/ultrawide grid breakpoints, and mobile swipe gestures.
- **Accessibility (a11y)**: WCAG 2.1 AA compliance, ARIA live regions, and keyboard navigation shortcuts.

---

## 🏆 ECSoC26 & ECSOC Sentinel Scoring Guide

This repository is an official participant in **ECSoC 2026**. All contributions are automatically evaluated and scored by **ECSOC Sentinel**.

### 🏷️ Mandatory PR Label
> [!IMPORTANT]
> **Every pull request MUST include the label: `ECSoC26`** before merging to be processed by the automated scoring system.

### 💯 Points Breakdown

| Difficulty Level | Label | Points Awarded | Description |
| :--- | :--- | :---: | :--- |
| **Easy** | `ECSoC26-L1` | **5 Points** | Small bug fixes, documentation, CSS tweaks, UI formatters, accessibility tags |
| **Medium** | `ECSoC26-L2` | **10 Points** | Multi-facet search filters, database pagination, new API routes, responsive layouts, CI/CD |
| **Difficult** | `ECSoC26-L3` | **15 Points** | Real-time WebRTC sync, vector embeddings, ML recommendation engines, E2E test suites |

### 🎁 Project Admin (PA) Bonus XP

| Bonus Label | Bonus XP | Applicable Contributions |
| :--- | :---: | :--- |
| `good-issue` | **+10 XP** | Exceptionally detailed, reproducible bug reports or architectural RFCs |
| `good-pr` | **+15 XP** | Clean code, thorough unit tests, and comprehensive PR descriptions |
| `good-ui` | **+25 XP** | High-polish UI components, micro-interactions, responsive refinements |
| `good-backend` | **+50 XP** | Complex algorithmic improvements, caching architectures, database migrations |

---

## 🚀 Quick Start (Up & Running in 2 Minutes)

### Prerequisites
- **Node.js**: v20.x or v22.x
- **Python**: 3.11, 3.12, or 3.13
- **Git**: Installed on your machine

### 1. Clone & Setup Backend
```bash
git clone https://github.com/RamK2006/cineiq.git
cd cineiq/backend

# Create virtual environment
python -m venv venv

# Activate (Windows PowerShell):
.\venv\Scripts\Activate.ps1
# Activate (Linux / macOS):
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt ruff pytest

# Start FastAPI backend (port 8001)
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```
*API will be live at `http://localhost:8001` (Interactive Swagger docs at `http://localhost:8001/docs`).*

### 2. Setup Frontend
In a separate terminal:
```bash
cd cineiq/frontend

# Install dependencies
npm install

# Start Next.js frontend (port 3000)
npm run dev
```
*Open `http://localhost:3000` to start exploring CineIQ!*

---

## 📡 API Endpoints Overview

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :---: |
| `GET` | `/health` | Health probe (Postgres/SQLite, Redis, Gemini) | ❌ |
| `GET` | `/api/v1/recommend/trending` | Fetch trending movies by popularity rank | ❌ |
| `GET` | `/api/v1/search/semantic?q={query}` | AI semantic & keyword movie search | ❌ |
| `GET` | `/api/v1/movie/{id}` | Detailed movie metadata & emotional arc | ❌ |
| `GET` | `/api/v1/movies/{id}/reviews` | Paginated reviews & rating distribution | ❌ |
| `POST` | `/api/v1/movies/{id}/reviews` | Submit user movie review & 1-5 star rating | ✅ |
| `GET` | `/api/v1/profile/stats` | Compute user taste profile & genre scores | ✅ |
| `WS` | `/api/v1/room/{id}/ws` | Real-time Watch Party synchronization socket | ❌ |

---

## 🤝 How to Contribute

Ready to write your first contribution? Check out our step-by-step [**Contributing Guide (CONTRIBUTING.md)**](CONTRIBUTING.md) for detailed instructions on forking, local verification commands, commit formatting, and PR submission.

Browse open issues by difficulty:
- [🟢 Easy Issues (ECSoC26-L1)](https://github.com/RamK2006/cineiq/issues?q=is%3Aissue+is%3Aopen+label%3AECSoC26-L1)
- [🟡 Medium Issues (ECSoC26-L2)](https://github.com/RamK2006/cineiq/issues?q=is%3Aissue+is%3Aopen+label%3AECSoC26-L2)
- [🔴 Advanced Issues (ECSoC26-L3)](https://github.com/RamK2006/cineiq/issues?q=is%3Aissue+is%3Aopen+label%3AECSoC26-L3)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

<div align="center">
  <sub>Built with ❤️ by RamK2006 & the CineIQ Open Source Community.</sub>
</div>