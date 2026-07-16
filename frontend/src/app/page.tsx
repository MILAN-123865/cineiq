'use client';

import { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { Play, Info } from 'lucide-react';
import Link from 'next/link';
import { apiRequest } from '@/lib/api';

// Fallback Mock data if API is down
const MOCK_HERO_MOVIE = {
  id: '1',
  title: 'Dune: Part Two',
  overview: 'Paul Atreides unites with Chani and the Fremen while on a warpath of revenge against the conspirators who destroyed his family.',
  backdrop: 'https://image.tmdb.org/t/p/original/8rpDcsfLJypbO6vtecsmHLsC88C.jpg',
  match: '98% Match'
};

const MOCK_TRENDING_MOVIES = [
  { id: '1', title: 'Dune: Part Two', poster: 'https://image.tmdb.org/t/p/w500/1pdfLvkbY9ohJlCjQH2JGqpTd4p.jpg' },
  { id: '2', title: 'Oppenheimer', poster: 'https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg' },
  { id: '3', title: 'Poor Things', poster: 'https://image.tmdb.org/t/p/w500/kCGlIMHnOm8PhcbTi03XQ5VGe1T.jpg' },
  { id: '4', title: 'Interstellar', poster: 'https://image.tmdb.org/t/p/w500/gEU2QlsE1ZEbKU01E8XgK31rGfQ.jpg' },
  { id: '5', title: 'Inception', poster: 'https://image.tmdb.org/t/p/w500/oYuLEt3zVCKqA3F0B7I2G0kE7Y.jpg' },
  { id: '6', title: 'Arrival', poster: 'https://image.tmdb.org/t/p/w500/x2FJsf1ElAgr63Y3PNPtJrcmpoe.jpg' }
];

export default function HomePage() {
  const [typedText, setTypedText] = useState('');
  const [trendingMovies, setTrendingMovies] = useState<any[]>([]);
  const [heroMovie, setHeroMovie] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const fullText = "Discover films that match your soul.";

  // Typewriter effect
  useEffect(() => {
    let i = 0;
    const interval = setInterval(() => {
      if (i <= fullText.length) {
        setTypedText(fullText.slice(0, i));
        i++;
      } else {
        clearInterval(interval);
      }
    }, 50);
    return () => clearInterval(interval);
  }, []);

  // Fetch API movies
  useEffect(() => {
    async function loadData() {
      try {
        const response = await apiRequest('recommend/trending');
        if (response && response.movies && response.movies.length > 0) {
          // Map to correct shape
          const fetchedMovies = response.movies.map((m: any) => ({
            id: m.id,
            title: m.title,
            poster: m.poster_path || 'https://image.tmdb.org/t/p/w500/kCGlIMHnOm8PhcbTi03XQ5VGe1T.jpg',
            match: `${Math.round(m.match_score * 100)}% Match`
          }));
          setTrendingMovies(fetchedMovies);

          // Find a hero movie from trending that has a backdrop (or default to first item)
          setHeroMovie({
            id: response.movies[0].id,
            title: response.movies[0].title,
            overview: "Trending movie on CineIQ now.",
            backdrop: response.movies[0].poster_path?.replace('/w500', '/original') || MOCK_HERO_MOVIE.backdrop,
            match: `${Math.round(response.movies[0].match_score * 100)}% Match`
          });
        } else {
          throw new Error("Empty movies list from backend");
        }
      } catch (err) {
        console.warn("Failed to load trending movies from API, using local fallbacks:", err);
        setTrendingMovies(MOCK_TRENDING_MOVIES);
        setHeroMovie(MOCK_HERO_MOVIE);
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, []);

  const activeHero = heroMovie || MOCK_HERO_MOVIE;

  return (
    <main>
      {/* Hero Section */}
      <section style={{
        position: 'relative',
        height: '85vh',
        width: '100%',
        display: 'flex',
        alignItems: 'center',
        padding: '0 5%',
        overflow: 'hidden'
      }}>
        {/* Background Image & Gradient */}
        <div style={{
          position: 'absolute', inset: 0, zIndex: -1,
          backgroundImage: `url(${activeHero.backdrop})`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          backgroundRepeat: 'no-repeat',
        }} />
        <div style={{
          position: 'absolute', inset: 0, zIndex: -1,
          background: 'linear-gradient(to right, #05050A 20%, transparent 60%), linear-gradient(to top, #05050A 0%, transparent 30%)'
        }} />

        {/* Hero Content */}
        <div style={{ maxWidth: '600px' }}>
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            <div style={{ color: 'var(--accent-primary)', fontWeight: 700, letterSpacing: '2px', marginBottom: '16px', fontSize: '14px' }}>
              CINEIQ PREMIERE
            </div>
            <h1 style={{ fontSize: '72px', marginBottom: '16px', textShadow: '0 4px 24px rgba(0,0,0,0.5)' }}>
              {activeHero.title}
            </h1>
            
            {/* Typewriter Effect */}
            <div style={{ fontSize: '18px', color: 'var(--text-secondary)', marginBottom: '8px', minHeight: '28px' }}>
              {typedText}<span style={{ opacity: 0.5 }}>|</span>
            </div>
            
            <p style={{ fontSize: '16px', color: '#D4D4D8', marginBottom: '32px', lineHeight: 1.6, textShadow: '0 2px 10px rgba(0,0,0,0.5)' }}>
              {activeHero.overview}
            </p>

            <div style={{ display: 'flex', gap: '16px' }}>
              <button className="btn btn-primary" style={{ padding: '14px 32px', fontSize: '16px' }}>
                <Play size={20} fill="currentColor" /> Play Now
              </button>
              <Link href={`/movie/${activeHero.id}`}>
                <button className="btn btn-glass" style={{ padding: '14px 32px', fontSize: '16px' }}>
                  <Info size={20} /> More Info
                </button>
              </Link>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Rows */}
      <section style={{ padding: '0 5%', marginTop: '-80px', position: 'relative', zIndex: 10 }}>
        <h3 style={{ fontSize: '24px', marginBottom: '20px' }}>Top Picks for You</h3>
        {loading ? (
          <div style={{ display: 'flex', gap: '16px', paddingBottom: '32px' }}>
            {[1, 2, 3, 4, 5, 6].map(n => (
              <div key={n} className="skeleton" style={{ width: '220px', height: '330px', borderRadius: '16px' }} />
            ))}
          </div>
        ) : (
          <div style={{ display: 'flex', gap: '16px', overflowX: 'auto', paddingBottom: '32px' }}>
            {trendingMovies.map((movie, i) => (
              <motion.div
                key={movie.id}
                initial={{ opacity: 0, x: 50 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1, duration: 0.5 }}
                style={{ flex: '0 0 auto', width: '220px' }}
              >
                <Link href={`/movie/${movie.id}`}>
                  <div className="movie-card">
                    <img src={movie.poster} alt={movie.title} className="movie-poster" />
                    <div className="movie-overlay">
                      <div className="movie-title">{movie.title}</div>
                      <div className="movie-meta">
                        <span style={{ color: '#22C55E', fontWeight: 600 }}>{movie.match || '95% Match'}</span>
                      </div>
                    </div>
                  </div>
                </Link>
              </motion.div>
            ))}
          </div>
        )}
      </section>
    </main>
  );
}
