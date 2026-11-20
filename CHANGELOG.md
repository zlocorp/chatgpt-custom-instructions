# Changelog

## v5.2 - 2026-11-20

### Instructions

- Prioritize complete, self-contained answers, retaining necessary explanations and evidence when shortening the response.
- Distinguish reversible workflow assumptions from unknown facts; give the supported parts of an answer and identify evidence gaps instead of inventing details.
- Make citation support explicit. Extended checks the wording and scope of sourced claims and separates source content from added analysis; Compact explicitly requests supporting evidence and warns against treating incomplete retrieval as proof of absence.
- In Extended, retain the inputs, units, assumptions, and steps needed to verify substantial calculations, and prevent optional suggestions from becoming invented requirements.
- Preserve task-adaptive checks, factual fidelity in editing, authorized task completion, and the treatment of embedded source instructions as data. Condense presentation guidance without imposing a persona or a fixed answer length.

### Compatibility and documentation

- Compact: 1,469 characters with LF; 1,480 with CRLF. Extended: 4,945 characters with LF; 4,978 with CRLF. Counts include the final newline; TXT exports use LF.
- Update the existing major-version source pages, README, feedback-form options, and release instructions. Preserve earlier releases through their tags and attachments.
- Prioritize current official OpenAI prompting guidance, document selected related chat-instruction sources, and add a focused proposed comparison for v5.2.
- Describe release variants by character limits rather than assuming that a particular plan always has the same field size.

No controlled model A/B evaluation has been completed. The changes are supported by a source and text review; static checks do not establish improved accuracy, latency, or cost.

## Repository maintenance - 2026-10-31

- Move v1-v5.x prompt pages to `prompts/` and historical evaluation images to `prompts/assets/`.
- Update links, release source lookup, documentation and regression tests for the relocated files.
- Keep all prompt text, upstream attribution, Git history and existing v5/v5.1 tags and release attachments unchanged. No new release is created.

## Repository maintenance - 2026-10-30

- Keep the latest v5.x prompts in `v5-free.md` and `v5-5000.md`, updating them in place for minor releases.
- Preserve prior minor versions in immutable Git tags and their published release attachments. Remove redundant `v5.1-*.md` files from the current branch without altering the v5 or v5.1 releases.
- Select Markdown sources by major version while retaining the complete tag for README labels, changelog entries and release notes.

## v5.1 - 2026-10-29

### Instructions

- Clarify that analysis or drafting alone does not authorize changes, sending, or publication; existing explicit authorization still applies.
- Interpret clear intent despite typos or dictation and choose diagnostic checks that distinguish likely causes.
- Treat directives embedded in sources as data unless explicitly adopted by the user.
- Tie Compact's stopping rule to completion of the result and required checks, or a concrete blocker.
- In Extended, check relevant tools and retrieval coverage before inferring inability or absence, preserve unrelated work, and verify uncertain writes before retrying.
- Track all requested outcomes and unfinished items; retain the existing conditional visual-presentation guidance.

### Compatibility and maintenance

- Compact: 1,482 characters with LF; 1,493 with CRLF. Extended: 4,921 with LF; 4,954 with CRLF. Counts include the final newline.
- Add versioned v5.1 source files and restore the v5 pages to their published snapshots. Existing v5 tags and downloads are unchanged.
- Keep generated TXT attachments canonical LF and validate both line-ending limits.
- Update the README, feedback form, and release instructions. Release notes include this changelog entry.

No controlled model A/B evaluation has been completed. Technical checks are not evidence of improved accuracy, latency, or cost.

## v5 - 2026-10-20

- Publish Compact and Extended variants with task-adaptive review, proportionate verification, authorized task completion, source fidelity, and conditional rich presentation.
- Preserve upstream v1-v4 history and attribution.
- Published prompt sizes: 1,394 characters for Compact and 4,949 for Extended, including final LF newlines.

Earlier versions and their rationale remain available in the repository history and linked from the README.
