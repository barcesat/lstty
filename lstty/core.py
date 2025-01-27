import serial.tools.list_ports

def list_serial_ports():
    """Lists available serial ports."""
    try:
        # Get the list of available ports
        ports = serial.tools.list_ports.comports()
        result = []

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

            result.append({
            "port": port.device,
            "type": port_type,
            "hwid": hwid,
            "details": details
            })
            
        return result

    except Exception as e:
        logger.error(f"Failed to retrieve serial ports: {e}")
