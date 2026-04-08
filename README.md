# Starter Story Pipeline

**The 5-step AI pipeline behind [Solo Founder Playbook](https://github.com/yayashuxue/solo-founder-playbook).**

Takes a YouTube channel → downloads transcripts → analyzes with Claude → extracts cross-video patterns. We ran it on 101 [Starter Story](https://www.youtube.com/@starterstory) videos to build a data-backed startup knowledge base.

## How It Works

```
YouTube Channel
      │
      ▼
┌─────────────┐
│  Step 1      │  Get all video URLs via YouTube Data API
│  video_urls  │  Filters out Shorts (<5 min)
└─────┬───────┘
      ▼
┌─────────────┐
│  Step 2      │  Download transcripts via youtube-transcript.io
│  transcripts │  Incremental — skips already downloaded
└─────┬───────┘
      ▼
┌─────────────┐
│  Step 3      │  Claude analyzes each transcript
│  chapters    │  Categorizes into 11 standard categories
└─────┬───────┘  (Idea Generation, Validation, Marketing, etc.)
      ▼
┌─────────────┐
│  Step 4      │  Claude summarizes & refines
│  refinement  │  Generates product one-liners
└─────┬───────┘  Condenses quotes → actionable summaries
      ▼
┌─────────────┐
│  Step 5      │  Claude extracts cross-video patterns
│  patterns    │  Finds recurring strategies + keywords
└─────────────┘  → patterns.json + insights.md
```

**Output**: The `patterns.json` and `insights.md` files that power the [Solo Founder Playbook](https://github.com/yayashuxue/solo-founder-playbook) skills.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

Add your API keys to `.env`:
- `ANTHROPIC_API_KEY` — Claude API (steps 3-5)
- `YOUTUBE_DATA_API_KEY` — YouTube Data API v3 (step 1)
- `YOUTUBE_TRANSCRIPT_IO_API_KEY` — youtube-transcript.io (step 2)

## Usage

Run individual steps:
```bash
bash run.sh step1          # Fetch video URLs
bash run.sh step2          # Download transcripts
bash run.sh step3          # Analyze chapters (pass number to limit: bash run.sh step3 10)
bash run.sh step4          # Summarize & refine
bash run.sh step5          # Extract patterns
```

Or run everything:
```bash
bash run.sh all
```

All steps are **incremental** — they skip already-processed videos, so you can safely re-run to pick up new content.

## Adapting for Other Channels

The pipeline is designed for Starter Story but can be adapted for any YouTube channel:

1. In `step1_get_video_urls.py`, change `@starterstory` to any channel handle
2. In `step3_analyze_chapters.py`, modify the `STANDARD_CATEGORIES` and prompt to match your domain
3. Run the pipeline

## Cost Estimate

For 100 videos:
- **YouTube Data API**: Free tier is sufficient (~10K quota units)
- **youtube-transcript.io**: ~$5-10 depending on plan
- **Anthropic API**: ~$15-30 (steps 3-5, using Claude Sonnet)

## Output Files

| File | Description |
|------|-------------|
| `video_urls.json` | All video URLs + metadata |
| `transcripts/*.txt` | Raw transcripts |
| `chapters_analysis.csv` | Per-video chapter extraction |
| `chapters_analysis_refined.csv` | Summarized + product one-liners |
| `patterns_analysis.json` | Cross-video patterns (→ powers the plugin) |
| `patterns_summary.md` | Human-readable pattern summary |

## Related

- **[Solo Founder Playbook](https://github.com/yayashuxue/solo-founder-playbook)** — The Claude Code plugin powered by this pipeline's output

## License

MIT
