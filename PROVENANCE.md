# Source and report integrity

The [integrity manifest](provenance/import-manifest.json) records byte counts,
SHA256 hashes, and Git blob identities for 17 baseline files: the two all-field
research notes, the all-field and audit experiment packages, and the MIT license.
Its source commit and original identities support comparison with the imported
scientific record. Documentation amendments have current checksums alongside
those original identities.

Each experiment's `MANIFEST.json` pins its executable files, input fixtures,
reference report, and any shared decoder dependency. The verifiers run the code
in temporary storage and compare the output exactly with the reference reports.

The dated JSON verification records identify the files and executions checked
at their recorded commits. Their hashes refer to those revisions.

See the [verification guide](docs/VERIFICATION.md) for reproduction commands.
