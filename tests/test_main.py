import os

def test_env_vars_set():
    assert os.getenv("AZURE_TRANSLATOR_KEY") is not None
    assert os.getenv("AZURE_TRANSLATOR_ENDPOINT") is not None
    assert os.getenv("AZURE_TRANSLATOR_REGION") is not None