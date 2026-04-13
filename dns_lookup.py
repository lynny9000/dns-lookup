import dns.resolver

# Function: Perform DNS lookup for a specific record type
# Returns:
#   results - DNS records if found
#   None    - if no records or error occurs
def lookup(domain, record_type):
    try:
        return dns.resolver.resolve(domain, record_type)

    # No records of this type exist
    except dns.resolver.NoAnswer:
        return None

    # Domain does not exist
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist\n")
        return None

    # Catch all other DNS errors
    except:
        return None

# Infinite loop to allow continuous lookups
while True:
    # Get user input
    domain = input("Enter domain (or type 'exit' to quit): ")

    # Exit condition
    if domain.lower() == "exit":
        break

    # Clean input (remove https:// and paths)
    domain = domain.replace("https://", "").replace("http://", "").split("/")[0]

    print("\n--- DNS Lookup ---")
    print("Domain:", domain)

    # A Records (IPv4 addresses)
    print("\nA Records:")
    results = lookup(domain, 'A')
    if results:
        for r in results:
            print(f"  {r}")
    else:
        print("  None")

    # AAAA Records (IPv6 addresses)
    print("\nAAAA Records:")
    results = lookup(domain, 'AAAA')
    if results:
        for r in results:
            print(f"  {r}")
    else:
        print("  None")

    # MX Records (mail servers for domain)
    print("\nMX Records:")
    results = lookup(domain, 'MX')
    if results:
        for r in results:
            print(f"  {r.exchange}")
    else:
        print("  None")

    # CNAME Records (aliases pointing to another domain)
    print("\nCNAME Records:")
    results = lookup(domain, 'CNAME')
    if results:
        for r in results:
            print(f"  {r}")
    else:
        print("  None")

    # TXT Records (extra information such as SPF, verification, etc.)
    print("\nTXT Records:")
    results = lookup(domain, 'TXT')
    if results:
        for r in results:
            print(f"  {r}")
    else:
        print("  None")

    print("\n" + "-" * 40 + "\n")