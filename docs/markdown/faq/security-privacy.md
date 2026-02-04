# Security & Privacy FAQ

Security, privacy, and data protection in PyGPT.

## 🔐 Is PyGPT Secure?

### Short Answer: **Yes, but understand the basics**

- ✅ PyGPT itself is secure (open source, auditable)
- ⚠️ Your data security depends on:
  - Where you store it (local vs cloud)
  - Which AI provider you use
  - Your API key protection

---

## 💾 Where Is My Data Stored?

### Local Storage (Default)

```
~/.pygpt/data/
├── conversations/    # Chat history
├── attachments/      # Uploaded files
└── embeddings/       # Vector store
```

**Security:**
- ✅ Only on your computer
- ✅ Not sent anywhere by default
- ✅ Only you can access (with system access)

### Cloud Storage (When Using APIs)

**When you use OpenAI/Google/Anthropic:**
- Messages sent to their servers
- Used to generate response
- May be used for training (depends on provider)
- Subject to provider's privacy policy

**What gets sent:**
- Your input text/questions
- Attached files
- Context from conversation

**What doesn't get sent:**
- Your settings
- Your stored conversations
- Your chat history (unless you send it)

---

## 🔑 API Key Security

### How API Keys Work

- Authenticates you to provider
- Grants access to use their API
- Like a password - don't share!

### Protecting Your Keys

**✅ DO:**
- Store in environment variables
- Use separate key per device
- Rotate keys regularly
- Monitor API usage
- Use read-only keys when available

**❌ DON'T:**
- Commit keys to Git/GitHub
- Share in emails or chat
- Store in plain text
- Use production key for testing
- Leave in browser history
- Post in forums/Discord

### If Key is Leaked

1. Immediately delete compromised key
2. Generate new key
3. Update all applications
4. Monitor account for suspicious activity
5. Check usage logs

---

## 🚨 Data Privacy by Provider

### Google Gemini

**Free Tier:**
- May be used for training
- Read their [privacy policy](https://policies.google.com/privacy)

**Paid Tier:**
- Not used for training
- Enterprise options available
- VertexAI for full control

### OpenAI

**Default:**
- May train on conversations
- Disable in account settings
- API calls: depends on tier

**Business Tier:**
- Enhanced privacy guarantees
- No training on conversations

### Anthropic Claude

**Their Policy:**
- Messages not used for training (by default)
- Good privacy focus
- Check current [privacy policy](https://www.anthropic.com/privacy)

### DeepSeek & Mistral

- Check their privacy policies
- Generally good privacy
- Use local Ollama if concerned

### Ollama (Local)

**100% Private:**
- Runs on your computer
- Nothing sent to servers
- Complete privacy
- Only you see data

---

## 📎 File Security

### When You Attach Files

**With Cloud APIs:**
1. File sent to API provider
2. Analyzed to answer your question
3. May be retained (check policy)
4. Could be used for training

**Sensitive Files:**
- ❌ Don't upload to cloud APIs
- ✅ Use local Ollama instead
- ✅ Or ask without uploading
- ✅ Use summarization locally first

### File Types to Avoid

- Financial records
- Medical documents
- Personal identification
- Passwords/secrets
- Confidential business data

---

## 🛡️ Encryption

### At Rest (Stored on Disk)

**PyGPT encryption:**
- Optional full-disk encryption
- Or use OS-level encryption
- Settings → Security → Encrypt

**Recommended:**
- Windows: BitLocker
- Linux: LUKS
- macOS: FileVault

### In Transit (Network)

**PyGPT:**
- Uses HTTPS/SSL by default
- Secure connection to APIs
- Encrypted network transmission
- ✅ Secure

---

## 👤 Privacy Best Practices

### Best Practice 1: Use Local Models

```
For maximum privacy:
1. Use Ollama (local)
2. Your computer only
3. No data leaves your machine
4. 100% private
```

### Best Practice 2: Separate Accounts

```
For different use cases:
1. Personal account
2. Work account  
3. Testing account
4. Each with own API key
```

### Best Practice 3: Monitor Usage

```
Regularly check:
1. API usage dashboard
2. Recent API calls
3. Unexpected activity
4. Spending spikes
```

### Best Practice 4: Use VPN

```
If concerned about ISP tracking:
1. Enable VPN
2. Routes through secure server
3. ISP can't see API calls
4. Added privacy layer
```

### Best Practice 5: Minimize Sensitive Data

```
When sharing prompts:
1. Remove names
2. Anonymize examples
3. Don't include passwords
4. Don't include personal info
```

---

## ⚠️ Common Vulnerabilities

### Vulnerability 1: Leaked API Key

**Risk:** Anyone can use your key
**Solution:**
- Store securely
- Rotate regularly
- Monitor usage
- Set usage limits

### Vulnerability 2: Open Wifi

**Risk:** Network snooping
**Solution:**
- Use VPN
- Avoid sensitive data on open wifi
- Use HTTPS only (PyGPT does this)

### Vulnerability 3: Shoulder Surfing

**Risk:** Someone sees your screen
**Solution:**
- Privacy screen filter
- Use Ctrl+L to clear chat
- Be aware of surroundings
- Lock when away

### Vulnerability 4: Account Takeover

**Risk:** Someone accesses your account
**Solution:**
- Strong password
- Two-factor authentication
- Monitor account activity
- Use separate recovery email

---

## 🔍 Data Deletion

### Delete Conversations

1. Right-click chat
2. Select "Delete"
3. Confirm deletion
4. Permanently removed

### Delete All Data

```
Windows: Delete %APPDATA%\pygpt\
Linux: rm -rf ~/.pygpt/
macOS: rm -rf ~/Library/Application\ Support/pygpt/
```

### Right to Deletion

- Your local data: You control
- Provider's data: Request from provider
- Some providers allow deletion
- Check their policies

---

## 🏢 Business & Compliance

### For Businesses

**Compliance considerations:**
- ✅ Use business tier if required
- ✅ Check data residency options
- ✅ Implement audit logs
- ✅ Use VPN/secure networks
- ✅ GDPR/CCPA compliance

**Recommended:**
- Anthropic Claude (good privacy)
- Google VertexAI (enterprise options)
- Ollama (complete control)

### GDPR/CCPA Compliance

- ✅ Don't store personal data
- ✅ Use anonymization
- ✅ Request right to deletion
- ✅ Check provider agreements
- ✅ Document data handling

---

## 🆘 If Privacy Breached

1. **Stop using provider immediately**
2. **Change all passwords**
3. **Regenerate API keys**
4. **Notify the provider**
5. **Check for unauthorized use**
6. **Monitor accounts for fraud**
7. **Report to relevant authorities if needed**

---

## 📚 Privacy Resources

- [PyGPT Privacy Policy](https://github.com/szczyglis-dev/py-gpt#privacy)
- [Google Privacy](https://policies.google.com/privacy)
- [OpenAI Privacy](https://openai.com/privacy)
- [Anthropic Privacy](https://www.anthropic.com/privacy)

---

**See Also:**
- [FAQ - General](./general.md)
- [API Key Setup](../guides/02-api-key-setup.md)
- [Troubleshooting](../reference/troubleshooting.md)

---

**Last Updated:** 2025
