from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
import json


class Settings(BaseSettings):
    # App
    environment: str = "development"
    frontend_url: str = "http://localhost:3000"
    backend_cors_origins: str | List[str] = []
    backend_host: str = "0.0.0.0"
    backend_port: int = 8001
    max_room_participants: int = 10

    # Database
    database_url: str = ""

    # Upstash Redis
    upstash_redis_url: str = ""
    upstash_redis_token: str = ""

    # Database
    database_url: str = "postgresql+asyncpg://cineiq:cineiq_secret@postgres_cineiq:5432/cineiq"

    # Auth
    clerk_secret_key: str = ""
    next_public_clerk_publishable_key: str = ""
    clerk_jwt_audience: str = ""
    clerk_audience: str = ""

    # Rate Limiting
    rate_limit_enabled: bool = True
    rate_limit_global: str = "100/minute"
    rate_limit_semantic_search: str = "10/minute"

    # External APIs
    tmdb_api_key: str = ""

    # Gemini LLM
    gemini_api_key: str = ""
    gemini_model: str = "gemini-2.0-flash"

    # Qdrant Vector DB
    qdrant_url: str = "http://localhost:6333"
    qdrant_api_key: str = ""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )

    @property
    def cors_origins_list(self) -> List[str]:
        origins = [self.frontend_url]
        if self.environment == "development" and "http://localhost:3000" not in origins:
            origins.append("http://localhost:3000")
            
        if isinstance(self.backend_cors_origins, str):
            try:
                parsed = json.loads(self.backend_cors_origins)
                if isinstance(parsed, list):
                    origins.extend(parsed)
            except json.JSONDecodeError:
                origins.extend([
                    origin.strip()
                    for origin in self.backend_cors_origins.split(",")
                    if origin.strip()
                ])
        elif isinstance(self.backend_cors_origins, list):
            origins.extend(self.backend_cors_origins)
            
        return list(set(origins))


settings = Settings()
