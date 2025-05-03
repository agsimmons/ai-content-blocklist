## AI Content Blocklist
The goal of this project is to create a blocklist (or possibly multiple blocklists) to block AI generated content.

My focus is specifically on websites with AI generated news, answers, etc. I will not be blocking any discussion of AI, AI generated image or video, or any demonstrations of AI generated content that is clearly labeled as such.

## How to Use
1. Install the [uBlacklist browser extension](https://iorate.github.io/ublacklist/docs)
2. Open the extension settings
3. If you use a search engine other than Google, make sure to enable it in the `Other search engines` menu
4. Under `Subscriptions`, press `Add a subscription`
5. Enter `https://raw.githubusercontent.com/agsimmons/ai-content-blocklist/refs/heads/main/uBlacklist.txt` for the URL
6. Press `Add`

## Contributing
Please submit a pull request or issue if you would like to add any websites to this list. If you think a website was incorrectly added, please create an issue.

New domains should be added to `source.toml`. Running the `generate.py` script (requires Python 3.11+) will then read that source file and generate an updated `uBlacklist.txt` file.

## Related Projects
[uBlockOrigin & uBlacklist Huge AI Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist) by laylavish
> A huge blocklist of manually curated sites that contain AI generated content for uBlock Origin & uBlacklist.

[Awesome List of uBlacklist Subscriptions](https://github.com/rjaus/awesome-ublacklist) by rjaus
> A compilation of awesome uBlacklist subscriptions to block various sites from appearing in Google, Bing, or DuckDuckGo search.
