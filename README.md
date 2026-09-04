# HTTPTrace

> Dependency-free HTTP diagnostics from the command line.

[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-111111?style=flat-square)](LICENSE)

HTTPTrace is a lightweight diagnostics CLI for inspecting HTTP requests, response status and safe response metadata.

## What it does

- Measures request timing
- Inspects HTTP status information
- Reports useful response metadata
- Keeps the implementation lightweight
- Works without third-party runtime dependencies

## Example

```bash
httptrace https://example.com
```

Use the CLI's built-in help for the complete command and option reference:

```bash
httptrace --help
```

## Design

```text
URL
 ↓
HTTP request
 ↓
status + timing + metadata
 ↓
terminal diagnostics
```

HTTPTrace is intended for **diagnostics and observability**, not unauthorized access or exploitation.

## Development

Run the repository's test suite before submitting changes.

## License

MIT. See [`LICENSE`](LICENSE).

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
