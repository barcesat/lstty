import serial.tools.list_ports
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("lstty - list serial ports")

    try:
        # Get the list of available ports
        ports = serial.tools.list_ports.comports()
        logger.info(f"{len(ports)} serial ports were found:")

        # Print table headers
        print(f"{'Port':<15}\t|\t{'Type':<10}\t|\t{'Details'}")
        print("-" * 70)

        for port in ports:
            # Determine port type and details
            port_type = "unknown"
            hwid = port.hwid or "N/A"
            details = ""

            if port.hwid.startswith("USB"):
                port_type = "usb"
                usb_info = port.hwid.split(" ")[1].split(":") if len(port.hwid.split(" ")) > 1 else ["unknown", "unknown"]
                vid = usb_info[0] if len(usb_info) > 0 else "unknown"
                pid = usb_info[1] if len(usb_info) > 1 else "unknown"
                details = f"{vid}:{pid} {port.description or ''}".strip()
            elif "BLUETOOTH" in port.description.upper():
                port_type = "bluetooth"
                details = port.description
            elif "PCI" in port.description.upper():
                port_type = "pci"
                details = port.description

            # Print the row
            print(f"{port.device:<15}\t|\t{port_type:<10}\t|\t{details}")

    except Exception as e:
        logger.error(f"Failed to retrieve serial ports: {e}")

if __name__ == "__main__":
    main()
