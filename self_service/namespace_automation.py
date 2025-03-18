import os
import git
import subprocess

# Configuration
GIT_REPO_PATH = "/tmp/namespace-repo" # path to the repo inside the container
GIT_REMOTE_URL = "https://github.com/Hashlama-016/Argo-Configs.git"
GIT_BRANCH = "dev"
VALUES_FILE_PATH = "rbac/values.yaml"  # Path to the Helm values file inside the repo

def get_env_variables():
    """Fetch namespace name from environment variables."""
    namespace = os.getenv("NAMESPACE_NAME")

    if not namespace:
        raise ValueError("Missing required environment variable: NAMESPACE_NAME")

    return namespace

def clone_git_repo():
    """Clones the Git repository if not already cloned."""
    if not os.path.exists(GIT_REPO_PATH):
        print("Cloning Git repository...")
        git.Repo.clone_from(GIT_REMOTE_URL, GIT_REPO_PATH, branch=GIT_BRANCH)
    return git.Repo(GIT_REPO_PATH)

def update_values_file(namespace):
    """Uses yq to add a new namespace entry under teams in the Helm values file."""
    values_file = os.path.join(GIT_REPO_PATH, VALUES_FILE_PATH)

    if not os.path.exists(values_file):
        raise FileNotFoundError(f"Values file not found at {values_file}")

    # Run yq command to update the YAML file
    cmd = [
        "yq", "-i",
        f".teams += [\"{namespace}\"]",
        values_file
    ]
    
    print(f"Updating {VALUES_FILE_PATH} with new namespace (team): {namespace}")
    subprocess.run(cmd, check=True)

def push_to_git(namespace):
    """Pushes the updated values.yaml to Git."""
    repo = git.Repo(GIT_REPO_PATH)
    file_path = os.path.join(GIT_REPO_PATH, VALUES_FILE_PATH)

    repo.index.add([file_path])
    repo.index.commit(f"Added namespace {namespace} to values.yaml")
    origin = repo.remote(name="origin")
    origin.push()

    print(f"Namespace {namespace} added to {VALUES_FILE_PATH} and pushed to Git.")

if __name__ == "__main__":
    try:
        namespace_name = get_env_variables()
        repo = clone_git_repo()
        update_values_file(namespace_name)
        push_to_git(namespace_name)

        print(f"Namespace {namespace_name} added successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")




# Change values in - values.yaml namespaces (RBAC)  - team name+  chenage values in users - values.yml (adding the user + password) : using yq