# ChatGPT Custom Instructions

**Task-adaptive instructions for clear answers, grounded research, and useful presentation.**

Choose a version, copy its prompt, and paste it into ChatGPT Custom Instructions. No installation or plugins required.

## Choose your version

| Version | Prompt length | Field limit | Get started |
| --- | ---: | ---: | --- |
| **v5 Compact** | 1,394 characters | 1,500 characters | [Open prompt](v5-free.md) |
| **v5 Extended** | 4,949 characters | 5,000 characters | [Open prompt](v5-5000.md) |

Choose by the limit shown in your Custom Instructions field. Counts include spaces, tags where present, LF line breaks, and the final newline, but not the surrounding Markdown.

As of October 2026, the [official FAQ](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions) lists 1,500 characters for Free and Go, and 5,000 for Plus, Pro, Business, Enterprise, and Education.

> Independently maintained. No controlled performance improvement has been demonstrated yet.

## Quick start

1. Open **ChatGPT → Settings → Personalization → Custom Instructions**.
2. Choose **Compact** or **Extended** above and copy only the text inside its code block.
3. **Replace** your previous instructions. Do not combine the two versions or paste the entire Markdown page.
4. Try a representative task and compare the result with your usual setup.

## What v5 focuses on

- **Useful answers:** match depth to the task, preserve editing requirements, and skip mandatory personas or response templates.
- **Grounded work:** use relevant sources, distinguish evidence from assumptions, and check actual results.
- **Completion with boundaries:** finish authorized work without treating drafting as permission to publish, spend, or disclose private data.
- **Appropriate presentation:** use clear text, structured comparisons, visuals, or supported interactive elements when they help.
- **Proportionate verification:** correct material problems without imposing a fixed-size rubric or endless self-criticism.

Extended spells out these preferences in more detail. Compact keeps the main priorities within the smaller field; it is not a line-for-line excerpt.

## FAQ

### Which version should I use?

Use the version that fits your available field. Compact is also an option when you prefer fewer defaults. A longer instruction is not automatically a better one.

### Should I append this to my current instructions?

No. Replace the previous general-purpose block, then reintroduce only personal preferences you still need. Check for contradictions and stay within the field limit.

### Does this require a specific model or plugin?

No. v5 was informed by current GPT-6 guidance, but does not select a model, set reasoning effort, install tools, or grant permissions. Effects can differ between models and tasks.

### Will this enable visuals or Intelligent UI?

No. Presentation preferences use capabilities already supported by the active mode. They cannot enable an unavailable feature. Plain text remains appropriate for many tasks.

### Is v5 proven to improve answers?

Not yet. Character counts and document structure are checkable; answer quality needs controlled comparisons. See the evaluation status below.

## Evaluation status

**v5 is an evidence-informed proposal, not a benchmark-proven improvement.** There are no controlled A/B results demonstrating higher accuracy, lower cost, or faster completion for these prompts on Astra, Sol, Sol 6.1, or other models.

A useful comparison keeps the model or snapshot, reasoning setting, tasks, tools, and scoring method the same, with an empty Custom Instructions baseline. Preserve raw outputs and report failures and negative results alongside successes. See [Contributing](CONTRIBUTING.md) for reporting guidance.

Historical [v3 evaluation results](v3.md), including the disclosed grader issue, do **not** validate v5.

## Earlier versions

<details>
<summary>Browse v1–v4 and the historical evaluation</summary>

| Version | Purpose |
| --- | --- |
| [v4 Extended](v4-5000.md) | Earlier edition for a 5,000-character field. |
| [v4 Compact](v4-free.md) | Earlier edition for a 1,500-character field. |
| [v3](v3.md) | Earlier self-reflection prompt and evaluation caveats. |
| [v2](v2.md) | Historical iteration. |
| [v1](v1.md) | Historical iteration. |

v4 kept task-specific reflection while removing the arbitrary numerical acceptance threshold from v3. v5 uses task-dependent success criteria and verification instead of a mandatory rubric, and adds a dedicated presentation section to Extended.

The earlier prompts and associated images remain unchanged.

</details>

## Sources and attribution

Product references explain relevant behavior and limits; they are not experimental proof of prompt effectiveness.

- [Custom Instructions FAQ](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions)
- [Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model)
- [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
- [Intelligent UI in ChatGPT](https://help.openai.com/en/articles/20001598-intelligent-ui-in-chatgpt)
- [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- [GPT-5 Prompting Guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide), the historical background for the rubric approach

This is an independently maintained fork of [thedisciple/chatgpt-custom-instructions](https://github.com/thedisciple/chatgpt-custom-instructions), itself a fork of [Denis Shiryaev's original repository](https://github.com/DenisSergeevitch/chatgpt-custom-instructions). Earlier versions and contributions remain credited to their original authors. v5 builds on v4 without replacing that history.

Focused suggestions and reproducible evaluations are welcome. Read [Contributing](CONTRIBUTING.md) before submitting a change.
