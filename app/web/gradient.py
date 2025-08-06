def gradients(name: str):
    options = {
        'metal': 'bg-gradient-to-r from-slate-500 to-slate-800',
        'verbena': 'bg-gradient-to-r from-violet-600 to-indigo-600',
        'standard': 'bg-gradient-to-br from-blue-800 via-blue-600 to-blue-500'
    }
    return options.get(name) if options.get(name) else options['standard']
