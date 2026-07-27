#!/usr/bin/env python3
"""Generate isayscribe.shortcut plist using the verified correct format."""
import plistlib
import uuid
import os

BASE = "/Users/clementsemerson/isayscribe"

# Read the system prompt from prompt.txt
with open(os.path.join(BASE, "prompt.txt"), "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

# Generate uppercase UUIDs
uuids = [str(uuid.uuid4()).upper() for _ in range(6)]


def uuid_str():
    return str(uuid.uuid4()).upper()


# --- Helpers for the WFDictionaryFieldValue serialization ---

def wf_key(name):
    """A key cell inside WFDictionaryFieldValueItems."""
    return {
        "Value": {"string": name},
        "WFSerializationType": "WFTextTokenString",
    }


def wf_text_value(text):
    """A text value cell (WFItemType 0)."""
    return {
        "Value": {"string": text},
        "WFSerializationType": "WFTextTokenString",
    }


def wf_string_value(text):
    """Wrap a plain string as WFDictionaryFieldValue."""
    return {
        "Value": {"WFDictionaryFieldValueItems": [
            {"UUID": uuid_str(), "WFKey": wf_key("string"), "WFItemType": 0, "WFValue": wf_text_value(text)}
        ]},
        "WFSerializationType": "WFDictionaryFieldValue",
    }


def wf_file_ref(source_uuid, output_name="Recorded Audio"):
    """Reference a previous action's file output."""
    return {
        "OutputUUID": source_uuid,
        "OutputName": output_name,
        "Type": "ActionOutput",
    }


def wf_text_ref(source_uuid, output_name="Dictionary Value"):
    """Reference a previous action's text output as a text token attachment."""
    return {
        "Value": {
            "OutputUUID": source_uuid,
            "OutputName": output_name,
            "Type": "ActionOutput",
        },
        "WFSerializationType": "WFTextTokenAttachment",
    }


def wf_form_value_text(name, text):
    """A text field inside WFFormValues (WFItemType 0)."""
    return {
        "UUID": uuid_str(),
        "WFKey": wf_key(name),
        "WFItemType": 0,
        "WFValue": wf_text_value(text),
    }


def wf_form_value_file(name, source_uuid):
    """A file field inside WFFormValues (WFItemType 5).

    Per SKILL.md: file fields must wrap the file reference in
    WFTokenAttachmentParameterState with an inner WFTextTokenAttachment.
    """
    return {
        "UUID": uuid_str(),
        "WFKey": wf_key(name),
        "WFItemType": 5,
        "WFValue": {
            "Value": {
                "Type": "ActionOutput",
                "OutputUUID": source_uuid,
                "OutputName": "Recorded Audio",
            },
            "WFSerializationType": "WFTokenAttachmentParameterState",
        },
    }


def wf_form_dict(items):
    """Build a WFDictionaryFieldValue for WFFormValues."""
    return {
        "Value": {"WFDictionaryFieldValueItems": items},
        "WFSerializationType": "WFDictionaryFieldValue",
    }


def wf_headers_dict(headers):
    """Build WFHTTPHeaders as WFDictionaryFieldValue."""
    items = [
        {
            "UUID": uuid_str(),
            "WFKey": wf_key(k),
            "WFItemType": 0,
            "WFValue": wf_text_value(v),
        }
        for k, v in headers.items()
    ]
    return {
        "Value": {"WFDictionaryFieldValueItems": items},
        "WFSerializationType": "WFDictionaryFieldValue",
    }


def wf_json_messages(system_content, user_source_uuid):
    """Build the messages array for the chat completions JSON body."""
    sys_item = {
        "WFItemType": 1,
        "WFValue": {
            "Value": {
                "WFDictionaryFieldValueItems": [
                    {
                        "UUID": uuid_str(),
                        "WFKey": wf_key("role"),
                        "WFItemType": 0,
                        "WFValue": wf_text_value("system"),
                    },
                    {
                        "UUID": uuid_str(),
                        "WFKey": wf_key("content"),
                        "WFItemType": 0,
                        "WFValue": wf_text_value(system_content),
                    },
                ]
            },
            "WFSerializationType": "WFDictionaryFieldValue",
        },
    }
    user_item = {
        "WFItemType": 1,
        "WFValue": {
            "Value": {
                "WFDictionaryFieldValueItems": [
                    {
                        "UUID": uuid_str(),
                        "WFKey": wf_key("role"),
                        "WFItemType": 0,
                        "WFValue": wf_text_value("user"),
                    },
                    {
                        "UUID": uuid_str(),
                        "WFKey": wf_key("content"),
                        "WFItemType": 0,
                        "WFValue": {
                            "Value": {
                                "OutputUUID": user_source_uuid,
                                "OutputName": "Dictionary Value",
                                "Type": "ActionOutput",
                            },
                            "WFSerializationType": "WFTextTokenAttachment",
                        },
                    },
                ]
            },
            "WFSerializationType": "WFDictionaryFieldValue",
        },
    }
    return [sys_item, user_item]


def wf_json_dict(items):
    """Build WFDictionaryFieldValue for WFJSONValues."""
    return {
        "Value": {"WFDictionaryFieldValueItems": items},
        "WFSerializationType": "WFDictionaryFieldValue",
    }


# --- Build the actions ---

API_KEY_PLACEHOLDER = "Bearer YOUR_GROQ_API_KEY_HERE"
HEADERS = {"Authorization": API_KEY_PLACEHOLDER}
JSON_HEADERS = {"Authorization": API_KEY_PLACEHOLDER, "Content-Type": "application/json"}

actions = []

# --- Action 0: Record Audio ---
actions.append({
    "WFWorkflowActionIdentifier": "is.workflow.actions.recordaudio",
    "WFWorkflowActionParameters": {
        "UUID": uuids[0],
    },
})

# --- Action 1: POST to Whisper (Form body with file upload) ---
actions.append({
    "WFWorkflowActionIdentifier": "is.workflow.actions.downloadurl",
    "WFWorkflowActionParameters": {
        "UUID": uuids[1],
        "WFURL": "https://api.groq.com/openai/v1/audio/transcriptions",
        "WFHTTPMethod": "POST",
        "WFHTTPHeaders": wf_headers_dict(HEADERS),
        "WFHTTPBodyType": "Form",
        "WFFormValues": wf_form_dict([
            wf_form_value_file("file", uuids[0]),
            wf_form_value_text("model", "whisper-large-v3"),
            wf_form_value_text("response_format", "json"),
        ]),
        "ShowHeaders": True,
        "WFAllowsCellularAccess": 1,
        "WFAllowsRedirects": 1,
        "WFIgnoreCookies": 0,
        "WFTimeout": 60,
    },
})

# --- Action 2: Get "text" from Whisper response ---
actions.append({
    "WFWorkflowActionIdentifier": "is.workflow.actions.getvalueforkey",
    "WFWorkflowActionParameters": {
        "UUID": uuids[2],
        "WFDictionaryKey": "text",
        "WFInput": {
            "Value": {
                "OutputUUID": uuids[1],
                "OutputName": "Contents of URL",
                "Type": "ActionOutput",
            },
            "WFSerializationType": "WFTextTokenAttachment",
        },
    },
})

# --- Action 3: POST to Llama-3 chat completions (JSON body) ---
actions.append({
    "WFWorkflowActionIdentifier": "is.workflow.actions.downloadurl",
    "WFWorkflowActionParameters": {
        "UUID": uuids[3],
        "WFURL": "https://api.groq.com/openai/v1/chat/completions",
        "WFHTTPMethod": "POST",
        "WFHTTPHeaders": wf_headers_dict(JSON_HEADERS),
        "WFHTTPBodyType": "JSON",
        "WFJSONValues": wf_json_dict([
            {
                "UUID": uuid_str(),
                "WFKey": wf_key("model"),
                "WFItemType": 0,
                "WFValue": wf_text_value("llama-3.3-70b-specdec"),
            },
            {
                "UUID": uuid_str(),
                "WFKey": wf_key("messages"),
                "WFItemType": 2,
                "WFValue": {
                    "Value": wf_json_messages(SYSTEM_PROMPT, uuids[2]),
                    "WFSerializationType": "WFArrayParameterState",
                },
            },
        ]),
        "ShowHeaders": True,
        "WFAllowsCellularAccess": 1,
        "WFAllowsRedirects": 1,
        "WFIgnoreCookies": 0,
        "WFTimeout": 60,
    },
})

# --- Action 4: Get "choices.1.message.content" from Llama response ---
actions.append({
    "WFWorkflowActionIdentifier": "is.workflow.actions.getvalueforkey",
    "WFWorkflowActionParameters": {
        "UUID": uuids[4],
        "WFDictionaryKey": "choices.1.message.content",
        "WFInput": {
            "Value": {
                "OutputUUID": uuids[3],
                "OutputName": "Contents of URL",
                "Type": "ActionOutput",
            },
            "WFSerializationType": "WFTextTokenAttachment",
        },
    },
})

# --- Action 5: Create Note ---
actions.append({
    "WFWorkflowActionIdentifier": "is.workflow.actions.createnote",
    "WFWorkflowActionParameters": {
        "UUID": uuids[5],
        "WFNoteContent": {
            "Value": {
                "OutputUUID": uuids[4],
                "OutputName": "Dictionary Value",
                "Type": "ActionOutput",
            },
            "WFSerializationType": "WFTextTokenAttachment",
        },
    },
})

# --- Build full workflow plist ---
workflow = {
    "WFWorkflowClientVersion": "2700.0.4",
    "WFWorkflowClientRelease": "2.1",
    "WFWorkflowHasOutputFallback": False,
    "WFWorkflowHasShortcutInputVariables": True,
    "WFWorkflowIcon": {
        "WFWorkflowIconStartColor": 4282601983,
        "WFWorkflowIconGlyphNumber": 61440,
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
    "WFWorkflowMinimumClientVersionString": "900",
    "WFWorkflowOutputContentItemClasses": [],
    "WFWorkflowName": "isayscribe",
    "WFWorkflowTypes": ["NCWidget", "WatchKit", "ActionExtension"],
}

# Write XML plist
out_path = os.path.join(BASE, "isayscribe.shortcut")
with open(out_path, "wb") as f:
    plistlib.dump(workflow, f, fmt=plistlib.FMT_XML)

print(f"Generated: {out_path}")
print(f"Actions: {len(actions)}")
for i, uid in enumerate(uuids):
    print(f"  [{i}] {uid}")
