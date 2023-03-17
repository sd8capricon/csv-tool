cases = {
    'hw_25000.csv':
    {
        'count': 25000,
        'mean': [
            {'col': 'Height(Inches)', 'value': 67.99328226439978},
            {'col': 'Weight(Pounds)', 'value': 127.07929911279915}
        ],
        'std': [
            {'col': 'Weight(Pounds)', 'value': 11.661111842424004},
        ],
        'filter': [
            {'col': 'Height(Inches)', 'filter': '70',
             'result': [{'Index': '1', 'Height(Inches)': '70', 'Weight(Pounds)': '112.9925'}]},
            {'col': 'Weight(Pounds)', 'filter': '82.38298',
                    'result': [{'Index': '728', 'Height(Inches)': '63.1255', 'Weight(Pounds)': '82.38298'}, {'Index': '24611', 'Height(Inches)': '66.56804', 'Weight(Pounds)': '82.38298'}]},
        ]
    },
    'deniro.csv':
    {
        'count': 87,
        'mean': [
            {'col': 'Year', 'value': 1995.9770114942528},
            {'col': 'Score', 'value': 58.195402298850574},
            {'col': 'Title', 'value': None},
        ],
        'filter': [
            {'col': 'Year', 'filter': '1977', 'result': [{'Year': '1977', 'Score': '47', 'Title': '1900'}, {
                'Year': '1977', 'Score': '67', 'Title': 'New York'}]},
            {'col': 'Score', 'filter': '80', 'result': [{'Year': '1987', 'Score': '80', 'Title': 'The Untouchables'}, {
                'Year': '1995', 'Score': '80', 'Title': 'Casino'}, {'Year': '1996', 'Score': '80', 'Title': "Marvin's Room"}]},
            {'col': 'Year', 'filter': None, 'result': None}
        ]
    }
}
