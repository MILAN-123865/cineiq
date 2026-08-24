# 🎬 CineIQ — Contributor's Guide

Welcome to the **CineIQ** open-source community! We're thrilled that you want to contribute to the next generation of AI-powered movie discovery and social streaming.

This repository is an official participant in **ECSoC 2026**. All contributions are evaluated and scored by **ECSOC Sentinel**, our automated PR scoring system.

---

## 📑 Table of Contents
1. [🏆 ECSoC26 & Automated Scoring Guide](#-ecsoc26--automated-scoring-guide)
2. [🔑 API Keys & Environment Setup](#-api-keys--environment-setup)
3. [🛠️ Development Environment Setup](#️-development-environment-setup)
4. [🚀 The Contributor Journey (Step-by-Step)](#-the-contributor-journey-step-by-step)
5. [🧪 How to Verify Your Fix (Testing Guide)](#-how-to-verify-your-fix-testing-guide)
6. [📝 Conventional Commit Guidelines](#-conventional-commit-guidelines)
7. [🤝 Code Review & Quality Standards](#-code-review--quality-standards)

---

## 🏆 ECSoC26 & Automated Scoring Guide

### 🏷️ Mandatory PR Label
> [!IMPORTANT]
> **Every pull request MUST include the label: `ECSoC26`** before merging to be processed by ECSOC Sentinel.

### 💯 Points Breakdown by Difficulty
- **Easy (`ECSoC26-L1`)** ➜ **5 Points**: Documentation, CSS tweaks, UI formatters, accessibility tags, minor bug fixes.
- **Medium (`ECSoC26-L2`)** ➜ **10 Points**: Multi-facet search filters, database pagination, new API endpoints, responsive layouts, CI/CD.
- **Difficult (`ECSoC26-L3`)** ➜ **15 Points**: WebRTC real-time sync, vector embedding pipelines, ML recommendation algorithms, E2E test suites.

### 🎁 Project Admin (PA) Bonus XP
Project Admins can award bonus labels for stellar PRs:
- `good-issue` ➜ **+10 XP** (Exceptional bug reports / RFCs)
- `good-pr` ➜ **+15 XP** (Clean code, thorough tests, clear descriptions)
- `good-ui` ➜ **+25 XP** (High-polish UI components, micro-interactions)
- `good-backend` ➜ **+50 XP** (Complex algorithmic or backend architectural feats)

---

## 🔑 API Keys & Environment Setup

CineIQ is designed for **zero-config local development** out of the box! You can run the entire backend and frontend without external services, but you can configure additional keys for advanced features:

| Service / Key | Required? | Where to Get | Purpose in CineIQ |
| :--- | :---: | :--- | :--- |
| **Movie Catalog** | ❌ *(Built-in)* | Automatically downloaded from [MovieLens](https://grouplens.org/datasets/movielens/) | 9,700+ movies with posters & genres. Runs completely offline. |
| **TMDB API** | ❌ *(Optional)* | [themoviedb.org/settings/api](https://www.themoviedb.org/settings/api) | High-res official poster & backdrop hydration. |
| **Google Gemini API** | ❌ *(Optional)* | [Google AI Studio](https://aistudio.google.com/) | Natural language keyword extraction for search. |
| **Clerk Auth** | ❌ *(Built-in Test Key)* | [clerk.com](https://clerk.com/) | User authentication & protected profile routes. |
| **Upstash Redis** | ❌ *(Optional)* | [upstash.com](https://upstash.com/) | Distributed rate limiting and response caching. |
| **Database** | ❌ *(Built-in SQLite)* | Native async SQLite (`aiosqlite`) | Zero-config local database. PostgreSQL supported for production. |

---

## 🛠️ Development Environment Setup

### 1. Clone your Fork
```bash
git clone https://github.com/<YOUR_USERNAME>/cineiq.git
cd cineiq
git remote add upstream https://github.com/RamK2006/cineiq.git
```

### 2. Backend Setup
```bash
cd backend

# Create Python virtual environment (Python 3.11+)
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\Activate.ps1
# Linux / macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt ruff pytest

# Start FastAPI dev server on port 8001
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```
*Verify: Open `http://localhost:8001/health` in your browser. You should see `{"status": "healthy"}`.*

### 3. Frontend Setup
In a new terminal window:
```bash
cd frontend

# Install dependencies
npm install

# Start Next.js dev server on port 3000
npm run dev
```
*Verify: Open `http://localhost:3000` in your browser to explore the cinematic home page!*

---

## 🚀 The Contributor Journey (Step-by-Step)

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Pick Issue  │────▶│ Create Branch│────▶│ Code & Verify│────▶│ Submit PR    │
│  (ECSoC26)   │     │ (feat/fix)   │     │ (Tests/Lint) │     │ (+ECSoC26)   │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
```

1. **Pick an Issue**: Browse the [Issues list](https://github.com/RamK2006/cineiq/issues) and comment on the issue you want to work on.
2. **Create a Feature Branch**:
   ```bash
   git checkout main
   git pull upstream main
   git checkout -b feat/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```
3. **Make Your Changes**: Write clean, modular, well-commented code following the architecture of the existing modules.
4. **Verify Locally**: Run the automated test suites (see below).
5. **Commit & Push**:
   ```bash
   git add .
   git commit -m "feat(search): add genre filter to semantic search"
   git push origin feat/your-feature-name
   ```
6. **Open a Pull Request**:
   - Title your PR with conventional commit format (e.g. `feat(ui): add trailer modal`).
   - In the PR description, include `Fixes #<issue_number>`.
   - Add screenshots or screen recordings for UI changes.
   - **Ensure the `ECSoC26` label is applied** to your PR!

---

## 🧪 How to Verify Your Fix (Testing Guide)

Before submitting your PR, ensure all automated verification checks pass cleanly:

### 🐍 Backend Verification
```bash
# 1. Check linting and formatting with Ruff (0 errors)
ruff check backend

# 2. Run automated test suite with Pytest (100% pass)
pytest -p no:cacheprovider

# 3. Test API endpoint manually
curl http://localhost:8001/api/v1/recommend/trending?limit=3
```

### ⚛️ Frontend Verification
```bash
cd frontend

# 1. Run ESLint
npm run lint

# 2. Run TypeScript strict type-check
npx tsc --noEmit

# 3. Run Next.js production build (Must complete with exit code 0)
npm run build
```

---

## 📝 Conventional Commit Guidelines

We use [Conventional Commits](https://www.conventionalcommits.org/) to keep the git history clean and descriptive:

- `feat(scope)`: A new feature for the user (e.g. `feat(search): add fuzzy typo tolerance`)
- `fix(scope)`: A bug fix (e.g. `fix(ui): resolve layout shift in movie poster`)
- `docs(scope)`: Documentation changes (e.g. `docs(readme): add API reference table`)
- `perf(scope)`: Performance improvements (e.g. `perf(caching): add Redis LRU layer`)
- `refactor(scope)`: Code restructuring without feature changes
- `test(scope)`: Adding or correcting tests (e.g. `test(backend): add pytest fixtures`)

---

## 🤝 Code Review & Quality Standards

- **No Hardcoded Secrets**: Always use environment variables or Pydantic settings.
- **Graceful Fallbacks**: Ensure the app continues to function if external APIs (TMDB, Gemini, Redis) are temporarily unreachable.
- **Responsive & Accessible**: Support mobile (<640px), tablet, and desktop viewports, and include accessible ARIA labels.
- **Supportive Community**: We value constructive feedback, collaboration, and learning! If you get stuck, ask questions in the issue thread.

Happy hacking! 🍿🎬
