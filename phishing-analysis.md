# Phishing Email Analysis Project

### 📌 Project Overview
This project documents my analysis of 10 emails in the Google Phishing Quiz. I identified phishing attempts by analyzing sender domains, links, urgency, and red flags.

### 📊 Quiz Score
- **Score:** 9/10
- **Date:** 19 July 2026
- **Platform:** Google Phishing Quiz

### 🔍 Example 1: Phishing Email

**Email Subject:** "Luke Johnson shared a document"

**Sender:** luke.json8000@gmail.com

**Red Flags:**
- Sender name doesn't match email (Luke Johnson vs luke.json)
- Unknown sender sharing a Google Doc
- No personal greeting

**Verdict:** ❌ Phishing

### 🔍 Example 2: Phishing Email

**Email Subject:** "Coca-Cola - ANSWER AND WIN!"

**Sender:** email_...@opmajvpqjcg.georgs-faescht.com

**Red Flags:**
- Fake domain (not coca-cola.com)
- "Free" offer too good to be true
- Urgent call to action: "GET STARTED NOW"

**Verdict:** ❌ Phishing

### 🔍 Example 3: Phishing Email

**Email Subject:** "Someone has your password"

**Sender:** no-reply@google.support

**Red Flags:**
- Fake sender domain (google.support is not Google)
- Generic greeting ("Hi,")
- Urgent scare tactic
- "The Mail Team" sign-off (not Google)

**Verdict:** ❌ Phishing

### 🔍 Example 4: Phishing Email

**Email Subject:** "Free Pixel 7 Pro – confirmation interview"

**Sender:** pixel-giveaway@google.com

**Red Flags:**
- Unsolicited giveaway (didn't enter any competition)
- "HACKER" listed as a guest
- Link likely leads to fake login page

**Verdict:** ❌ Phishing


### 🔍 Example 5: Legitimate Email

**Email Subject:** "Your Dropbox is full"

**Sender:** no-reply@dropboxmail.com

**Why It's Legit:**
- Sender domain is official (dropboxmail.com)
- Links go to dropbox.com
- No urgent scare tactics
- No request for personal info

**Verdict:** ✅ Legitimate

### 🌳 Phishing Triage Decision Tree
              ┌─────────────────────────┐
              │   Email Received        │
              └──────────┬──────────────┘
                         │
              ┌──────────▼──────────────┐
              │   Check Red Flags       │
              │   (11-point list)       │
              └──────────┬──────────────┘
                         │
      ┌──────────────────┼──────────────────┐
      │                  │                  │
┌─────▼─────┐     ┌──────▼──────┐    ┌──────▼──────┐
│  0 Flags  │     │  1-3 Flags  │    │  4+ Flags   │
└─────┬─────┘     └──────┬──────┘    └──────┬──────┘
      │                  │                  │
┌─────▼─────┐     ┌──────▼──────┐    ┌──────▼──────┐
│   SAFE    │     │ SUSPICIOUS  │    │ MALICIOUS   │
│           │     │             │    │             │
│ • Close   │     │ • Warn User │    │ • Block     │
│ • Delete  │     │ • Monitor   │    │ • Escalate  │
└───────────┘     └─────────────┘    └─────────────┘

### 📋 Key Red Flags I Learned
| 1 | Fake sender domain | google.support instead of google.com |
| 2 | Suspicious links | Link goes to a different domain when hovered |
| 3 | Urgent language | "Act now or your account will be locked!" |
| 4 | Generic greetings | "Dear Customer" instead of your name |
| 5 | Too good to be true | Free offers, giveaways, prizes |
| 6 | Fake phone numbers | Calls asking for personal info |
| 7 | Scare tactics | "Your account has been compromised" |
| 8 | Grammar/spelling errors | Misspelled words |
| 9 | Requests for personal info | Asking for passwords or OTPs |
| 10 | Unknown senders | People you don't know sharing documents |
| 11 | Contradicting instructions | "Ignore" vs "Respond with CANCEL" |


### 💡 Key Takeaways

- **Always check the sender domain** — a single letter off means it's fake
- **Hover over links** before clicking — the real URL is often hidden
- **Legitimate companies** use your full name in security emails
- **Urgency and fear** are the most common phishing tactics
- **If it's too good to be true, it probably is**
- **Never share your OTPs or passwords** with anyone

