# Version History

## [2.0.0] - 2026-07-27
- Complete rewrite: replaced 5-step manual Shortcut build with a signed `.shortcut` file. One download, one tap, enter API key, done.
- Added `build_shortcut.py` for regenerating the shortcut file from source components.
- Import questions prompt for API key on first open -- no manual editing needed.

## [1.2.1] - 2026-07-27
- Rewritten Shortcut build steps as clear Key/Value tables showing exactly what goes in the left field (Key) and right field (Type + Value) for every header, body parameter, dictionary, and array item. Eliminates ambiguity for first-time Shortcut builders.

## [1.2.0] - 2026-07-27 (Phase 2)
- Complete Back Tap setup guide with step-by-step instructions, troubleshooting, and sensitivity tips.
- Complete Lock Screen and Home Screen widget setup guide with visual navigation paths.
- Rewritten Trigger Options section as a full tutorial covering all three trigger methods for iPhone 11+.

## [1.1.0] - 2026-07-27 (Phase 2)
- Added official Prompt Presets directory (`prompts/`) with specialized templates for Meeting Minutes (`meeting-minutes.txt`) and Technical Brainstorms (`code-brainstorm.txt`).
- Expanded customization documentation.

## [1.0.0] - 2026-07-27
- Initial release of isayscribe.
- Supported on iPhone 11 and newer (iOS 16.0+).
- Integrated Groq API (Whisper + Llama-3.3-70B) for free, high-speed transcription and summarization.
- Support for direct Apple Notes/Obsidian saving.
