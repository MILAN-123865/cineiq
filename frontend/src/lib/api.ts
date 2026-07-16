const BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8001/api/v1';

export async function apiRequest(endpoint: string, options: RequestInit = {}) {
  const url = `${BASE_URL}${endpoint.startsWith('/') ? '' : '/'}${endpoint}`;
  
  const headers = new Headers(options.headers);
  if (!headers.has('Content-Type')) {
    headers.set('Content-Type', 'application/json');
  }

  // If there's an active Clerk session, we can dynamically retrieve the JWT token:
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
