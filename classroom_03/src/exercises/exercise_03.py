"""
Filter and print message with severity equal to ERROR.
Data example: {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
"""

try:
    log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
    
    if log['level'] == 'ERROR':
        print(log['message'])
except ValueError as e:
    print(e)