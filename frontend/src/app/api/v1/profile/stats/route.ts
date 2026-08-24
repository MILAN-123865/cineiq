import { NextResponse } from 'next/server';

export async function GET() {
  return NextResponse.json({
    movies_watched: 42,
    reviews: 12,
    genre_preferences: [
      { genre: 'Sci-Fi', score: 88 },
      { genre: 'Action', score: 82 },
      { genre: 'Adventure', score: 75 },
      { genre: 'Drama', score: 70 },
      { genre: 'Thriller', score: 65 },
      { genre: 'Animation', score: 60 },
    ],
  });
}
