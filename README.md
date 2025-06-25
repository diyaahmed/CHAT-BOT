# CHAT-BOT
# Lulu Chatbot - Instruction Manual

## Overview
Lulu is a friendly desktop chatbot that assists with basic tasks like answering greetings, providing the date, and fetching online information via Google search.

## Getting Started
1. Run the program by executing: python chatBot.py
2. Enter your name when prompted (e.g., "Emily" or "My name is Emily")
3. Begin chatting!

## Features

### Basic Interaction
- Greetings: Responds to "hi" or "hello"
- Personalization: Remembers your name throughout the session
- Farewells: Recognizes "bye" to end conversations

### Information Services
1. Date Information:
   - Ask: "What's today's date?" or "date"
   - Response: Displays current date (e.g., "June 26, 2025")

2. Web Search:
   - Format: "Give me information about [topic]" or "link for [topic]"
   - Example: "Give me information about Python programming"
   - Action: Provides clickable Google search link

### Teacher Office Information
- Pre-loaded office locations (manually added in code)
- Ask: "Where is Professor [Name]'s office?"

## Technical Requirements

### For Computers
- Python 3.x installed
- Required modules (pre-installed with Python):
  - tkinter
  - datetime
  - webbrowser
  - random

### For Mobile Devices
1. Android:
   - Install Pydroid 3 from Play Store
   - Copy-paste code and run

2. iOS:
   - Install Pythonista from App Store
   - Import and run the script

## Troubleshooting
- Links not opening: Check internet connection
- No response: Ensure messages end with Enter key or Send button
- Reset chat: Close and reopen the program

## Notes
- Chat history clears when program closes
- All search queries open in default web browser
- Teacher office info requires manual code updates

## Sample Conversations
User: My name is Alex
Lulu: Nice to meet you, Alex! How can I help you today?

User: What's today's date?
Lulu: Today's date is June 26, 2025.

User: Give me information about quantum computing
Lulu: Here's a link to help you find more information: [clickable Google search link]

User: Bye
Lulu: Goodbye, Alex! Have a wonderful day!
