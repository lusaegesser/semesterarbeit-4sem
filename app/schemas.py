from pydantic import BaseModel, ConfigDict, Field, field_validator


class TrackBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    artist: str = Field(min_length=1, max_length=255)
    genre: str = Field(min_length=1, max_length=100)
    bpm: int = Field(ge=0, le=400)
    key: str = Field(max_length=100)
    status: str = Field(max_length=100)


    @field_validator("title", "artist", "genre")
    @classmethod
    def not_blank(cls, value):
        value = value.strip()
        if not value:
            raise ValueError("Darf nicht leer sein")
        return value


class TrackCreate(TrackBase):
    pass


class TrackResponse(TrackBase):
    id: int

    audio_file: str | None = None
    model_config = ConfigDict(from_attributes=True)
