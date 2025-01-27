from lstty.core import list_serial_ports

def test_list_serial_ports():
    ports = list_serial_ports()
    assert isinstance(ports, list)