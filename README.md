# ChatGPT Custom Instructions

General-purpose, evidence-informed Custom Instructions for ChatGPT. This fork adds **v5**, updated for the GPT-6 family and optional rich or interactive presentation, while preserving the previous versions and upstream history.

The prompts describe **preferences**, not new model capabilities or permissions. Neither variant requires a specific model, plugin, account-specific context, or writing style. Their effects are **not yet benchmark-proven**.

> [!IMPORTANT]
> As of October 2026, ChatGPT Custom Instructions allow **1,500 characters for Free and Go**, and **5,000 characters for Plus, Pro, Business, Enterprise, and Education**. See the [official Custom Instructions FAQ](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions). Choose the variant for your plan and copy only its fenced prompt, not the surrounding Markdown.

## Choose v5

### Free & Go: 1,500 characters

**[v5 Compact](v5-free.md)** — **1,394 characters** with LF line endings.

A shorter set of preferences covering useful answers, task completion, editing fidelity, evidence, proportionate checks, and optional visual presentation. It intentionally avoids rigid response templates.

### Plus / Pro / Business / Enterprise / Education: 5,000 characters

**[v5 Extended](v5-5000.md)** — **4,949 characters** with LF line endings.

The extended version adds detailed guidance for self-review, authorization boundaries, source handling, visual and document quality, clear explanations, and reporting limits. It supports mixed text-and-visual answers **when the active ChatGPT mode actually supports them**.

## What changed in v5

- **Task-specific quality checks:** define success for the task, correct material weaknesses, and stop when the result is complete; no mandatory 5–7-point rubric or repeated self-criticism.
- **Follow-through with boundaries:** finish authorized work without re-asking for approval, while distinguishing analysis and drafting from publication, spending, disclosure, or destructive actions.
- **Adaptive presentation:** use plain text, structured comparisons, visuals, charts, or supported interactive elements when they materially help. Keep publishable writing copyable and editable.
- **Evidence over confidence:** distinguish sourced facts, estimates, and uncertainty; check changing claims and validate actual artifacts with proportionate tools and tests.
- **Less compulsory process:** no mandatory persona, TL;DR, output format, document stack, or universal test suite.

The extended and compact variants pursue the same goals at different levels of detail. Neither variant enables Intelligent UI in an unsupported mode.

## How to use

1. Open **ChatGPT → Settings → Personalization → Custom Instructions**.
2. Open [v5 Compact](v5-free.md) or [v5 Extended](v5-5000.md) according to the field limit shown for your plan.
3. Copy **only the text inside the code block** and replace previous instructions. Do not combine variants.
4. Use a new task to assess the behavior. Custom Instructions are preferences layered with ChatGPT's governing rules and the specific task; results can vary by model and mode.

## Evaluation and limitations

**v5 is an editorial proposal, not a demonstrated performance improvement.** The text has been checked for its character limits and structure, but there are no controlled A/B results proving improved accuracy, lower cost, or faster completion on GPT-6 Astra, Sol, Sol 6.1, or other models. Individual features, including Intelligent UI, depend on product and mode availability.

A fair evaluation should compare an **empty Custom Instructions baseline** against the candidate under the same model or snapshot, reasoning setting, task set, tools, and scoring method. Preserve raw outputs and report failures and negative results, not only aggregate successes. Review the [contribution guidance](CONTRIBUTING.md) for reproducible reports.

The historical v3 MMLU-PRO results remain in [v3.md](v3.md), including the author's disclosure that a grader issue affected some answers. Those results **do not validate v5**.

## Earlier versions

| Version | Scope | Notes |
|---|---|---|
| [v4 Extended](v4-5000.md) | 5,000 characters | Task-specific reflection, stopping conditions, sources, and checks. |
| [v4 Compact](v4-free.md) | 1,500 characters | Shorter edition for Free and Go. |
| [v3 archive](v3.md) | Historical | Earlier self-reflection prompt and evaluation caveats. |
| [v2](v2.md) | Historical | Earlier iteration. |
| [v1](v1.md) | Historical | Earlier iteration. |

v4 retained the rubric concept from v3 while removing its arbitrary numerical acceptance threshold. v5 instead makes success criteria and actual verification task-dependent, and adds a dedicated presentation section in the extended edition.

## References

- [OpenAI: Custom Instructions FAQ](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions) — field limits and behavior.
- [OpenAI: Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model) — model-family guidance.
- [OpenAI: Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) — prompt scope, redundant checks, and over-instruction.
- [OpenAI: Intelligent UI in ChatGPT](https://help.openai.com/en/articles/20001598-intelligent-ui-in-chatgpt) — conditional rich presentation.
- [OpenAI: ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes).
- [OpenAI: GPT-5 Prompting Guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide) — historical background for the rubric approach.

## Attribution

This repository is a fork of [thedisciple/chatgpt-custom-instructions](https://github.com/thedisciple/chatgpt-custom-instructions), itself a fork of [DenisSergeevitch/chatgpt-custom-instructions](https://github.com/DenisSergeevitch/chatgpt-custom-instructions) by **Denis Shiryaev**. The earlier versions, original contributions, repository history, and acknowledgments remain credited to their original authors. v5 builds upon the v4 approach rather than replacing its historical record.

Contributions and reproducible evaluations are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).
