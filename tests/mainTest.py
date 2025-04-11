from main import printNums

def test_printNums(capsys):
    printNums(3)
    captured = capsys.readouterr()
    assert captured.out == "0\n1\n2\n"
