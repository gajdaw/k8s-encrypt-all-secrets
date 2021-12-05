import subprocess

class CommandExecutor(object):

    def run_str_command(self, command):
        cmd = command.split()
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
