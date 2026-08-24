import { NextRequest, NextResponse } from 'next/server';
import { searchCatalog } from '@/lib/catalog';

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const query = searchParams.get('q') || '';
  const limit = parseInt(searchParams.get('limit') || '20', 10);

  const results = searchCatalog(query, limit).map((m) => ({
    id: m.id,
    title: m.title,
    overview: m.overview,
    poster_path: m.poster_path,
    similarity_score: m.match_score,
  }));

  return NextResponse.json({
    query,
    results,
  });
}
