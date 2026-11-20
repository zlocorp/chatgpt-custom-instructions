# ChatGPT Custom Instructions

**Task-adaptive instructions for clear answers, grounded research, and useful presentation.**

Choose the version that fits your ChatGPT Custom Instructions field, copy its prompt, and paste it into ChatGPT.

## Choose your version

| Version | Prompt length (LF) | With CRLF | Target limit | Get started |
| --- | ---: | ---: | ---: | --- |
| **v5.2 Compact** | 1,469 characters | 1,480 characters | 1,500 characters | [Open prompt](prompts/v5-free.md) |
| **v5.2 Extended** | 4,945 characters | 4,978 characters | 5,000 characters | [Open prompt](prompts/v5-5000.md) |

Choose by the limit shown in your account; see [OpenAI's Custom Instructions FAQ](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions). Both counts include the final newline, not the surrounding Markdown.

> Independently maintained. Improvements in answer quality have not yet been demonstrated in controlled tests.

## Quick start

1. Open **ChatGPT → Settings → Personalization → Custom Instructions**.
2. Open the version above and copy **only the text inside its code block**.
3. Replace your previous general-purpose instructions and save.

Download ready-to-use TXT files from [Release v5.2](https://github.com/zlocorp/chatgpt-custom-instructions/releases/tag/v5.2). See the [changelog](CHANGELOG.md) for the version history.

## What changed in v5.2

Both variants now explicitly protect complete, self-contained answers: preserve necessary explanations and evidence, distinguish workflow assumptions from unknown facts, cite supported claims, and state specific evidence gaps. Compact also warns that incomplete retrieval is not proof of absence.

Extended additionally checks that each source supports the wording and scope of its claim, keeps source content separate from added analysis, and makes substantial calculations inspectable through their inputs, units, assumptions, and necessary steps. Optional suggestions must not become invented requirements. Presentation guidance is more compact while retaining useful formats and capability limits.

The revision prioritizes OpenAI's prompting guidance reviewed on November 20, 2026, with selected ideas from related chat-instruction projects. These are evidence-informed wording changes, not measured improvements in model performance.

Compact is a shorter set of priorities, not a full substitute for every Extended rule. Both variants fit their limits with LF and CRLF line endings.

## FAQ

### Can I combine these with my existing instructions?

Replace your previous general-purpose block to avoid contradictions. Add personal preferences only if needed and within your field limit; the supplied prompts leave little room for additions.

### Do these require a particular model or plugin?

No. They describe behavioral preferences, not a model choice, new tools, or additional permissions. Results vary by model and task.

### Do these enable Intelligent UI or other features?

No. They can request supported presentation formats but cannot enable capabilities missing from the active ChatGPT mode.

## Evaluation status

There are no controlled A/B results demonstrating better accuracy, lower cost, or faster completion for v5.2. Character-limit, structure, and export checks establish content consistency, not model performance.

Compare against an empty-instructions baseline and the previous version with the same model, reasoning setting, tasks, tools, and scoring method. Preserve raw outputs and report failures as well as successes; see the [evaluation guide](EVALUATION.md) and [Contributing](CONTRIBUTING.md).

Historical [v3 evaluation results](prompts/v3.md), including the documented grader issue, do not establish v5.2 performance.

## Earlier versions

<details>
<summary>Browse v1-v5 and historical evaluation material</summary>

| Version | Purpose |
| --- | --- |
| [v5.1 release](https://github.com/zlocorp/chatgpt-custom-instructions/releases/tag/v5.1) | Previous Compact and Extended instructions, preserved by the release tag and TXT downloads. |
| [v5 Extended](https://github.com/zlocorp/chatgpt-custom-instructions/blob/v5/v5-5000.md) | Original v5 text at its published tag. |
| [v5 Compact](https://github.com/zlocorp/chatgpt-custom-instructions/blob/v5/v5-free.md) | Original compact v5 text at its published tag. |
| [v4 Extended](prompts/v4-5000.md) | Earlier 5,000-character edition. |
| [v4 Compact](prompts/v4-free.md) | Earlier 1,500-character edition. |
| [v3](prompts/v3.md) | Historical prompt and evaluation caveats. |
| [v2](prompts/v2.md) | Earlier iteration. |
| [v1](prompts/v1.md) | Earlier iteration. |

The [v5 release and its downloads](https://github.com/zlocorp/chatgpt-custom-instructions/releases/tag/v5) remain unchanged. Minor updates reuse the current major-version Markdown files; each release tag preserves its own source snapshot.

</details>

## Sources and attribution

- [OpenAI: Custom Instructions FAQ](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions)
- [OpenAI: Latest model prompting guidance](https://developers.openai.com/api/docs/guides/latest-model) (GPT-6.2 when reviewed for v5.2)
- [OpenAI: Citation formatting](https://developers.openai.com/api/docs/guides/citation-formatting)
- [OpenAI: Reasoning models](https://developers.openai.com/api/docs/guides/reasoning)
- [OpenAI: Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [OpenAI: Model Spec, October 29, 2026](https://model-spec.openai.com/2026-10-29.html)
- [OpenAI: Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) (earlier context)
- [OpenAI: Intelligent UI in ChatGPT](https://help.openai.com/en/articles/20001598-intelligent-ui-in-chatgpt)
- [OpenAI: ChatGPT release notes](https://help.openai.com/en/articles/6825453/chatgpt-release-notes)
- [OpenAI: GPT-5 Prompting Guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide) (historical context)

Related chat-instruction projects reviewed for v5.2 include [admknight's scope-control rules](https://github.com/admknight/universal-chatgpt-custom-instructions/blob/7cc588b8423974cfe0a429bd0535ef6d2e3ab10d/COPY-THIS-Plus-Pro-Business-Enterprise-Education.txt), [Artur Bikbaev's calculation guidance](https://github.com/arturbikbaev/Custom-Instructions-for-ChatGPT/blob/dc8c226e98d105d3c66c097257f81f203512d91f/README.md), and [GPT-Helper's mobile source checks](https://github.com/FFriends/GPT-Helper/blob/12edc146f6f932ee1886899d9741662e2d31ccdd/MOBILE_CUSTOM_INSTRUCTIONS_EN.md). Individual principles were adapted; their complete prompts and performance claims are not adopted.

This is an independently maintained fork of [thedisciple/chatgpt-custom-instructions](https://github.com/thedisciple/chatgpt-custom-instructions), itself a fork of [Denis Shiryaev's original project](https://github.com/DenisSergeevitch/chatgpt-custom-instructions). Earlier versions and contributions retain their original attribution.

Suggestions and reproducible evaluations are welcome; see [Contributing](CONTRIBUTING.md).
