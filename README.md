# isayscribe 🎙️✨

Bypass the $159 hardware tax. Turn your iPhone into a professional-grade AI note-taker for $0.00.

`isayscribe` is a lightweight, zero-friction, fully open-source alternative to expensive AI hardware devices like Plaud and Pocket AI. It uses the supercomputer already in your pocket (your iPhone), a free API key from Groq, and native iOS Shortcuts to give you instant, S-tier audio transcription and structured brain-dump summaries in under 3 seconds.

No subscriptions. No hardware to charge. No tracking. 100% local-first and customizable.

```
┌──────────────┐      ┌─────────────────────────┐      ┌────────────────────────┐
│  Your Voice  │ ───> │     Groq Whisper API    │ ───> │   Llama-3.3-70B API    │
│  (iPhone Mic)│      │  (Instant Transcription)│      │   (System Prompting)   │
└──────────────┘      └─────────────────────────┘      └────────────────────────┘
                                                                   │
                                                                   ▼
                                                       ┌────────────────────────┐
                                                       │   Your Apple Notes /   │
                                                       │     Obsidian Vault     │
                                                       └────────────────────────┘
```

---

## Why does this exist?

Devices like Plaud and Pocket AI are beautiful, but they charge you a high upfront premium ($159+) and lock your personal thoughts behind proprietary servers and subscription tiers.

In reality, your iPhone already has a high-quality microphone, and developers have access to **Groq's LPU-powered cloud infrastructure**, which transcribes audio and formats it with advanced LLMs for free, at speeds that feel like magic. 

`isayscribe` brings these pieces together in a simple iOS Shortcut. Bring your own API key, tap one button, and watch your messy spoken thoughts transform into polished, structured, actionable notes.

---

## Features

- **100% Free**: Operates entirely within Groq's generous perpetual free-tier limit (2,000 requests per day).
- **Insanely Fast**: Whisper Large V3 transcribes your audio, and Llama 3.3 formats it, returning a complete note in under 3 seconds.
- **Native iOS Integration**: Trigger it from your Lock Screen, Home Screen, Back Tap, or physical Action Button (iPhone 15 Pro / 16 / 16 Pro).
- **No Third-Party Apps**: Built natively using the pre-installed iOS Shortcuts app.
- **Privacy First**: Your recordings do not go to a proprietary startup's servers. They go from your iPhone directly to Groq, and are stored permanently inside your local Apple Notes or iCloud Obsidian Vault.

---

## Step-by-Step Installation Guide (Under 3 Minutes)

### Step 1: Get a Free Groq API Key
1. Go to [console.groq.com](https://console.groq.com/) and create a free developer account.
2. Go to **API Keys** in the sidebar.
3. Click **Create API Key**, name it `isayscribe`, and copy the generated key (it starts with `gsk_`).

### Step 2: Build the iOS Shortcut
Open the built-in **Shortcuts** app on your iPhone, click the **+** icon in the top-right to create a new shortcut, name it **"isayscribe"**, and assemble these exact actions:

#### 1. Record the Audio
- Add the **Record Audio** action.
- Set configuration to: Record `Audio` with `Microphone`. Stop Recording: `On Tap` (or `On Short Tap`).

#### 2. Send to Groq Whisper (Speech-to-Text)
- Add the **Get Contents of URL** action.
- Set the URL to: `https://api.groq.com/openai/v1/audio/transcriptions`
- Tap **Show More** to configure:
  - **Method**: `POST`
  - **Headers**:
    - `Authorization`: `Bearer YOUR_GROQ_API_KEY` (Paste your key here)
  - **Request Body**: `Form`
    - Add Key `file`: Choose type **File** and select the output of **Recorded Audio** from the magic variables list.
    - Add Key `model`: Choose type **Text** and write `whisper-large-v3`.
    - Add Key `response_format`: Choose type **Text** and write `json`.

#### 3. Extract the Transcript
- Add the **Get Value from Dictionary** action.
- Set the key to `text` in `Contents of URL`. This isolates your raw transcript.

#### 4. Send to Llama-3 (Brain-Dump Formatter)
- Add the **Get Contents of URL** action.
- Set the URL to: `https://api.groq.com/openai/v1/chat/completions`
- Tap **Show More** to configure:
  - **Method**: `POST`
  - **Headers**:
    - `Authorization`: `Bearer YOUR_GROQ_API_KEY`
    - `Content-Type`: `application/json`
  - **Request Body**: `JSON`
    - Add Key `model`: `llama-3.3-70b-specdec`
    - Add Key `messages`: (Choose **Array** type)
      - **Item 1 (System Prompt)**: Choose **Dictionary** type:
        - Key `role`: `system`
        - Key `content`: [Copy and paste the exact system prompt from prompt.txt in this repository]
      - **Item 2 (User Input)**: Choose **Dictionary** type:
        - Key `role`: `user`
        - Key `content`: Select the transcript output from the previous dictionary step.

#### 5. Parse and Save the Note
- Add the **Get Value from Dictionary** action.
- Set the key path to `choices.1.message.content` in `Contents of URL`.
- Add the **Create Note** action (to save it directly inside Apple Notes) or **Create File** action (to save it inside your iCloud Obsidian folder as a `.md` file), and pass the output of this final dictionary step as the note content.

---

## Trigger Options

To get the real "Plaud/Pocket AI" immediate hardware feel, configure how you trigger the shortcut:
- **Action Button (iPhone 15 Pro / 16 / 16 Pro)**: Go to **Settings > Action Button**, select **Shortcut**, and choose `isayscribe`. Press and hold your physical side button to instantly start recording your thoughts.
- **Back Tap**: Go to **Settings > Accessibility > Touch > Back Tap**. Assign `isayscribe` to Double Tap or Triple Tap.
- **Home Screen / Lock Screen Widget**: Add a native Shortcuts widget directly to your Home Screen or Lock Screen for one-tap capture.

---

## Customizing the Output

Want to tweak how `isayscribe` formats your brain dumps? Simply modify the system prompt stored in your Shortcut's Step 4. You can instruct the model to write in different languages, prioritize code blocks, organize thoughts into tables, or automatically match your specific meeting note styles.

---

## License

This project is open-source and licensed under the MIT License. Feel free to clone it, modify it, share it, and help others escape unnecessary hardware subscriptions.
