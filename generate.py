import tomllib
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


SOURCE_FILE = Path("source.toml")
DEST_FILE = Path("uBlacklist.txt")


@dataclass(frozen=True)
class DomainEntry:
    domain_name: str
    subdomains: list[str] | None = None
    include_base_domain: bool = True


last_updated = datetime.now(timezone.utc)


with open(SOURCE_FILE, "rb") as f:
    data = tomllib.load(f)

domain_entries: list[DomainEntry] = sorted(
    (DomainEntry(**domain_data) for domain_data in data["domains"]),
    key=lambda domain_entry: domain_entry.domain_name,
)

with open(DEST_FILE, "wt") as f:
    f.write(
        f"""---
name: AI Content Blocklist
homepage: https://github.com/agsimmons/ai-content-blocklist
last_updated: {last_updated.isoformat()}
---
"""
    )

    for domain_entry in domain_entries:
        f.write("\n")

        if domain_entry.include_base_domain:
            f.write(f"*://{domain_entry.domain_name}/*\n")

        if domain_entry.subdomains is not None:
            for subdomain in sorted(domain_entry.subdomains):
                f.write(f"*://{subdomain}.{domain_entry.domain_name}/*\n")
