testCases = {
    'count': 25000,
    'mean': [
        {'col': 'Height(Inches)', 'value': 67.99328226439978},
        {'col': 'Weight(Pounds)', 'value': 127.07929911279915}
    ],
    'std': [
        {'col': 'Height(Inches)', 'value': 1.9016317307941983},
        {'col': 'Weight(Pounds)', 'value': 11.661111842424006},
    ],
    'filter': [
        {'col': 'Height(Inches)', 'filter': '70',
         'result': [{'Index': '1', 'Height(Inches)': '70', 'Weight(Pounds)': '112.9925'}]},
        {'col': 'Weight(Pounds)', 'filter': '82.38298',
         'result': [{'Index': '728', 'Height(Inches)': '63.1255', 'Weight(Pounds)': '82.38298'}, {'Index': '24611', 'Height(Inches)': '66.56804', 'Weight(Pounds)': '82.38298'}]},
    ]
}
