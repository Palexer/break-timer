# Break Timer

## About this application

Break Timer is a little application, that regularly notifies you to take a break.

## Dependencies

- Python 3
- PyQt5

## Installation

### Executable file (only Linux)

#### Debian based distributions (including Ubuntu):

**Install BreakTimer and receive automatic updates:**

``` 
$ sudo apt-get install apt-transport-https
$ wget -qO - https://fbs.sh/Palexer/BreakTimer/public-key.gpg | sudo apt-key add -
$ echo 'deb [arch=amd64] https://fbs.sh/Palexer/BreakTimer/deb stable main' | sudo tee /etc/apt/sources.list.d/breaktimer.list
$ sudo apt-get update
$ sudo apt-get install breaktimer
```

**Force an immediate update (if you have BreakTimer already installed):**

```
$ sudo apt-get update -o Dir::Etc::sourcelist="/etc/apt/sources.list.d/breaktimer.list" -o Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0"
$ sudo apt-get install --only-upgrade breaktimer
```

**Install BreakTimer WITHOUT receiving automatic updates:**

#### Arch based distributions (including Manjaro)

**Install BreakTimer and receive automatic updates:**

``` 
$ curl -O https://fbs.sh/Palexer/BreakTimer/public-key.gpg && sudo pacman-key --add public-key.gpg && sudo pacman-key --lsign-key 4F90A4D22E60B34F54D8B638C47C1F143142908A && rm public-key.gpg
$ echo -e '\n[BreakTimer]\nServer = https://fbs.sh/Palexer/BreakTimer/arch' | sudo tee -a /etc/pacman.conf
$ sudo pacman -Syu breaktimer
```

**Force an immediate update (if you have BreakTimer already installed):**

```
$ sudo pacman -Syu --needed breaktimer
```

**Install BreakTimer WITHOUT receiving automatic updates:**

Download [https://fbs.sh/Palexer/BreakTimer/BreakTimer.pkg.tar.xz](here)


### Using Python (all operating systems)

1. Install Python 3
2. Install the dependencies:
    > ``` pip3 install -r requirements/base.txt ```
3. Run the main.py file using Python 3
