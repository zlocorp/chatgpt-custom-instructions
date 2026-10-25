# Personalization: what belongs where

Reviewed on 2026-10-25. Field names and available controls can differ by client and rollout. Use the fields your interface actually provides.

| Setting | Useful content |
|---|---|
| Name / nickname | How you want to be addressed |
| Occupation | A short professional description |
| About you / more about you | Stable background, skill level, recurring goals, and constraints |
| Custom Instructions | Preferences for how the assistant should respond and act |
| Base style and tone / personality | A communication preset you like |
| Project instructions | The project's audience, stack, conventions, success criteria, and boundaries |
| Current message | This task's deliverable, relevant context, date, and acceptance criteria |

Do not duplicate the same behavioral rules across every field. Avoid filling a global profile with transient project status. Review outdated memories and profile facts when they start producing wrong assumptions.

[OpenAI's personalization documentation](https://learn.chatgpt.com/docs/personalize) describes personality as a style control, separate from model capability. A neutral/default preset is a reasonable starting point for evaluating instructions. Other choices are preferences, not accuracy upgrades. Do not assume a preset name is identical on web and desktop.

Memory can carry useful context, but it is not a guarantee that the assistant has retrieved every previous chat. Ask it to use relevant available context and report missing evidence when it matters. The instructions should not pretend that unavailable tools, files, or account features exist.

For Codex, use [global instructions](codex-global.md) for personal working defaults and repository `AGENTS.md` files for codebase rules. The [documented discovery order](https://learn.chatgpt.com/docs/agent-configuration/agents-md) includes global guidance, directory guidance, and override files. Repository-specific rules can override earlier global defaults. ChatGPT's UI character limits do not describe Codex's instruction-file budget.

Subscription price alone does not prove an account's plan, selected model, or feature access. Check the account and model selector. Prompts do not need a subscription price or a hard-coded model name.
