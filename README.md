# Flask Micro Api App

Basic flask app with routes and endpoints for testing local servers and services in micro api framework

## WSGI App Hosting
- https://www.devdungeon.com/content/run-python-wsgi-web-app-waitress

### Development Server
- flask --app app run --debug
- waitress-serve --host 127.0.0.1 --port 5000 app:app

### Production Server
- waitress-serve --host 0.0.0.0 app:app

### Systemctl Service Integration
First you need to create a virtual environment for the root user leveraging same principles as non-root user.
The reason for this is we want PipFile to manage the environment and dependencies. This way we can 
test upgrades to code and python for non-root with feature branches without affecting production services.
Upgrades for production services should be tested with parallel endpoints and real calls through database and services.
Once verified, then we can go through process of restarting with new service. A rollback plan is required as one
might encounter issues. The most straightforward way is to leverage release branches of code. This way a rollback can 
happen within minutes, if not less.

```shell
sudo -i (login with root privileges)
yum install python (ensure that pyton 3 is being installed)
# If pip does not already exist, run following command
python -m ensurepip --upgrade
# If pipenv does not already exist, run following command
python -m pip install pipenv

# !! EXIT SUDO !!
# Otherwise when trying to run pipenv, error will occur: "Error: the command waitress-serve could not be found wihtin PATH or Pipfile's [Scripts]"
# Install virtual environment letting Pipfile manage the packages
cd /home/user/flask && python -m pip install pipenv && pipenv install
# Test local service as root
python -m pipenv run waitress-serve --host 0.0.0.0 main:app
```

Move necessary unit.service file to correct linux directories.
Restart Linux daemon
Start unit.service

```shell
sudo cp microapp.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl start microapp.service
sudo systemctl stop microapp.service
sudo systemctl restart microapp.service
sudo systemctl status microapp.service
```

To view any logs that you might encounter during startup.

```shell
# View general logs
journalctl -u microapp.service
# View last 25 entries
journalctl -u microapp.service -n 25
# View from last 5 minutes
journalctl -u microapp.service --since=-5m
# Tail the logs
journalctl -u microapp.service -f
```

Common troubleshooting issues when viewing logs:
"pipenv process not found" - must use direct call to pipenv binary
- /home/user/.local/bin/pipenv run waitress-serve --host 0.0.0.0 main:app
"217/User" - incorrect user listed in unit.service file. update to correct user where command is being run
- User=nonroot_user

## Api Listing
- /
- login
- login_auth
- logout
- hello
- hello/<name>
- hello-world
- user/<username>
- post/<post_id>
- upload
- upload-secure
- path/<sub_path>
- post_form
- projects
- about

## Notes

Unit configuration files are added in following directory to be seen by systemd.

```shell
/etc/systemd/system
chmod 777 unit.service
```

Each time you add or modify a unit file you must tell systemd to refresh its configuration:

```shell
sudo systemctl daemon-reload
```

If you've noticed that /etc/systemd/system contains symlinks to /lib/systemd/system, that is because
you will find that not everything under /lib is loaded under systemd control. It may only 
be needed to boot up once, rather than controlled and maintained by systemd throughout
entire lifecycle of a session.
Primary reason for difference in location is:
- https://unix.stackexchange.com/questions/206315/whats-the-difference-between-usr-lib-systemd-system-and-etc-systemd-system

Table View for Debian/Ubuntu architectures:

| Path                 | Description                  |
|----------------------|------------------------------|
| /etc/systemd/system  | Local configuration          |
| /run/systemd/system  | Runtime units                |
| /lib/systemd/system  | Units of installed packages  |

For logs and viewing of journal daemon managed by the linux server, use the following journalctl commands.

View the logs for the microblog service:
```shell
journalctl -u microapp
```

View the last 25 log entries for the microblog service:
```shell
journalctl -u microapp -n 25
```

View the logs for the microblog service from the last five minutes:
```shell
journalctl -u microapp --since=-5m
```

Tail the logs for the microblog service:
```shell
journalctl -u microapp -f
```
