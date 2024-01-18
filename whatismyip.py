import click
import requests


@click.command()
def cli():
    """Print your public IP address."""
    ip = requests.get('http://api.ipify.org').text
    click.echo(ip)
