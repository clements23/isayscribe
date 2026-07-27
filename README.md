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

- **Supported Devices**: iPhone 11 and newer (requires iOS 16+)
- **OS**: iOS 16.0 or later
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

### Step 2: Install the Shortcut

**One tap. Done.**

1. On your iPhone, open this page in Safari.
2. Tap the download link below.
3. When prompted, enter your Groq API key (starts with `gsk_`).
4. Tap **Add Shortcut**.

👉 **[Download isayscribe.shortcut](isayscribe.shortcut)**

That's it. The shortcut is now in your Shortcuts app, fully configured.

> **What's inside:** Record Audio → Groq Whisper transcription → Llama-3.3 structured formatting → Apple Notes. Open it in the Shortcuts app anytime to inspect or modify.

---

## Trigger Options

The whole point of isayscribe is speed. Your ideas arrive in seconds. Your capture method should too.

Below are three trigger methods, ordered by how fast they get you from thought to recording. iPhone 11-14 users should use Method 2 (Back Tap) or Method 3 (Widget). iPhone 15 Pro and 16 Pro users have all three.

---

### Method 1: Action Button (iPhone 15 Pro / 16 / 16 Pro Only)

This is the fastest possible trigger. You press a physical button and start talking. No screen interaction required.

1. Open **Settings**.
2. Scroll down and tap **Action Button**.
3. Swipe left until you see the **Shortcuts** option (the icon looks like two colored squares).
4. Tap the shortcut selector below it and choose **isayscribe** from the list.
5. Done. Now press and hold the Action Button on the left side of your iPhone to instantly start recording.

---

### Method 2: Back Tap (iPhone 11 and Newer)

Back Tap turns the back of your iPhone into a hidden button. Double-tap or triple-tap the back glass to launch isayscribe from anywhere - even when your phone is locked.

This is the best trigger method for iPhone 11-14 users who do not have an Action Button.

#### Step-by-Step Setup:

1. Open **Settings**.
2. Tap **Accessibility**.
3. Under the "Physical and Motor" section, tap **Touch**.
4. Scroll all the way to the bottom and tap **Back Tap**.
5. Choose either **Double Tap** or **Triple Tap**.
   - **Double Tap** is faster but may trigger accidentally when you set your phone down.
   - **Triple Tap** is more deliberate. Recommended if you carry your phone in your hand a lot.
6. Scroll through the list of available actions and find **isayscribe** under the Shortcuts section.
7. Tap it to assign it.
8. Exit Settings. Your trigger is now live.

#### How to Use It:
- With your iPhone unlocked or locked, firmly tap the back glass twice (or three times) with your finger.
- isayscribe will launch immediately and start recording.
- Tap the screen when you are done speaking. Your note will appear in Apple Notes or Obsidian within seconds.

#### Troubleshooting Back Tap:
- If nothing happens when you tap, try tapping harder. Thick cases reduce sensitivity.
- If it triggers too often, switch from Double Tap to Triple Tap.
- If it never works, go back to Settings > Accessibility > Touch > Back Tap and make sure isayscribe is still assigned.

---

### Method 3: Home Screen & Lock Screen Widget (iPhone 11 and Newer)

If Back Tap feels unreliable with your phone case, use a widget instead. One visible tap on your screen is all it takes.

#### Add to Home Screen:
1. Go to your Home Screen.
2. Press and hold on any empty space until the apps start wiggling.
3. Tap the **+** button in the top-left corner (or top-right, depending on your iOS version).
4. Search for **Shortcuts** in the widget gallery.
5. Choose the **single shortcut** widget size (the smallest square).
6. Tap **Add Widget**.
7. While still in wiggle mode, tap the widget to configure it.
8. Select **isayscribe** from the shortcut list.
9. Tap outside the widget to exit configuration.
10. Drag the widget wherever you want it on your Home Screen.
11. Tap **Done** in the top-right corner.

#### Add to Lock Screen (iOS 16+):
1. Wake your iPhone but do not unlock it. Stay on the Lock Screen.
2. Press and hold on the Lock Screen until the customization menu appears.
3. Tap **Customize** at the bottom.
4. Tap the **Lock Screen** preview.
5. Tap the area **below the clock** where widgets live (this is the widget strip).
6. In the widget picker that slides up, scroll down and find **Shortcuts**.
7. Tap it, then tap the single shortcut widget.
8. Tap the widget to select it, then choose **isayscribe** from the list.
9. Tap **Done** in the top-right corner, then tap the Lock Screen preview to confirm.
10. Your Lock Screen now has a one-tap isayscribe button visible every time you pick up your phone.

#### How to Use It:
- From the Lock Screen, tap the isayscribe widget. Your phone will unlock, launch the shortcut, and start recording immediately.
- From the Home Screen, same thing - one tap and you are recording.

---

## Customizing the Output

Want to tweak how `isayscribe` formats your brain dumps? Simply modify the system prompt stored in your Shortcut's Step 4. You can instruct the model to write in different languages, prioritize code blocks, organize thoughts into tables, or automatically match your specific meeting note styles.

---

## License

This project is open-source and licensed under the MIT License. Feel free to clone it, modify it, share it, and help others escape unnecessary hardware subscriptions.
