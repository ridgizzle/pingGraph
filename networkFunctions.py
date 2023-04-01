import subprocess


def ping(ip_address):
    """Pings a device and returns True if it's reachable, False otherwise"""
    # Construct the ping command
    command = ['ping', '-n', '1', '-w', '1000', ip_address]

    # Try to run the command
    try:
        subprocess.check_output(command)
        return True
    except subprocess.CalledProcessError:
        return False


