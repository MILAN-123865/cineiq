const BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8001/api/v1';

export interface MovieItem {
  id: string;
  title: string;
  poster_path?: string | null;
  vote_average: number;
  genres: string[];
  match_score: number;
}

export interface RecommendationResponse {
  algorithm: string;
  movies: MovieItem[];
}

export async function apiRequest(endpoint: string, options: RequestInit = {}) {
  const url = `${BASE_URL}${endpoint.startsWith('/') ? '' : '/'}${endpoint}`;
  
  const headers = new Headers(options.headers);
  if (!headers.has('Content-Type')) {
    headers.set('Content-Type', 'application/json');
  }

  try {
    if (typeof window !== 'undefined' && (window as any).Clerk) {
      const session = (window as any).Clerk.session;
      if (session) {
        const token = await session.getToken();
        if (token) {
          headers.set('Authorization', `Bearer ${token}`);
        }
      }
    }
  } catch (err) {
    console.warn("Clerk token extraction failed:", err);
  }

  const response = await fetch(url, {
    ...options,
    headers,
  });

  if (!response.ok) {
    const errorBody = await response.json().catch(() => ({}));
    throw new Error(errorBody.detail || `API error: ${response.statusText}`);
  }

  return response.json();
}

export async function fetchTrendingMovies(limit: number = 20): Promise<RecommendationResponse> {
  return apiRequest(`/recommend/trending?limit=${limit}`);
}

export async function fetchPersonalizedMovies(limit: number = 20): Promise<RecommendationResponse> {
  return apiRequest(`/recommend/personalized?limit=${limit}`);
}
