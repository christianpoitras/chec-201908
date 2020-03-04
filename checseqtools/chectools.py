import click

from checseqtools import DyadPositionFinder, PrepareGenomeCoverage


@click.group()
def chectools():
    pass


chectools.add_command(DyadPositionFinder.dyadposition)
chectools.add_command(PrepareGenomeCoverage.prepgenomecov)

if __name__ == '__main__':
   chectools()
