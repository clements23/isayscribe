#!/usr/bin/env python3
"""Generate isayscribe.shortcut plist from components."""
import plistlib
import uuid
import os

BASE = "/Users/clementsemerson/isayscribe"

# Read the system prompt from prompt.txt
with open(os.path.join(BASE, "prompt.txt"), "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

# Generate action UUIDs
uuids = [str(uuid.uuid4()) for _ in range(6)]

def action_ref(action_uuid, output_name):
    """Create a variable reference to an action's output."""
    return {
        "OutputUUID": action_uuid,
        "OutputName": output_name,
        "Type": "ActionOutput",
    }

def text_attr(value):
    """Wrap a plain text value for JSON/form body."""
    return {
        "Value": {"string": value},
        "WFSerializationType": "WFTextTokenString",
    }

def file_attr(action_uuid, output_name):
    """Wrap a file reference for form body."""
    return {
        "Value": action_ref(action_uuid, output_name),
        "WFSerializationType": "WFFileTokenAttachment",
    }

def text_ref_attr(action_uuid, output_name):
    """Wrap a text output reference."""
    return {
        "Value": action_ref(action_uuid, output_name),
        "WFSerializationType": "WFTextTokenAttachment",
    }

API_KEY_PLACEHOLDER = "Bearer YOUR_GROQ_API_KEY_HERE"

actions = []

# --- 0: Record Audio ---
actions.append({
    "WFWorkflowActionIdentifier": "is.workflow.actions.recordaudio",
    "WFWorkflowActionParameters": {
        "UUID": uuids[0],
    },
})

# --- 1: POST to Whisper ---
actions.append({
    "WFWorkflowActionIdentifier": "is.workflow.actions.getcontentsofurl",
    "WFWorkflowActionParameters": {
        "UUID": uuids[1],
        "WFURL": "https://api.groq.com/openai/v1/audio/transcriptions",
        "WFHTTPMethod": "POST",
        "WFHTTPBodyType": "Form",
        "WFHTTPHeaders": {"Authorization": API_KEY_PLACEHOLDER},
        "WFFormValues": {
            "file": file_attr(uuids[0], "Recorded Audio"),
            "model": text_attr("whisper-large-v3"),
            "response_format": text_attr("json"),
        },
    },
})

# --- 2: Get "text" from Whisper response ---
actions.append({
    "WFWorkflowActionIdentifier": "is.workflow.actions.getvalueforkey",
    "WFWorkflowActionParameters": {
        "UUID": uuids[2],
        "WFDictionaryKey": "text",
        "WFInput": action_ref(uuids[1], "Contents of URL"),
    },
})

# --- 3: POST to Llama-3 chat completions ---
actions.append({
    "WFWorkflowActionIdentifier": "is.workflow.actions.getcontentsofurl",
    "WFWorkflowActionParameters": {
        "UUID": uuids[3],
        "WFURL": "https://api.groq.com/openai/v1/chat/completions",
        "WFHTTPMethod": "POST",
        "WFHTTPBodyType": "JSON",
        "WFHTTPHeaders": {
            "Authorization": API_KEY_PLACEHOLDER,
            "Content-Type": "application/json",
        },
        "WFJSONValues": {
            "model": text_attr("llama-3.3-70b-specdec"),
            "messages": {
                "Value": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": text_ref_attr(uuids[2], "Dictionary Value"),
                    },
                ],
                "WFSerializationType": "WFArrayTokenAttachment",
            },
        },
    },
})

# --- 4: Get "choices.1.message.content" from Llama response ---
actions.append({
    "WFWorkflowActionIdentifier": "is.workflow.actions.getvalueforkey",
    "WFWorkflowActionParameters": {
        "UUID": uuids[4],
        "WFDictionaryKey": "choices.1.message.content",
        "WFInput": action_ref(uuids[3], "Contents of URL"),
        "WFGetValueFromDictionaryKeyPath": True,
    },
})

# --- 5: Create Note ---
actions.append({
    "WFWorkflowActionIdentifier": "is.workflow.actions.createnote",
    "WFWorkflowActionParameters": {
        "UUID": uuids[5],
        "WFNoteContent": text_ref_attr(uuids[4], "Dictionary Value"),
    },
})

# Build full workflow plist
workflow = {
    "WFWorkflowClientVersion": "900.5.1",
    "WFWorkflowClientRelease": "2.1",
    "WFWorkflowIcon": {
        "WFWorkflowIconStartColor": 4282601983,      # Blue
        "WFWorkflowIconGlyphNumber": 61440,           # Microphone glyph
    },
    "WFWorkflowImportQuestions": [
        {
            "Category": "Parameter",
            "ActionIndex": 1,
            "ParameterKey": "WFHTTPHeaders",
            "Text": "Your Groq API Key (starts with gsk_)",
            "DefaultValue": "",
        },
        {
            "Category": "Parameter",
            "ActionIndex": 3,
            "ParameterKey": "WFHTTPHeaders",
            "Text": "Your Groq API Key (same as above)",
            "DefaultValue": "",
        },
    ],
    "WFWorkflowTypes": ["NCWidget", "WatchKit", "ActionExtension"],
    "WFWorkflowInputContentItemClasses": [
        "WFAppStoreAppContentItem", "WFArticleContentItem",
        "WFContactContentItem", "WFDateContentItem",
        "WFEmailAddressContentItem", "WFGenericFileContentItem",
        "WFImageContentItem", "WFiTunesProductContentItem",
        "WFLocationContentItem", "WFDCMapsLinkContentItem",
        "WFAVAssetContentItem", "WFPDFContentItem",
        "WFPhoneNumberContentItem", "WFRichTextContentItem",
        "WFSafariWebPageContentItem", "WFStringContentItem",
        "WFURLContentItem",
    ],
    "WFWorkflowActions": actions,
    "WFWorkflowMinimumClientVersion": 900,
}

# Write XML plist
out_path = os.path.join(BASE, "isayscribe.shortcut")
with open(out_path, "wb") as f:
    plistlib.dump(workflow, f, fmt=plistlib.FMT_XML)

print(f"Generated: {out_path}")
print(f"Actions: {len(actions)}")
for i, uid in enumerate(uuids):
    print(f"  [{i}] {uid}")
