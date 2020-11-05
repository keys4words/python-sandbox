import logging

class NewFuncFilter(logging.Filter):
    def filter(self, record):
        print(record.my_name)
        return record.funcName == 'new_func'


logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'std_format': {
            'format': '{asctime} - {levelname} - {name} - {module}:{funcName}:{lineno} - {message}',
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
            'filters': ['new_filter']
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console']
            #'propagate': False
        }
    },

    'filters': {
        'new_filter': {
            '()': NewFuncFilter
        }
    },
    # 'root': {}   # '': {}
    # 'incremental': True
}
