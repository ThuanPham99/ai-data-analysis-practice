def load_data():
    return 'Data loaded'


def handle_missing_values(data):
    return data.dropna()

def summarize_data(data):
    return {
        "rows": len(data),
        "columns": len(data.columns),
    }