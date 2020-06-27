import click

from demoflask.app import app, db
from demoflask.models import TestMethod


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    if drop:
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')


@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    """Generate fake messages."""
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo('Working...')

    for i in range(count):
        message = TestMethod(
            methodName=fake.name(),
            methodDesc=fake.name(),
            className=fake.name(),
            classDesc=fake.name(),
            fileName=fake.name(),
            fileDesc=fake.name(),
            moduleName=fake.name(),
            moduleDesc=fake.name(),
            author=fake.name()
        )
        db.session.add(message)

    db.session.commit()
    click.echo('Created %d fake messages.' % count)