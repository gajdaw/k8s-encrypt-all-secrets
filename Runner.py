import CommandExecutor

class Runner(object):

    def __init__(self):
        self._processor  = CommandExecutor.CommandExecutor()
        self._secrets = []

    def fetch(self):
        self._list_all_secrets()
        self._get_all_secrets()

    def _list_all_secrets(self):
        output = self._processor.run_str_command(
            "kubectl get secret --no-headers --all-namespaces -o custom-columns=NAME:.metadata.name,RSRC:.metadata.namespace"
        )
        for line in output.strip().split("\n"):
            parsed = line.split()
            self._secrets.append(parsed)

    def _get_all_secrets(self):
        self._processor.run_str_command("mkdir -p secret")
        for secret in self._secrets:
            output = self._processor.run_str_command(
                f"kubectl get secret {secret[0]} --namespace {secret[1]} -o yaml"
            )
            filename = f"secret/{secret[1]}-{secret[0]}.yaml"
            with open(filename, "w") as text_file:
                text_file.write(output)

    def _tar(self):
        self._processor.run_str_command("tar cf secret.tar secret")
        self._processor.run_str_command("rm -rf secret")

    def encrypt(self, email: str):
        self._tar()
        self._processor.run_str_command(f"gpg --encrypt --recipient {email} --output secret.tar.gpg secret.tar")
        self._processor.run_str_command("rm -rf secret.tar")

    def decrypt(self):
        self._processor.run_str_command("gpg --decrypt --output secret.tar secret.tar.gpg")
        self._processor.run_str_command("rm secret.tar.gpg")
        self._processor.run_str_command("tar xf secret.tar")
        self._processor.run_str_command("rm secret.tar")

