# BreakTimer

## About this application

BreakTimer is a little application, that regularly notifies you to take a break.

## Dependencies

- Python (3.6)
- PyQt5 (5.9.2)
- fbs
- _for more information see see requirements/base.txt_

## Installation

### Executable file (only Linux)

#### Debian based distributions (including Ubuntu):

Install BreakTimer and receive automatic updates:

``` 
$ sudo apt-get install apt-transport-https
$ wget -qO - https://fbs.sh/Palexer/BreakTimer/public-key.gpg | sudo apt-key add -
$ echo 'deb [arch=amd64] https://fbs.sh/Palexer/BreakTimer/deb stable main' | sudo tee /etc/apt/sources.list.d/breaktimer.list
$ sudo apt-get update
$ sudo apt-get install breaktimer
```

Force an immediate update (if you have BreakTimer already installed):

```
$ sudo apt-get update -o Dir::Etc::sourcelist="/etc/apt/sources.list.d/breaktimer.list" -o Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0"
$ sudo apt-get install --only-upgrade breaktimer
```

Install BreakTimer WITHOUT receiving automatic updates:

Download [here](https://fbs.sh/Palexer/BreakTimer/BreakTimer.deb)

#### Arch based distributions (including Manjaro)

Install BreakTimer and receive automatic updates:

``` 
$ curl -O https://fbs.sh/Palexer/BreakTimer/public-key.gpg && sudo pacman-key --add public-key.gpg && sudo pacman-key --lsign-key 4F90A4D22E60B34F54D8B638C47C1F143142908A && rm public-key.gpg
$ echo -e '\n[BreakTimer]\nServer = https://fbs.sh/Palexer/BreakTimer/arch' | sudo tee -a /etc/pacman.conf
$ sudo pacman -Syu breaktimer
```

Force an immediate update (if you have BreakTimer already installed):

```
$ sudo pacman -Syu --needed breaktimer
```

Install BreakTimer WITHOUT receiving automatic updates:

Download [here](https://fbs.sh/Palexer/BreakTimer/BreakTimer.pkg.tar.xz)

#### Fedora and CentOS

Install BreakTimer and receive automatic updates:
``` 
$ sudo rpm -v --import https://fbs.sh/Palexer/BreakTimer/public-key.gpg
$ sudo dnf config-manager --add-repo https://fbs.sh/Palexer/BreakTimer/rpm/BreakTimer.repo
$ sudo dnf install breaktimer

```
_On CentOS, replace 'dnf' by 'yum' and 'dnf config-manager' by 'yum-config-manager'._

Force an immediate update

on Fedora:
```
$ sudo dnf upgrade breaktimer --refresh
```

on CentOS:
```
sudo yum clean all && sudo yum upgrade breaktimer
```

Install BreakTimer WITHOUT receiving automatic updates:
```
$ https://fbs.sh/Palexer/BreakTimer/BreakTimer.rpm
```

## License

GPL v3
