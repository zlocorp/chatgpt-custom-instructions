# ChatGPT Custom Instructions

**Task-adaptive instructions for clear answers, grounded research, and useful presentation.**

Choose the version that fits your ChatGPT Custom Instructions field, copy its prompt, and paste it into ChatGPT.

## Choose your version

The prompt pages below contain **unreleased working edits**. The published v5 release remains unchanged.

| Version | Prompt length (LF) | Field limit | Get started |
| --- | ---: | ---: | --- |
| **v5 Compact** | 1,474 characters | 1,500 characters | [Open prompt](v5-free.md) |
| **v5 Extended** | 4,869 characters | 5,000 characters | [Open prompt](v5-5000.md) |

As of October 2026, [OpenAI's Custom Instructions FAQ](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions) lists a 1,500-character limit for Free and Go, and 5,000 for Plus, Pro, Business, Enterprise, and Education. Choose by the limit available in your account.

> Independently maintained. Improvements in answer quality have not yet been demonstrated in controlled tests.

## Quick start

1. Open **ChatGPT → Settings → Personalization → Custom Instructions**.
2. Open the version above and copy **only the text inside its code block**.
3. Replace your previous general-purpose instructions and save.

For the previous published text, download TXT files from [Release v5](https://github.com/zlocorp/chatgpt-custom-instructions/releases/tag/v5). These do not include the working edits above.

## What v5 focuses on

- **Clear answers:** match the task's complexity without mandatory personas, templates, or unnecessary repetition.
- **Grounded research:** distinguish evidence, assumptions, and uncertainty; verify when it matters.
- **Reliable completion:** finish authorized work while respecting boundaries around publication, spending, and disclosure.
- **Useful presentation:** use tables, visuals, or interactive elements when available and genuinely helpful.
- **Proportionate checks:** validate important results without an endless self-review loop.

## FAQ

### Can I combine v5 with my existing instructions?

Replace your previous general-purpose block to avoid contradictions. Add personal preferences separately if needed, staying within the character limit.

### Does v5 require a particular model or plugin?

No. It describes behavioral preferences, not a model choice, new tools, or additional permissions. Results vary by model and task.

### Does v5 enable Intelligent UI or other features?

No. It can request supported presentation formats but cannot enable capabilities missing from the active ChatGPT mode.

## Evaluation status

There are no controlled A/B results demonstrating better accuracy, lower cost, or faster completion for v5. To evaluate it, compare against an empty-instructions baseline using the same model, reasoning setting, tasks, tools, and scoring method. Preserve raw outputs and report failures as well as successes; see the [12-case evaluation guide](EVALUATION.md) and [Contributing](CONTRIBUTING.md).

Historical [v3 evaluation results](v3.md), including the documented grader issue, do not establish v5 performance.

## Earlier versions

<details>
<summary>Browse v1–v4 and historical evaluation material</summary>

| Version | Purpose |
| --- | --- |
| [v4 Extended](v4-5000.md) | Previous 5,000-character edition. |
| [v4 Compact](v4-free.md) | Previous 1,500-character edition. |
| [v3](v3.md) | Historical prompt and evaluation caveats. |
| [v2](v2.md) | Earlier iteration. |
| [v1](v1.md) | Earlier iteration. |

v5 replaces a mandatory rubric with task-dependent success criteria and verification, and adds guidance for conditional visual presentation.

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
