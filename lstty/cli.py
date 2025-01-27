import click
from .core import list_serial_ports

@click.command()
def main():
    """Command-line interface for listing serial ports."""
    ports = list_serial_ports()

    # Print table headers
    print(f"{'Port':<15}\t|\t{'Type':<10}\t|\t{'Details'}")
    print("-" * 70)

    for port in ports:
        print(f"{port['port']:<15}\t|\t{port['type']:<10}\t|\t{port['details']}")
