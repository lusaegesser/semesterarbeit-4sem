from sqlalchemy import Column, Integer, String

from app.database import Base


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255))
    artist = Column(String(255))
    genre = Column(String(100))
    bpm = Column(Integer)

    key = Column(String(100))
    status = Column(String(100))

    audio_file = Column(String(255), nullable=True)


class Share(Base):
    __tablename__ = "shares"
    token_hash = Column(String(64), primary_key=True)
    track_id = Column(Integer, nullable=False, index=True)


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    track_id = Column(Integer, nullable=False, index=True)
    author = Column(String(80), nullable=False)
    body = Column(String(2000), nullable=False)
    seconds = Column(Integer, nullable=False)
