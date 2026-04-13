# DNS Lookup Tool

A Python-based DNS lookup tool that retrieves common DNS records for a given domain.

## Features
- Retrieves A (IPv4) records
- Retrieves AAAA (IPv6) records
- Retrieves MX (mail server) records
- Retrieves CNAME (alias) records
- Retrieves TXT records (SPF, verification, etc.)
- Handles invalid domains and missing records
- Accepts full URLs (auto-cleans input)
- Runs continuously until user exits

## How it works

The script uses the `dnspython` library to query DNS servers and retrieve different record types.

Key concepts:
- A record - maps domain to IPv4 address
- AAAA record - maps domain to IPv6 address
- MX record - defines mail servers for a domain
- CNAME record - alias pointing to another domain
- TXT record - stores extra data (SPF, verification, etc.)

## Usage

Run:

python dns_lookup.py

Example:

Enter domain (or type 'exit' to quit): google.com

Output:

--- DNS Lookup ---
Domain: google.com

A Records:
  209.85.202.102
  209.85.202.139
  209.85.202.100

AAAA Records:
  2a00:1450:400b:c02::8a
  2a00:1450:400b:c02::65

MX Records:
  smtp.google.com.

CNAME Records:
  None

TXT Records:
  "v=spf1 include:_spf.google.com ~all"

----------------------------------------

## Notes

- Uses `dnspython` for DNS queries
- Not all domains have all record types
- TXT records may contain SPF and verification data
- Input URLs are automatically cleaned