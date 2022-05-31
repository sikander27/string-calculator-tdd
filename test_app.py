import app
 
# def test_app():
#     input_values = [2, 3]
#     output = []
 
#     def mock_input(s):
#         output.append(s)
#         return input_values.pop(0)
#     app.input = mock_input
#     app.print = lambda s : output.append(s)
 
#     app.main()
 
#     assert output == [
#         'First: ',
#         'Second: ', 
#         'The result is 5',
#     ]

def test_app(capsys):
    input_values = [2, 3]
 
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