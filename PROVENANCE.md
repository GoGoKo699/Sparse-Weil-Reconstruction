# Provenance

The [preservation manifest](provenance/import-manifest.json) identifies the
17-file research baseline and records each file's path, byte count, SHA256,
and Git blob identity. It retains the source metadata needed to verify the
baseline independently.

The preserved set is deliberately small:

- Notes 28 and 29, at their original `exploration/phase_2/` paths.
- The complete `experiments/all_field_reconstruction_v1/` directory.
- The complete `experiments/reconstruction_audit_v1/` directory.
- The MIT license.

These are 17 files. Their contents, expected reports, and internal manifests are
unchanged. Keeping the original paths preserves relative links and the audit's
pinned dependency on the sibling reconstruction decoder. No earlier experiment
is required to run these two verifiers.

Historical notes retain their checkpoint hashes, research decisions, and
execution statements. They describe the state at the time of writing.
The current project state is maintained in [STATUS.md](STATUS.md).

Source records document the primary-source inspections performed at each
checkpoint. A bounded predecessor search is not a publication-priority certificate.

Future scientific changes should use a versioned successor directory and retain
these inputs and reference reports. Do not regenerate the preserved reports to
make a changed implementation pass verification.
