def convert_to_type(value):
    # Try converting to int, float, and bool
    for converter in (int, float, lambda x: x.lower() == 'true' if x.lower() in ['true', 'false'] else x):
        try:
            return converter(value)
        except ValueError:
            pass
    # If all conversions fail, return the original string
    return value

def parse_ini(file_path):
    config = {}
    current_section = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            
            if line.startswith(";"):
                continue

            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1]
                config[current_section] = {}
            elif '=' in line:
                key, value = line.split('=', 1)
                key, value = key.strip(), value.strip()
                config[current_section][key] = convert_to_type(value)

    return config

# Example usage:
config_file = 'example.ini'
parsed_config = parse_ini(config_file)

# Accessing values
value = parsed_config.get('Section1', {}).get('Key1')
print(f'Value from config: {value}, Type: {type(value).__name__}')