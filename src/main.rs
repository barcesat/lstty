use serialport::available_ports;
use pretty_env_logger;
#[macro_use] extern crate log;

fn main() {

    // initialise logging
    pretty_env_logger::init();
    info!("lstty - list serial ports");

    // print serial ports
    match available_ports() {

        Ok(ports) => {

            info!("{} serial ports found:", ports.len());
            for port in ports {

                // determine port details string
                let mut details = String::new();

                // add port type
                details.push_str(format!("{:9}", match port.port_type {
                    serialport::SerialPortType::BluetoothPort => "bluetooth",
                    serialport::SerialPortType::PciPort       => "pci",
                    serialport::SerialPortType::UsbPort(_)    => "usb",
                    serialport::SerialPortType::Unknown       => "unknown",
                }).as_str());

                // if the port is a usb device, add extra info
                match port.port_type {
                    serialport::SerialPortType::UsbPort(info) => {
                        details.push_str(
                            format!("{:04x}:{:04x} {}", 
                                info.vid, info.pid, 
                                match info.product {
                                    Some(name) => name.to_string(),
                                    None => "".to_string(),
                                }
                        ).as_str());
                    }

                    // ignore if not a usb device
                    _ => {}
                }

                // print port details
                println!("{:14} {}",  port.port_name, details);
            }

        }

        Err(e) => {
            error!("Failed to retrieve serial ports: {e}");
        }

    }
}
