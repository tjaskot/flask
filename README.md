# Flask Micro Api App

Basic flask app with routes and endpoints for testing local servers and services in micro api framework

## WSGI App Hosting
- https://www.devdungeon.com/content/run-python-wsgi-web-app-waitress

### Development Server
- flask --app app run --debug
- waitress-serve --host 127.0.0.1 --port 5000 app:app

### Production Server
- waitress-serve --host 127.0.0.1 app:app

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
