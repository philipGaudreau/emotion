from emotion import root_dir
from emotion.models.audio_model import AudioModel


def test_audio_model():
    audio_model = AudioModel()
    processed_features = audio_model.preprocess([root_dir / "data/raw_sample/audio/UlTJmndbGHM.wav"])
    predictions = audio_model.predict(processed_features)
    assert len(predictions) == 1
