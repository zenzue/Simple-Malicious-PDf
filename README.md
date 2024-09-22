# PDF Payload Injector

This script allows you to inject a custom payload into a PDF file, which can be particularly useful for testing or demonstration purposes in security research. The script adds a specifically formatted entry into the PDF structure, targeting a specific section of the document.

## Warning

This tool is intended for educational and research purposes only. The author is not responsible for any misuse or damage resulting from the use of this tool. Always ensure you have permission to test and use this tool on any PDF documents and systems.

## Installation

To run this script, you need Python installed on your system. This script is compatible with Python 3.x.

No additional libraries are required beyond the Python standard library. Simply clone this repository or download the script to your local machine.

## Usage

To use the script, you need to pass the path to the PDF file and an IP address to be included in the payload. Here's how to run the script from the command line:

```bash
python pdf_payload_injector.py path_to_pdf_file ip_address
```

### Example

```bash
python pdf_payload_injector.py example.pdf --ip_address 192.168.1.1
```
```bash
python pdf_payload_injector.py example.pdf --domain_name example.com
```
```bash
python pdf_payload_injector.py example.pdf --ip_address 192.168.1.1 --domain_name example.com
```

This command will modify `example.pdf` by injecting the specified payload containing the IP address `192.168.1.1` and create a new file `example.pdf.payload.pdf`.

## Disclosure

The issue exploited by this tool was previously disclosed both to Adobe and Foxit. Foxit fixed the issue as part of their 9.1 release. Adobe addressed this vulnerability as part of the Adobe Reader version released in May (CVE-2018-4993).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
