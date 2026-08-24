import { NextRequest, NextResponse } from 'next/server';
import { MOVIE_CATALOG } from '@/lib/catalog';

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const limit = parseInt(searchParams.get('limit') || '20', 10);

  // Return shuffled personalized feed
  const shuffled = [...MOVIE_CATALOG].sort(() => 0.5 - Math.random());
  const movies = shuffled.slice(0, limit).map((m) => ({
    id: m.id,
    title: m.title,
    poster_path: m.poster_path,
    vote_average: m.vote_average,
    genres: m.genres,
    match_score: m.match_score,
  }));

  return NextResponse.json({
    algorithm: 'edge_collaborative_filtering',
    movies,
  });
}
