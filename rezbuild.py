import os
import os.path
import shutil
import stat
import subprocess


def build(source_path, build_path, install_path, targets):

    def _build():
        # Run normal python setup build
        setup_py = os.path.join(source_path, 'setup.py')
        proc = subprocess.Popen(['python', setup_py, 'build'], stdout=subprocess.PIPE, cwd=source_path)
        stdout, stderr = proc.communicate()
        if stdout:
            print stdout
        if stderr:
            print stderr

        # Move Python libraries to build location
        src = os.path.join(source_path, 'build', 'lib')
        dest = os.path.join(build_path, 'python')
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.move(src, dest)

        # Create scripts/bins for entry points
        pass

    def _install():
        # Copy build python libraries
        # Copy Scripts/entry points
        for name in ['python', 'bin']:
            src = os.path.join(build_path, name)
            dest = os.path.join(install_path, name)
            if os.path.exists(dest):
                shutil.rmtree(dest)
            if os.path.exists(src):
                shutil.copytree(src, dest)

    _build()

    if "install" in (targets or []):
        _install()
