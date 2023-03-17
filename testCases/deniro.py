testCases = {
    'count': 87,
    'mean': [
            {'col': 'Year', 'value': 1995.9770114942528},
            {'col': 'Score', 'value': 58.195402298850574},
            {'col': 'Title', 'value': None},
    ],
    'std': [
        {'col': 'Year', 'value': 12.864436419920098},
        {'col': 'Score', 'value': 27.90576881012477},
        {'col': 'Title', 'value': None}
    ],
    'filter': [
        {'col': 'Year', 'filter': '1977', 'result': [{'Year': '1977', 'Score': '47', 'Title': '1900'}, {
                'Year': '1977', 'Score': '67', 'Title': 'New York'}]},
        {'col': 'Score', 'filter': '80', 'result': [{'Year': '1987', 'Score': '80', 'Title': 'The Untouchables'}, {
                'Year': '1995', 'Score': '80', 'Title': 'Casino'}, {'Year': '1996', 'Score': '80', 'Title': "Marvin's Room"}]},
        {'col': 'Year', 'filter': None, 'result': None}
    ]
}
