import click
from flask import Flask
from flask.cli import with_appcontext
from database.mock import cv

app = Flask(__name__)

@app.cli.command("cv")
@with_appcontext
def print_cv():
    """Prints the full cv to the console."""

    click.echo("== CONTACT ==")
    for k, v in cv.contact.model_dump().items():
        click.echo(f"{k.title()}: {v}")

    click.echo("\n== SKILLS ==")
    click.echo("Highlights:")
    for skill in cv.skills.highlights:
        click.echo(f"  - {skill}")
    click.echo("Technical:")
    for tech in cv.skills.technical:
        click.echo(f"  - {tech}")

    click.echo("\n== LANGUAGES ==")
    for lang in cv.languages.root:
        click.echo(f"- {lang}")

    click.echo("\n== EXPERIENCE ==")
    for job in cv.experience:
        click.echo(f"\n{job.title} at {job.company} ({job.start} - {job.end})")
        for bullet in job.bullets:
            click.echo(f"  • {bullet}")

    click.echo("\n== EDUCATION ==")
    for edu in cv.education:
        location = f" ({edu.location})" if edu.location else ""
        click.echo(f"- {edu.degree} at {edu.institution}{location}")

    click.echo("\n== INTERESTS ==")
    for interest in cv.interests.root:
        click.echo(f"- {interest}")
