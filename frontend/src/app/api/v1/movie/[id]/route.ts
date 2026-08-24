import { NextRequest, NextResponse } from 'next/server';
import { findMovieById, MOVIE_CATALOG } from '@/lib/catalog';

export async function GET(
  request: NextRequest,
  context: { params: Promise<{ id: string }> }
) {
  const { id } = await context.params;
  const movie = findMovieById(id) || MOVIE_CATALOG[0];

  return NextResponse.json({
    id: movie.id,
    title: movie.title,
    tagline: movie.tagline,
    overview: movie.overview,
    year: movie.year,
    runtime: movie.runtime,
    rating: movie.rating,
    genres: movie.genres,
    director: movie.director,
    cast: movie.cast,
    backdrop: movie.backdrop_path,
    dominant_emotion: movie.dominant_emotion,
    match: Math.round(movie.match_score * 100),
    emotional_arc: movie.emotional_arc,
  });
}
