# Version History

## [2.0.2] - 2026-07-27
- **VALIDATOR-PASSING BUILD**: Fixed all shortcuts-playground validator errors.
- Switched to correct action identifier `is.workflow.actions.downloadurl` (not `getcontentsofurl`).
- Correct `WFDictionaryFieldValue` serialization for `WFHTTPHeaders`, `WFJSONValues`, `WFFormValues`.
- Proper `WFItemType = 5` file attachment format with `WFTokenAttachmentParameterState`.
- `getvalueforkey` now uses explicit `WFInput` with `WFTextTokenAttachment`.
- Create Note uses `com.apple.mobilenotes.SharingExtension` (ToolKit AppIntent) with `AppIntentDescriptor`, `name`, and `content` keys.
- Added 3 Comment blocks with Shortcuts Playground prompt text and UI-wording wiring notes.
- Removed unused `WFWorkflowInputContentItemClasses`.
- Build now converts to binary plist before signing to fix `shortcuts sign` rejection.
- **CRITICAL FIX**: Changed action identifier from `is.workflow.actions.getcontentsofurl` to `is.workflow.actions.downloadurl`. Previous version showed "Unknown Action" on iPhone 11+ iOS 16/17.
- Fixed `WFHTTPHeaders`, `WFJSONValues`, and `WFFormValues` to use the proper `WFDictionaryFieldValue` + `WFDictionaryFieldValueItems` serialization. The flat dict format from v2.0.0 was rejected by iOS.
- Added file upload format for Form body: `WFItemType = 5` wrapped in `WFTokenAttachmentParameterState` with inner `WFTextTokenAttachment` reference to the Recorded Audio action output.
- Switched dot-notation key path from `WFGetValueFromDictionaryKeyPath` boolean flag to `WFDictionaryKey` string with dot notation (e.g. `choices.1.message.content`).
- Added required network settings: `WFAllowsCellularAccess`, `WFAllowsRedirects`, `WFIgnoreCookies`, `WFTimeout`.
- UUIDs now generated in uppercase as required by Shortcuts validators.
- Bumped `WFWorkflowClientVersion` to `2700.0.4`.

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
