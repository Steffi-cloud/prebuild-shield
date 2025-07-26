import yaml

def basic_check():
    with open("specs/sample-api.yaml") as f:
        spec = yaml.safe_load(f)
    assert spec.get("openapi", "").startswith("3."), "Invalid OpenAPI version"
    print("✔ OpenAPI version is valid")

if __name__ == "__main__":
    basic_check()
