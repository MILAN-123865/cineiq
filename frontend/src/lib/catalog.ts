export interface CatalogMovie {
  id: string;
  title: string;
  tagline: string;
  overview: string;
  year: string;
  runtime: string;
  rating: string;
  genres: string[];
  director: string;
  cast: string[];
  poster_path: string;
  backdrop_path: string;
  vote_average: number;
  vote_count: number;
  dominant_emotion: string;
  match_score: number;
  emotional_arc: { time: string; tension: number; awe: number; action: number }[];
}

export const MOVIE_CATALOG: CatalogMovie[] = [
  {
    id: "1",
    title: "Interstellar",
    tagline: "Mankind was born on Earth. It was never meant to die here.",
    overview: "When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.",
    year: "2014",
    runtime: "169m",
    rating: "8.7",
    genres: ["Adventure", "Drama", "Sci-Fi"],
    director: "Christopher Nolan",
    cast: ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain", "Michael Caine"],
    poster_path: "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
    backdrop_path: "https://image.tmdb.org/t/p/original/xJHokMbljvjADYdit5fK5VQsXEG.jpg",
    vote_average: 8.7,
    vote_count: 34500,
    dominant_emotion: "Awe-Inspiring",
    match_score: 0.98,
    emotional_arc: [
      { time: "0m", tension: 15, awe: 20, action: 5 },
      { time: "40m", tension: 45, awe: 70, action: 30 },
      { time: "80m", tension: 85, awe: 90, action: 65 },
      { time: "120m", tension: 95, awe: 98, action: 90 },
      { time: "160m", tension: 40, awe: 100, action: 20 }
    ]
  },
  {
    id: "2",
    title: "Inception",
    tagline: "Your mind is the scene of the crime.",
    overview: "Cobb steals information from his targets by entering their dreams. He is offered a chance to regain his old life as payment for a task considered impossible: \"inception\".",
    year: "2010",
    runtime: "148m",
    rating: "8.8",
    genres: ["Action", "Adventure", "Sci-Fi", "Thriller"],
    director: "Christopher Nolan",
    cast: ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page", "Tom Hardy"],
    poster_path: "https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg",
    backdrop_path: "https://image.tmdb.org/t/p/original/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg",
    vote_average: 8.8,
    vote_count: 36000,
    dominant_emotion: "Mind-Bending",
    match_score: 0.96,
    emotional_arc: [
      { time: "0m", tension: 30, awe: 40, action: 25 },
      { time: "35m", tension: 50, awe: 65, action: 40 },
      { time: "70m", tension: 75, awe: 80, action: 60 },
      { time: "105m", tension: 90, awe: 92, action: 85 },
      { time: "140m", tension: 98, awe: 95, action: 90 }
    ]
  },
  {
    id: "3",
    title: "Dune: Part Two",
    tagline: "Long live the fighters.",
    overview: "Paul Atreides unites with Chani and the Fremen while seeking revenge against the conspirators who destroyed his family. Facing a choice between the love of his life and the fate of the universe.",
    year: "2024",
    runtime: "166m",
    rating: "8.6",
    genres: ["Action", "Adventure", "Drama", "Sci-Fi"],
    director: "Denis Villeneuve",
    cast: ["Timothée Chalamet", "Zendaya", "Rebecca Ferguson", "Javier Bardem"],
    poster_path: "https://image.tmdb.org/t/p/w500/1pdfLvkbY9ohJlCjQH2JGqpTd4p.jpg",
    backdrop_path: "https://image.tmdb.org/t/p/original/xOMo8BRK7PfcJv9JCnx7s520b22.jpg",
    vote_average: 8.6,
    vote_count: 8500,
    dominant_emotion: "Epic Thrill",
    match_score: 0.95,
    emotional_arc: [
      { time: "0m", tension: 40, awe: 50, action: 30 },
      { time: "40m", tension: 60, awe: 80, action: 50 },
      { time: "80m", tension: 75, awe: 90, action: 70 },
      { time: "120m", tension: 90, awe: 95, action: 85 },
      { time: "160m", tension: 98, awe: 100, action: 95 }
    ]
  },
  {
    id: "4",
    title: "Oppenheimer",
    tagline: "The world forever changes.",
    overview: "The story of J. Robert Oppenheimer's role in the development of the atomic bomb during World War II.",
    year: "2023",
    runtime: "180m",
    rating: "8.9",
    genres: ["Biography", "Drama", "History"],
    director: "Christopher Nolan",
    cast: ["Cillian Murphy", "Emily Blunt", "Matt Damon", "Robert Downey Jr."],
    poster_path: "https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
    backdrop_path: "https://image.tmdb.org/t/p/original/fm6KqXpk3M2HVveHwCrBSSBaO0V.jpg",
    vote_average: 8.9,
    vote_count: 14000,
    dominant_emotion: "Tense & Gripping",
    match_score: 0.94,
    emotional_arc: [
      { time: "0m", tension: 20, awe: 30, action: 10 },
      { time: "45m", tension: 50, awe: 60, action: 20 },
      { time: "90m", tension: 80, awe: 85, action: 40 },
      { time: "135m", tension: 100, awe: 98, action: 80 },
      { time: "175m", tension: 85, awe: 90, action: 30 }
    ]
  },
  {
    id: "5",
    title: "The Dark Knight",
    tagline: "Welcome to a world without rules.",
    overview: "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
    year: "2008",
    runtime: "152m",
    rating: "9.0",
    genres: ["Action", "Crime", "Drama", "Thriller"],
    director: "Christopher Nolan",
    cast: ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"],
    poster_path: "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
    backdrop_path: "https://image.tmdb.org/t/p/original/dqK9Hag1054tghRQSqLSfrkvQnA.jpg",
    vote_average: 9.0,
    vote_count: 32000,
    dominant_emotion: "High Adrenaline",
    match_score: 0.97,
    emotional_arc: [
      { time: "0m", tension: 50, awe: 40, action: 60 },
      { time: "40m", tension: 70, awe: 60, action: 75 },
      { time: "80m", tension: 85, awe: 70, action: 80 },
      { time: "120m", tension: 95, awe: 85, action: 95 },
      { time: "150m", tension: 90, awe: 90, action: 85 }
    ]
  },
  {
    id: "6",
    title: "Spirited Away",
    tagline: "Nothing that happens is ever forgotten, even if you can't remember.",
    overview: "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, a world where humans are changed into beasts.",
    year: "2001",
    runtime: "125m",
    rating: "8.6",
    genres: ["Animation", "Adventure", "Family", "Fantasy"],
    director: "Hayao Miyazaki",
    cast: ["Rumi Hiiragi", "Miyu Irino", "Mari Natsuki", "Takashi Naito"],
    poster_path: "https://image.tmdb.org/t/p/w500/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
    backdrop_path: "https://image.tmdb.org/t/p/original/mSDsSDwaP3E7dEfUPWy4J0djt4O.jpg",
    vote_average: 8.6,
    vote_count: 16500,
    dominant_emotion: "Magical Wonder",
    match_score: 0.93,
    emotional_arc: [
      { time: "0m", tension: 20, awe: 30, action: 10 },
      { time: "30m", tension: 40, awe: 60, action: 25 },
      { time: "60m", tension: 65, awe: 85, action: 40 },
      { time: "90m", tension: 70, awe: 95, action: 35 },
      { time: "120m", tension: 30, awe: 100, action: 15 }
    ]
  },
  {
    id: "7",
    title: "Spider-Man: Across the Spider-Verse",
    tagline: "It's how you wear the mask that matters.",
    overview: "Miles Morales catapults across the Multiverse, where he encounters a team of Spider-People charged with protecting its very existence. When the heroes clash on how to handle a new threat, Miles must redefine what it means to be a hero.",
    year: "2023",
    runtime: "140m",
    rating: "8.7",
    genres: ["Action", "Adventure", "Animation", "Sci-Fi"],
    director: "Joaquim Dos Santos, Kemp Powers",
    cast: ["Shameik Moore", "Hailee Steinfeld", "Oscar Isaac", "Daniel Kaluuya"],
    poster_path: "https://image.tmdb.org/t/p/w500/8Vt6mWEReuy4Of61Lnj5Xj704m8.jpg",
    backdrop_path: "https://image.tmdb.org/t/p/original/4HodYYKEIsGOdinkGi2Ucz6X9i0.jpg",
    vote_average: 8.7,
    vote_count: 14200,
    dominant_emotion: "Mind-Bending Action",
    match_score: 0.95,
    emotional_arc: [
      { time: "0m", tension: 35, awe: 50, action: 40 },
      { time: "35m", tension: 55, awe: 75, action: 60 },
      { time: "70m", tension: 80, awe: 90, action: 85 },
      { time: "105m", tension: 95, awe: 98, action: 95 },
      { time: "135m", tension: 90, awe: 95, action: 80 }
    ]
  },
  {
    id: "8",
    title: "Parasite",
    tagline: "Act like you own the place.",
    overview: "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
    year: "2019",
    runtime: "132m",
    rating: "8.5",
    genres: ["Comedy", "Drama", "Thriller"],
    director: "Bong Joon-ho",
    cast: ["Song Kang-ho", "Lee Sun-kyun", "Cho Yeo-jeong", "Choi Woo-shik"],
    poster_path: "https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg",
    backdrop_path: "https://image.tmdb.org/t/p/original/hiKmpZMGZsrkA3cdce8a7Dpos1j.jpg",
    vote_average: 8.5,
    vote_count: 18000,
    dominant_emotion: "Tense Suspense",
    match_score: 0.92,
    emotional_arc: [
      { time: "0m", tension: 10, awe: 20, action: 5 },
      { time: "30m", tension: 30, awe: 40, action: 15 },
      { time: "65m", tension: 70, awe: 60, action: 40 },
      { time: "95m", tension: 95, awe: 80, action: 75 },
      { time: "130m", tension: 90, awe: 85, action: 50 }
    ]
  }
];

export function findMovieById(id: string): CatalogMovie | undefined {
  return MOVIE_CATALOG.find((m) => m.id === id);
}

export function searchCatalog(query: string, limit: number = 20): CatalogMovie[] {
  const q = query.toLowerCase().trim();
  if (!q) return MOVIE_CATALOG.slice(0, limit);

  return MOVIE_CATALOG.filter((m) => {
    return (
      m.title.toLowerCase().includes(q) ||
      m.overview.toLowerCase().includes(q) ||
      m.director.toLowerCase().includes(q) ||
      m.genres.some((g) => g.toLowerCase().includes(q)) ||
      m.cast.some((c) => c.toLowerCase().includes(q))
    );
  }).slice(0, limit);
}
