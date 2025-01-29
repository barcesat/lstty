# lstty

`lstty` is a Python-based command-line tool to list available serial ports. 
It prints the name of the serial port, the type of port, and if it's a USB port, it will include the VID, PID, and product name. 
Currently, there are no command-line parameters—just run `lstty` to see the output.

## Features

- Cross-platform tool (tested on Linux and Win 10).
- Lists available serial ports.
- Displays port type (e.g., USB, Bluetooth, PCI, etc.).
- Includes USB-specific details like VID, PID, and product description.
- Outputs information in a clear ASCII table format.

### Example Output
Linux:
```text
$ lstty
Port            Type       Details
----------------------------------------------------------------------
/dev/ttyS0      unknown    
/dev/ttyS1      unknown    
/dev/ttyACM0    usb        VID:PID=2E8A RaspberryPi Pico
```

Windows:
```text
> lstty
Port            |       Type            |       Details
----------------------------------------------------------------------
COM24           |       bluetooth       |       Standard Serial over Bluetooth link (COM24)
COM6            |       usb             |       VID:PID=413C DW5821e Snapdragon X20 LTE Diagnostic (COM6)
COM22           |       bluetooth       |       Standard Serial over Bluetooth link (COM22)
COM3            |       usb             |       VID:PID=0403 USB Serial Port (COM3)
COM7            |       usb             |       VID:PID=413C DW5821e Snapdragon X20 LTE Modem
```

## Installation

To install `lstty`, clone this repository and run:

```bash
pip install .
```

Currently, `lstty` is not available on PyPI.

## Dependencies

This tool relies on the following Python libraries:
- [pyserial](https://github.com/pyserial/pyserial) – for serial port information.
- [click](https://click.palletsprojects.com/en/stable/) – for the command-line interface.

Install them via `pip`:

```bash
pip install pyserial click
```
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Acknowledgments

This tool was inspired by the original [lstty](https://github.com/atctwo/lstty) project by [@atctwo](https://github.com/atctwo). 
Special thanks to the original author for creating the Rust-based implementation that served as the foundation for this Python adaptation.
