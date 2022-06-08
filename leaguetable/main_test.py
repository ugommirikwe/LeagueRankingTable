from click.testing import CliRunner
from testfixtures import compare
from leaguetable import main

sample_scores = [
    "--scores", "Shalke FC 32, City 42", 
    "-s", "Lions 3, Snakes 3", 
    "-s", "Tarantulas 1, FC Awesome 0",
    "-s", "Lions 1, FC Awesome 1",
    "-s", "Tarantulas 3, Snakes 1",
    "-s", "Lions 4, Grouches 0",
]

def test_cli_output_to_stdin():
    runner = CliRunner()
    result = runner.invoke(main.cli, sample_scores)

    compare(result.output, """League Table:
1. Tarantulas, 6 pts    
2. Lions, 5 pts    
3. City, 3 pts    
4. FC Awesome, 1 pt     
5. Snakes, 1 pt     
6. Grouches, 0 pts    
7. Shalke FC, 0 pts""", trailing_whitespace=False)

    assert result.exit_code == 0


def test_cli_output_to_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("table.txt", "w"):
            pass

        result = runner.invoke(main.cli, sample_scores + ["-o", "table.txt"])
        assert result.exit_code == 0

        with open("table.txt") as t:
            league_table = t.read()
            compare(league_table, """League Table:
1. Tarantulas, 6 pts    
2. Lions, 5 pts    
3. City, 3 pts    
4. FC Awesome, 1 pt     
5. Snakes, 1 pt     
6. Grouches, 0 pts    
7. Shalke FC, 0 pts""", trailing_whitespace=False)

            t.close()


if __name__ == '__main__':
    test_cli_output_to_stdin()
    test_cli_output_to_file()
