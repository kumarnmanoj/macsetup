from fabric2 import task

import sys


def check_whether_installed_via_brew_cask(c, package):
    cask_list_output = c.run('brew cask list | grep "{}"'.format(package))

    if cask_list_output.stdout.strip() == package:
        print("Seems {} is already installed".format(package))
        return True

    return False

@task
def install_homebrew(c):
    brew_available = c.run("which brew")

    if brew_available.ok:
        print("homebrew already installed :)")
        return

    c.run('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)')


@task(pre=[install_homebrew])
def install_virtualbox(c):

    if check_whether_installed_via_brew_cask(c, "virtualbox"):
        return

    c.run("brew update")
    c.run("brew tap caskroom/cask")
    c.run("brew cask install virtualbox")


@task
def install_kubectl(c):
    c.run("curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl")
    c.run("chmod +x ./kubectl")
    c.sudo("mv ./kubectl /usr/local/bin/kubectl")


@task(pre=[install_virtualbox, install_kubectl])
def install_minikube(c):

    if check_whether_installed_via_brew_cask(c, "minikube"):
        return

    c.run("brew cask install minikube")

@task
def install_okta_cli(c):
    c.run("curl 'https://raw.githubusercontent.com/oktadeveloper/okta-aws-cli-assume-role/master/bin/install.sh' --output okta_cli.sh")
    c.run("echo $HOME/blah")
    c.run("bash okta_cli.sh -i", hide=True)
    c.run("echo 'export PATH=$HOME/.okta/bin:$PATH' >> $HOME/.mk_exports")
    c.run("echo 'source $HOME/.okta/bash_functions' >> $HOME/.mk_functions")