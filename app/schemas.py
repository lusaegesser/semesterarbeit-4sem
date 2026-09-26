from pydantic import BaseModel, ConfigDict


class TrackBase(BaseModel):
    title: str
    artist: str
    genre: str
    bpm: int
    key: str
    status: str


class TrackCreate(TrackBase):
    pass


class TrackResponse(TrackBase):
    id: int

    audio_file: str | None = None
    model_config = ConfigDict(from_attributes=True)
