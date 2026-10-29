# Daily networking agent

A scheduled Claude Code task runs every morning (US Eastern), reads `profile.md` and `instructions.md`,
finds 5 people worth reaching out to, saves the digest to `digests/`, and records them in `contacted.md`
so nobody is suggested twice.

To change what it looks for, edit `profile.md`.
