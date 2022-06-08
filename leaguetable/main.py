import sys
import re
import click

def compute_league_table(scores: str):
    """
    Given a stringified list of scores of matches, computes a league table sorted by scores
    and then alphabetically where teams have the same league points.

    Arguments:
        scores: A string containing a list of matches' scores with each match score in a seperate line.
    
    Returns:
        A dictionary object representing the computed league table.
    """

    teams_and_scores = {}
    for line in scores:
        each_game = line.strip().split(',')
        team1 = " ".join(re.findall(r'\b[^\d\W]+\b', each_game[0])).strip()
        team2 = " ".join(re.findall(r'\b[^\d\W]+\b', each_game[1])).strip()
        team1_score = re.findall(r'\d+$', each_game[0])
        team2_score = re.findall(r'\d+$', each_game[1])

        if team1_score > team2_score:
            teams_and_scores[team1] = teams_and_scores[team1] + 3 if team1 in teams_and_scores else 3
        elif team1_score == team2_score:
            teams_and_scores[team1] = teams_and_scores[team1] +1 if team1 in teams_and_scores else 1
        else:
            teams_and_scores[team1] = teams_and_scores[team1] + 0 if team1 in teams_and_scores else 0

        if team2_score > team1_score:
            teams_and_scores[team2] = teams_and_scores[team2] + 3 if team2 in teams_and_scores else 3
        elif team2_score == team1_score:
            teams_and_scores[team2] = teams_and_scores[team2] + 1 if team2 in teams_and_scores else 1
        else:
            teams_and_scores[team2] = teams_and_scores[team2] + 0 if team2 in teams_and_scores else 0

    sorted_by_points = sorted(
        teams_and_scores.items(), key=lambda x: (-x[1], x[0]))
    formatted_with_pts = map(lambda x: (x[0], str(
        x[1]) + " pts" if x[1] > 1 or x[1] == 0 else str(x[1]) + " pt"), dict(sorted_by_points).items())

    return dict(formatted_with_pts)


@click.command()
@click.option(
    "-f",
    "--scores-file",
    help="Select a file containing scores, in seperate lines, for several matches.",
    type=click.File("r")
)
@click.option(
    "-s",
    "--scores",
    help="Enter individual match scores, each with this flag.",
    multiple=True
)
@click.option(
    "-o",
    "--file-output",
    help="File to write table to. Omit this flag to just display the league table on screen.",
    type=click.File("w", lazy=True),
)
def cli(scores_file, scores, file_output):
    """
    Reads a file or individual input containing match scores and then computes and outputs the resulting league table.
    """

    if scores_file is None and not all(scores):
        click.echo("Error: You must either provide a scores file or enter score for each match with the '-s' or '--scores' option.")
        return

    output = compute_league_table(scores_file if scores_file is not None else scores)
    table_formatted = str("\n".join(f'{index + 1}. {k}, {v:9}' for index, (k, v) in enumerate(output.items())))
    click.echo(f"League Table:\n\n{table_formatted}", file=file_output)


if __name__ == "__main__":
    cli()
