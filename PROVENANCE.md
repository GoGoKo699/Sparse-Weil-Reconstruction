# Provenance

The initial research baseline is imported from
[Quantum-Assisted-Algorithm-Discovery at 9ef56e5a](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/tree/9ef56e5af6c7af452750b8cd035da6745f1d00c0).
The full source commit is `9ef56e5af6c7af452750b8cd035da6745f1d00c0`.
The source branch at extraction was `research/prx-quantum-phase2`.

The [import manifest](provenance/import-manifest.json) records each source path,
byte count, SHA256, and Git blob identity, plus the recovered checkpoint archive's
SHA256. All imported files were checked against the live pinned GitHub tree.

The preserved set is deliberately small:

- Notes 28 and 29, at their original `exploration/phase_2/` paths.
- The complete `experiments/all_field_reconstruction_v1/` directory.
- The complete `experiments/reconstruction_audit_v1/` directory.
- The MIT license, already byte-identical in the new repository.

These are 17 files. Their contents, expected reports, and internal manifests are
unchanged. Keeping the original paths preserves relative links and the audit's
pinned dependency on the sibling reconstruction decoder. No earlier experiment
is required to run these two verifiers.

The destination started at commit
`6a1954a35f2e24dbdc7485c4e8ec301702cd9d9d`, containing only README and LICENSE.
New root navigation, status, work order, and verification orchestration are
handoff additions, not alterations to the inherited scientific evidence.

Historical notes retain their original branch names, earlier checkpoint hashes,
research decisions, and execution statements. In particular, their statements
that a separate repository has not yet been created describe the time of writing.
The current project state is maintained in [STATUS.md](STATUS.md).

The preserved source records document the earlier primary-source inspections.
Importing those records does not imply that every source was reread during the
handoff. A bounded predecessor search is not a publication-priority certificate.

Future scientific changes should use a versioned successor directory and retain
these inputs and reference reports. Do not regenerate the preserved reports to
make a changed implementation pass verification.
