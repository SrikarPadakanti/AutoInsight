from parser.email_reader import connect_email, fetch_target_emails, parse_email, store_to_db

def run_email_parser():
    print("🔌 Connecting to email server...")
    server = connect_email()
    print("📬 Fetching emails...")
    raw_emails = fetch_target_emails(server)
    print(f"📦 Total emails fetched: {len(raw_emails)}")

    for idx, raw in enumerate(raw_emails):
        print(f"\n📨 Processing email #{idx + 1}...")
        parsed_data = parse_email(raw)

        if parsed_data:
            print(f"✅ Extracted {len(parsed_data)} rows.")
            store_to_db(parsed_data)
        else:
            print("❌ No structured table found.")

if __name__ == "__main__":
    run_email_parser()