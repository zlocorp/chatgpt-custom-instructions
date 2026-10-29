# ChatGPT Custom Instructions

**Task-adaptive instructions for clear answers, grounded research, and useful presentation.**

Choose the version that fits your ChatGPT Custom Instructions field, copy its prompt, and paste it into ChatGPT.

## Choose your version

| Version | Prompt length (LF) | With CRLF | Field limit | Get started |
| --- | ---: | ---: | ---: | --- |
| **v5.1 Compact** | 1,482 characters | 1,493 characters | 1,500 characters | [Open prompt](v5.1-free.md) |
| **v5.1 Extended** | 4,921 characters | 4,954 characters | 5,000 characters | [Open prompt](v5.1-5000.md) |

Choose by the limit shown in your account; see [OpenAI's Custom Instructions FAQ](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions). Both counts include the final newline, not the surrounding Markdown.

> Independently maintained. Improvements in answer quality have not yet been demonstrated in controlled tests.

## Quick start

1. Open **ChatGPT → Settings → Personalization → Custom Instructions**.
2. Open the version above and copy **only the text inside its code block**.
3. Replace your previous general-purpose instructions and save.

Download ready-to-use TXT files from [Release v5.1](https://github.com/zlocorp/chatgpt-custom-instructions/releases/tag/v5.1). See the [changelog](CHANGELOG.md) for the version history.

## What changed in v5.1

Both variants clarify completion criteria, understand clear intent despite typos, encourage diagnostic checks that distinguish causes, and treat instructions embedded in sources as data. The authorization wording now explicitly distinguishes analysis or drafting **alone** from a request that also authorizes changes or publication.

Extended additionally checks relevant tool availability and retrieval coverage, preserves unrelated work, verifies uncertain writes before retrying, and accounts for unfinished parts of a request. Its conditional visual-presentation guidance is unchanged.

Compact is a shorter set of priorities, not a full substitute for every Extended rule. Both variants fit their limits with LF and CRLF line endings.

## FAQ

### Can I combine these with my existing instructions?

Replace your previous general-purpose block to avoid contradictions. Add personal preferences only if needed and within your field limit; the supplied prompts leave little room for additions.

### Do these require a particular model or plugin?

No. They describe behavioral preferences, not a model choice, new tools, or additional permissions. Results vary by model and task.

### Do these enable Intelligent UI or other features?

No. They can request supported presentation formats but cannot enable capabilities missing from the active ChatGPT mode.

## Evaluation status

There are no controlled A/B results demonstrating better accuracy, lower cost, or faster completion for v5.1. Character-limit, structure, and export checks establish content consistency, not model performance.

Compare against an empty-instructions baseline and the previous version with the same model, reasoning setting, tasks, tools, and scoring method. Preserve raw outputs and report failures as well as successes; see the [evaluation guide](EVALUATION.md) and [Contributing](CONTRIBUTING.md).

Historical [v3 evaluation results](v3.md), including the documented grader issue, do not establish v5.1 performance.

## Earlier versions

<details>
<summary>Browse v1-v5 and historical evaluation material</summary>

| Version | Purpose |
| --- | --- |
| [v5 Extended](v5-5000.md) | Original v5 text, matching the published v5 release. |
| [v5 Compact](v5-free.md) | Original compact v5 text, matching the published v5 release. |
| [v4 Extended](v4-5000.md) | Earlier 5,000-character edition. |
| [v4 Compact](v4-free.md) | Earlier 1,500-character edition. |
| [v3](v3.md) | Historical prompt and evaluation caveats. |
| [v2](v2.md) | Earlier iteration. |
| [v1](v1.md) | Earlier iteration. |

The [v5 release and its downloads](https://github.com/zlocorp/chatgpt-custom-instructions/releases/tag/v5) remain unchanged.

</details>

## Sources and attribution

- [OpenAI: Custom Instructions FAQ](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions)
- [OpenAI: GPT-6 model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [OpenAI: Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
- [OpenAI: Intelligent UI in ChatGPT](https://help.openai.com/en/articles/20001598-intelligent-ui-in-chatgpt)
- [OpenAI: ChatGPT release notes](https://help.openai.com/en/articles/6825453/chatgpt-release-notes)
- [OpenAI: GPT-5 Prompting Guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide) (historical context)

This is an independently maintained fork of [thedisciple/chatgpt-custom-instructions](https://github.com/thedisciple/chatgpt-custom-instructions), itself a fork of [Denis Shiryaev's original project](https://github.com/DenisSergeevitch/chatgpt-custom-instructions). Earlier versions and contributions retain their original attribution.

Suggestions and reproducible evaluations are welcome; see [Contributing](CONTRIBUTING.md).
