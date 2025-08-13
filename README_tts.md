# verahession TTS Usage Example

This example shows how to use the `tts_interface` class from the `verahession.tts` module to convert text to speech.

---

### Usage

1. Import the `tts_interface` class.
2. Create an instance with your API key, gender, and accent.
3. Call the `tts` method with the text you want to speak.

---

### Example Script (`tts_example.py`)

```python
from verahession.api import tts_interface

if __name__ == "__main__":
    API_KEY = "your_api_key_here"
    gender = "female"
    accent = "english"

    tts = tts_interface(API_KEY, gender, accent)

    text = "Hello, this is a test of the verahession text-to-speech system."
    tts.tts(text)
```

---

### Notes

- Replace `"your_api_key_here"` with your actual API key.
- Supported genders and accents depend on the backend service.
- The script will send a TTS request, play the audio if successful, and print status messages.

---
If you do not yet have an API key, you need to create an account at https://hessiondynamics.com/login - and then press 'create API key' - do NOT share the key with anyone.

For more information, check the verahession documentation or support channels.
