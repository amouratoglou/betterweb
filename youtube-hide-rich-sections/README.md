BetterWeb (Chrome Extension)

Why and What?
- Just improves your UX in youtube, maybe in the future will add other features.

Overview
- Hides YouTube homepage “rich section” rows by targeting `#content.ytd-rich-section-renderer`.
- Observes DOM mutations so newly loaded sections are hidden too.
- Runs at `document_start` for earlier hiding.

Manual Install (Unpacked)
1. Open `chrome://extensions`.
2. Enable Developer mode (top-right).
3. Click Load unpacked and select the extension folder.
4. Open YouTube; the targeted rows will be hidden automatically.

Store Listing Text (copy/paste)
- Name: BetterWeb
- Short description: Hides YouTube homepage “rich section” rows automatically, including dynamically loaded content.
- Full description:
  Hide YouTube’s rich section rows on the homepage. The extension removes elements matching `#content.ytd-rich-section-renderer` and keeps them hidden as the page updates.

  Highlights
  - Runs automatically on YouTube pages
  - Observes DOM changes to hide new sections
  - No ads, no analytics, no data collection

  Notes
  - Not affiliated with YouTube or Google.
  - YouTube is a trademark of Google LLC.

Privacy
- This extension does not collect, transmit, or store any personal data. It operates entirely as a content script on `youtube.com` and does not communicate with external services.

Support
- GitHub Issues: https://github.com/amouratoglou/betterweb/issues
- Alternatively, enable Discussions and use Q&A.

Files
- `manifest.json`: Manifest V3 config.
- `content.js`: Content script logic.
- `icons/`: Extension icons (16/48/128).
