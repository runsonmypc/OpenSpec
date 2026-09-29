# Recursive OpenSpec listing captures

These PNGs faithfully render captured stdout from the source-built OpenSpec CLI on a temporary fixture with fictional product directories and sample items. The adjacent text files are captured stdout. No private repository content or paths are included.

Commands: `openspec list`, `openspec list --specs`, with FORCE_COLOR=1 to capture ANSI styling.
The PNGs use a near-black terminal palette with soft teal, amber, green, and gray. The CLI sets no background color. The original ANSI captures and rendering script are included.
The narrow capture runs the same built CLI with stdout columns set to 50.

Fixture libraries: openspec/, batch-worker/openspec/, web-client/openspec/, help-center/openspec/.
Screenshots are hosted separately from the implementation PR so the code diff contains no binary artifacts or demonstration fixtures.
