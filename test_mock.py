from unittest import mock


def yes_or_no():
    answer = input("Do you want to quit? > ")
    if answer == "yes":
        print("Quitter!")
    elif answer == "no":
        return("Awesome!")
    else:
        return("BANG!")


def test_quitting():

    with mock.patch('builtins.input', return_value="yes"):
        assert yes_or_no() == "Quitter!"

    with mock.patch('builtins.input', return_value="no"):
        assert yes_or_no() == "Awesome!"

def test_patching():
    input_values = [1, 3]
 
    def mock_input(s):
        print(s, end='')
        return input_values.pop(0)
    app.input = mock_input
 
    app.main()
 
    out, err = capsys.readouterr()
 
    assert out == "".join([
        'First: ',
        'Second: ', 
        'The result is 5\n',
    ])
 
    assert err == ''
