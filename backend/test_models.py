import requests

api_key = "AIzaSyBp7Yf75zO_9Rw3xw39hXcgvLsr6R2O6aU"
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

response = requests.get(url)
if response.status_code == 200:
    models = response.json().get('models', [])
    print("Available models that support generateContent:")
    print("=" * 60)
    for model in models[:20]:
        name = model['name']
        methods = model.get('supportedGenerationMethods', [])
        if 'generateContent' in methods:
            # Extract just the model name without 'models/' prefix
            short_name = name.replace('models/', '')
            print(f"✓ {short_name}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
