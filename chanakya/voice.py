"""Optional local file-based transcription (pip install -e '.[voice]')."""
import os
from pathlib import Path

def transcribe(filename: str) -> str:
    from faster_whisper import WhisperModel
    path = Path(filename).expanduser().resolve()
    if not path.is_file() or path.stat().st_size > 20 * 1024 * 1024:
        raise ValueError("Input must be a local file no larger than 20 MiB")
    model = WhisperModel(os.getenv("WHISPER_MODEL", "base.en"),
                         device="cpu", compute_type="int8")
    segments, _ = model.transcribe(str(path), vad_filter=True)
    return " ".join(segment.text.strip() for segment in segments)
