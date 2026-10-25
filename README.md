# ChatGPT & Codex Custom Instructions

Practical, source-informed starting points reviewed for **GPT-6 on October 25, 2026**. Choose the smallest set that fixes your actual problems. These prompts are proposals, **not benchmark-proven accuracy improvements**.

## Choose a starting point

| Use | Prompt | Characters* |
|---|---|---:|
| ChatGPT Free / Go, or a lean default on any plan | [ChatGPT Compact](chatgpt-compact.md) | 1,327 |
| ChatGPT Plus / Pro / Business / Enterprise / Education | [ChatGPT Extended](chatgpt-extended.md) | 2,924 |
| Codex global preferences | [Codex global instructions](codex-global.md) | 2,053 |

*Prompt block only; LF line breaks counted, no trailing newline. Names refer to instruction variants, not model versions.

## What changed for GPT-6

The [current GPT-6 guide](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#prompting-best-practices) highlights follow-through, sensitivity to contextual instructions, writing style, and proportionate verification. Its examples describe Astra behavior and are starting points for the family, not measured guarantees for every ChatGPT surface.

The October 7 [ChatGPT release note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) distinguishes GPT-6 Sol in paid Chat, GPT-6 Luna in Free/Go Chat, and Astra for Pro reasoning. Work and Codex have their own model selection. An API model guide does not establish what a particular subscription can access.

The new defaults therefore:

- Define the requested outcome and continue through relevant validation within the user's authorization.
- Ask questions when the answer materially changes the outcome, rather than pausing for routine choices.
- Keep a simple evidence-and-requirements check. Remove the mandatory hidden 5–7-part rubric, numeric self-scores, and expert-role ceremony.
- Prefer targeted validation; repeated tests and self-critique need a concrete reason.
- Distinguish the user's request from instructions embedded in source material.
- Allow useful tables, diagrams, and interactive visuals without requiring a presentation ritual.

These are design choices informed by current guidance. Removing a fixed rubric is **not** a claim that rubrics never help. Use an explicit rubric in a task prompt when assessment criteria matter. The [OpenAI article on revisiting skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) supports reviewing accumulated scaffolding, contextual reading rules, and completion boundaries.

## ChatGPT setup and limits

1. Open **Settings → Personalization → Custom Instructions** (mobile labels may differ).
2. Enable customization and paste **one** prompt block.
3. Put stable biography in the profile fields that your client exposes; put project-specific context in the project or current request.
4. Test the result on a few representative tasks. Remove rules that do not improve your experience.

The [Custom Instructions FAQ](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions) currently states **1,500 characters for Free and Go**, and **5,000 for Plus, Pro, Business, Enterprise, and Education**. The higher limit was announced on July 15, 2026 in the [release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes). Follow the limit shown by your client if rollout or interface differences arise.

The FAQ's setup section says updates apply **immediately across chats, including existing conversations**. They do not rewrite previously generated messages. Some older FAQ wording still refers to future conversations; a new chat is useful for a clean comparison, not a documented prerequisite for applying the setting.

See [personalization guidance](PERSONALIZATION.md) for profile fields, personality, memory, and the separate Codex setup. Custom Instructions do not select a model, set API reasoning parameters, unlock tools, expand context, or bypass permissions.

## Evaluation status

**No new model benchmark or controlled behavioral A/B evaluation was run for this update.** Character counts, local links, prompt structure, and source claims were checked. Those checks establish documentation consistency, not prompt efficacy.

The [v3 archive](v3.md) preserves the upstream reported MMLU-PRO result of **70.20%** on GPT-5 Nano and the author's note about a TL;DR-related grader bug. That result does not validate these GPT-6 prompts or predict everyday ChatGPT performance.

Use [EVALUATION.md](EVALUATION.md) for a small, repeatable task suite and reporting controls. Compare an empty-instructions baseline, the previous prompt, and the new variant on the same visible model, surface, tools, and settings. Report regressions as well as wins.

## Sources reviewed

- [Using GPT-6 — prompting best practices](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#prompting-best-practices): model behavior and outcome-focused prompting.
- [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): accumulated guidance, reading scope, tests, and persistence.
- [ChatGPT Custom Instructions FAQ](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions): setup, limits, and application of changes.
- [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes): July 15 limits and October 7 GPT-6 rollout.
- [Personalize ChatGPT](https://learn.chatgpt.com/docs/personalize): global preferences, personality, and memory.
- [AGENTS.md instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md): Codex discovery, overrides, and size cap.
- [Prompting in Chat, Work, and Codex](https://learn.chatgpt.com/docs/prompting): goals, context, output, and boundaries.

Live documentation can change. The review date is a snapshot, not a promise of future availability.

## History and attribution

Original v1–v3 prompts and benchmarks: **[Denis Shiryaev (@DenisSergeevitch)](https://github.com/DenisSergeevitch)**, [upstream repository](https://github.com/DenisSergeevitch/chatgpt-custom-instructions). This fork preserves that history and attribution.

- [v1](v1.md), [v2](v2.md), [v3 and its reported benchmark](v3.md)
- Historical v4: [Compact](v4-free.md), [Extended](v4-5000.md)
- [Changelog](CHANGELOG.md), [contribution guidance](CONTRIBUTING.md)

## License

The inherited repository says: “Feel free to use and modify these instructions for your own use.” This update does not add a new license or change upstream licensing terms.
