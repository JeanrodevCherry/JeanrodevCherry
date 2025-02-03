import openai
import subprocess
import os

# Set up API key & GitHub Token
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = "JeanrodevCherry"  # Replace with your GitHub username
REPO_URL = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/JeanrodevCherry.git"

# Function to generate code
def generate_code(prompt):
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content, response

# Function to write content to a file
def write_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

# Function to configure Git with authentication
def configure_git():
    subprocess.run(["git", "config", "--global", "user.name", GITHUB_USERNAME], check=True)
    subprocess.run(["git", "config", "--global", "user.email", f"{GITHUB_USERNAME}@users.noreply.github.com"], check=True)
    subprocess.run(["git", "remote", "set-url", "origin", REPO_URL], check=True)

# Function to commit and push files using Git
def commit_and_push(files, commit_message):
    try:
        # Ensure Git is configured
        configure_git()

        # Add files to Git
        subprocess.run(["git", "add"] + files, check=True)
        
        # Commit changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push to GitHub
        subprocess.run(["git", "push", "origin", "main"], check=True)  # Change branch if needed

        print("✅ Changes pushed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running Git command: {e}")

# === MAIN EXECUTION ===
if __name__ == "__main__":
    prompt = "Write a Python function to calculate Fibonacci numbers"
    #configure_git()

    generated_code, full_response = generate_code(prompt)

    # Define filenames
    code_file = "fibonacci.py"
    metadata_file = "README.txt"

    # Extract metadata
    metadata = f"AI Model: {full_response.model}\nTokens Used: {full_response.usage.total_tokens}\n\nFull Response:\n{full_response}"

    # Write files
    write_to_file(code_file, generated_code)
    write_to_file(metadata_file, metadata)

    # Commit and push changes
    commit_and_push([code_file, metadata_file], "Auto-generated Fibonacci function")

