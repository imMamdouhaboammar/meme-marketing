<div align="center">

<img src="assets/logo.svg" alt="Meme Marketing Logo" width="380" />

# 🎭 Meme Marketing: Fully Agentic Meme Crafting Engine

### High-resonance, zero-cringe memes grounded in hyper-specific audience friction, real receipts, and cultural authenticity.
**Universal AI Agent Skill • Built-in Vector Doodle Renderer • Multi-Dialect Comedy Matrix • BinEval 8-Gate Quality Filter**

<br />

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Bun](https://img.shields.io/badge/Runtime-Bun%20%3E%3D1.0-FBF0DF?style=flat-square&logo=bun&logoColor=black)](https://bun.sh)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Certified%20Skill-D97706?style=flat-square&logo=anthropic&logoColor=white)](https://claude.ai)
[![Antigravity](https://img.shields.io/badge/Antigravity%20%2F%20Gemini-Compatible-4285F4?style=flat-square&logo=google&logoColor=white)](https://deepmind.google)
[![Cursor](https://img.shields.io/badge/Cursor%20%2F%20Windsurf-Ready-000000?style=flat-square&logo=cursor&logoColor=white)](https://cursor.com)
[![Codex](https://img.shields.io/badge/Codex%20%2F%20ChatGPT-Supported-10A37F?style=flat-square&logo=openai&logoColor=white)](https://chatgpt.com)
[![Skills.sh](https://img.shields.io/badge/Skills.sh-Registry-000000?style=flat-square&logo=vercel&logoColor=white)](https://skills.sh/meme-marketing)
[![BinEval](https://img.shields.io/badge/BinEval%20Gate-10%2F10%20Verified-10B981?style=flat-square)](references/bineval-gates.md)
[![Zero Cringe](https://img.shields.io/badge/Zero%20Cringe-Guaranteed-FF6B6B?style=flat-square)](references/bineval-gates.md)

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-installation-guide">Install Guide</a> •
  <a href="#-quickstart">Quickstart</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-cli-reference">CLI Reference</a> •
  <a href="#-doodle-templates">Templates</a> •
  <a href="#-examples">Examples</a>
</p>

</div>

---

## 💡 What is Meme Marketing Agent?

Most AI-generated memes are agonizingly corporate: generic templates, forced puns, and transparent product pitches that make audiences cringe.

**Meme Marketing Agent** transforms your AI agent into an elite satirical comedy writer. Operating under the **/omni-skill** dynamic routing architecture, it mines real-world daily friction (like pushing an unreviewed PR at 4:58 PM on a Friday or getting client revisions after midnight), pairs them with proven comedic mechanisms, subjects them to 8 adversarial quality gates, and can even render them into **funny doodle line-art SVG cards** on demand.

### 🌟 Key Capabilities
- 🎯 **Tactile Receipts**: Grounded in specific error messages, timestamps (`11:47 PM`), tool names (`Docker`, `Figma`, `Excel`), and real team dynamics.
- 🌍 **Multi-Dialect Mastery**: Native fluency in **English** (Tech/B2B/Dev cynicism), **Egyptian Arabic** (Cinema echoes, witty colloquial irony), **Saudi/Gulf Arabic** (Riyadh tech scene, X feed banter), and **Levantine Arabic**.
- 🚫 **Zero Cringe Guarantee**: Automated filters eliminate corporate slogans, on-image sales pitches, hashtags, and URLs.
- 🎨 **Built-in Doodle Renderer**: Generate standalone, scalable SVG doodle meme cards directly from terminal or prompt.
- 🔄 **Continuous Taste Profiling**: Learns what your brand and audience love or hate across sessions via `assets/taste-profile.json`.

---

## 📦 Installation Guide

Install `meme-marketing` across any AI coding agent or command line environment in seconds.

### 1. One-Line Universal Auto-Installer (Recommended)
Automatically detects all installed agent environments (`Claude Code`, `Google Antigravity`, `Gemini CLI`, `Cursor`, `Codex`, and `Agent Kernel`) and installs the skill:

```bash
curl -fsSL https://raw.githubusercontent.com/imMamdouhaboammar/meme-marketing/main/install.sh | bash
```

*Or run directly if you have cloned the repository:*
```bash
./install.sh
```

---

### 2. Manual Installation by Agent Harness

#### 🟠 Claude Code & Claude Desktop
Add to your global or project skills:
```bash
# Option A: Via Skills.sh
npx skills add imMamdouhaboammar/meme-marketing

# Option B: Manual clone into Claude skills directory
mkdir -p ~/.claude/skills
git clone https://github.com/imMamdouhaboammar/meme-marketing.git ~/.claude/skills/meme-marketing
```

#### 🔵 Google Antigravity & Gemini CLI
Clone into your Gemini / Antigravity config directory:
```bash
mkdir -p ~/.gemini/config/skills
git clone https://github.com/imMamdouhaboammar/meme-marketing.git ~/.gemini/config/skills/meme-marketing
```

#### 🟣 Cursor IDE & Windsurf
Add to your project root or user configuration:
```bash
mkdir -p .cursor/skills
git clone https://github.com/imMamdouhaboammar/meme-marketing.git .cursor/skills/meme-marketing
```
*Or add this rule to `.cursorrules` / `.windsurfrules`:*
```text
When asked to create memes or social humor, refer to instructions in .cursor/skills/meme-marketing/SKILL.md
```

#### 🟢 OpenAI Codex & ChatGPT
Copy or link the package to your Codex skills directory:
```bash
mkdir -p ~/.codex/skills
git clone https://github.com/imMamdouhaboammar/meme-marketing.git ~/.codex/skills/meme-marketing
```
*The root `.codex-plugin/plugin.json` is pre-configured and ready for ChatGPT Actions and custom GPTs.*

#### ⚡ Zero-Install CLI (Any Terminal)
Run immediately without installation using Bun or npx:
```bash
# Using Bun (instant TS execution)
bunx meme-marketing --help

# Using npx
npx meme-marketing list
```

---

## ⚡ Quickstart

Once installed, simply prompt your agent naturally:

### Example Prompts

#### 1. English Developer Culture
> *"Craft 3 memes for our open-source developer tooling project. Our audience is senior backend engineers who hate slow CI/CD pipelines. Platform: X (Twitter)."*

#### 2. Egyptian B2B SaaS
> *"عايز 3 ميمز لصفحة PrePilot، منصة بتساعد الماركتير يحسب الميزانية وميديا بلان قبل الحملة. الجمهور بتاعنا performance marketers في مصر. باللهجة المصرية ولينكد إن."*

#### 3. Saudi E-Commerce Logistics
> *"اكتبلي ميمز لشركة شحن وتوصيل B2B في الرياض، لمدراء العمليات وأصحاب المتاجر الإلكترونية. نبيها باللهجة السعودية لـ X مع ريندر دودل."*

---

## 🏛️ Architecture & Execution Flow

Operating under the canonical `/omni-skill` dynamic routing pattern:

```mermaid
flowchart TD
    A["User Request (Any Language)"] --> B["OmniSkill Intent Router"]
    B --> C["Route Classifier (CREATE | AUDIT | LOCALIZE | TUNE | BATCH | RENDER)"]
    
    subgraph ExecutionDAG ["Targeted Meme Execution DAG"]
        D["Phase 1: Discovery & Briefing (Persona, Tone, Platform)"]
        E["Phase 2: Micro-Moment Miner (Real-world friction & receipts)"]
        F["Phase 3: Comedy Matrix Engine (Mechanic + Format + Image-Text Tension)"]
        G["Phase 4: Multi-Agent Critic & BinEval Gate (Send test, Cringe filter)"]
        H["Phase 5: Visual Production & Doodle Renderer (SVG Card / Diffusion Prompt)"]
        I["Phase 6: Multi-Platform Publishing Copy & Contract Export"]
    end
    
    C --> ExecutionDAG
    G -.->|"Gate Failure / Cringe Detected"| F
    ExecutionDAG --> J["Publishable Relatable Meme (Text + SVG + JSON)"]
```

---

## 🛠️ CLI Reference (`meme-craft`)

The built-in CLI provides instant utilities for generating, rendering, and validating memes:

```bash
meme-craft <command> [options]
```

### Commands & Flags

| Command | Options | Description |
|---|---|---|
| `craft` | `--topic`, `--audience`, `--dialect`, `--platform`, `--json` | Synthesize complete meme specs or machine-readable JSON |
| `render` | `--template`, `--caption`, `--new`, `--user`, `--current`, `--out` | Render vector doodle line-art meme card (`.svg`) |
| `validate` | `<path-to-json>` | Validate batch JSON against output contract and cringe filters |
| `list` | *none* | Display catalog of humor mechanics, formats, and doodle templates |
| `tune` | `--accept <id>`, `--reject <id>`, `--note <text>` | Mutate and persist preferences into `taste-profile.json` |

---

## 🎨 Built-in Doodle Line-Art Templates

The engine includes 4 pre-drawn, funny doodle vector templates ready for instant rendering:

| Template Name | Identifier | Best For |
|---|---|---|
| **Distracted Marketer** | `distracted` | Choosing a shiny new trend/framework over existing critical duties |
| **Two Buttons Dilemma** | `two-buttons` | Agonizing between two equally stressful or tempting options |
| **This is Fine** | `this-is-fine` | Unfazed calm while servers, budgets, or deadlines burn down |
| **Doodle Approve / Reject** | `drake` | Disapproving legacy slow workflows vs approving modern agentic workflows |

### CLI Rendering Example:
```bash
bun scripts/meme-craft.ts render --template distracted \
  --caption "Every single Friday at 4:30 PM" \
  --new "Rewriting the backend in Rust" \
  --user "Senior Architect" \
  --current "24 unresolved client tickets" \
  --out friday-dilemma.svg
```

---

## 🛡️ The 8 BinEval Quality Gates

Every meme generated must pass 8 strict gates:

1. **The Send Test**: You can name the exact human who forwards this to whom in Slack/DMs.
2. **The Receipt Check**: Grounded in specific, tactile real-world details (`11:47 PM`, `Docker build`, `Excel formula error`).
3. **Image-Text Contract**: Caption and visual have tension or dialogue; neither is redundant.
4. **Feed Glance Test**: The joke registers in under 1.5 seconds at feed speed.
5. **Logo-Free Share Test**: Funny even if the company logo is covered.
6. **Batch Variety**: Every concept uses a distinct comedic mechanism and visual format.
7. **Zero Cringe Guarantee**: Automated check bans on-image URLs, CTAs, hashtags, and corporate jargon.
8. **Dialect Integrity**: True spoken phrasing; never stiff Modern Standard Arabic or unconvincing slang.

---

## 📁 Repository Structure

```text
├── assets/
│   ├── logo.svg              # Funny Doodle Line-Art Vector Logo
│   ├── logo.png              # High-res visual asset
│   ├── taste-profile.json    # Continuous memory & feedback store
│   └── templates/            # Hand-drawn vector meme templates (SVG)
│       ├── distracted-doodle.svg
│       ├── two-buttons-doodle.svg
│       ├── this-is-fine-doodle.svg
│       └── drake-doodle.svg
├── bin/
│   └── cli.js                # Executable CLI entrypoint (Bun & Node)
├── evals/
│   ├── evals.json            # Benchmark test cases
│   └── fixtures/             # Valid and invalid JSON test cases
├── references/
│   ├── agentic-router.md     # Dynamic routing & DAG execution spec
│   ├── bineval-gates.md      # The 8 quality gates & anti-cringe filters
│   ├── caption-craft.md      # Dialect rules, pacing & mobile cadence
│   ├── design-spec.md        # Typography, contrast & safe areas
│   ├── format-bank.md        # Taxonomy of visual formats
│   ├── host-compatibility.md # Per-agent capability profiles
│   ├── humor-mechanics.md    # 10 comedic mechanics & voices
│   ├── output-contract.md    # JSON schema specification
│   └── post-tuning.md        # Continuous taste learning guide
├── scripts/
│   ├── meme-craft.ts         # Agentic CLI engine & SVG renderer
│   ├── validate.py           # Python 3 validator
│   └── test_validate.py      # Automated Python unit test suite
├── .codex-plugin/
│   └── plugin.json           # OpenAI Codex manifest
├── .github/workflows/
│   └── ci.yml                # GitHub Actions test pipeline
├── .skills.json              # Skills.sh registry manifest
├── install.sh                # Universal multi-agent installer
├── marketplace.json          # Claude Marketplace manifest
├── package.json              # Bun / npm distribution manifest
├── SKILL.md                  # Canonical Agentic Skill contract
└── README.md                 # High-presence documentation
```

---

## 🤝 Contributing

Contributions of new funny doodle templates, humor mechanics, and dialect nuances are welcome! Please run tests before submitting PRs:

```bash
bun test
python3 scripts/test_validate.py
```

---

## 📄 License

MIT © [Mamdouh Aboammar](https://github.com/imMamdouhaboammar)
