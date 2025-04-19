def clear_log_file():
    import os
    log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'myapp.log')
    with open(log_file_path, 'w'):
        pass


clear_log_file()
