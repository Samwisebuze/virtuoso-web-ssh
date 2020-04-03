# virtuoso-web-ssh

Note: This is a hacky fork of [huashengdun/webssh](https://github.com/huashengdun/webssh) to work with Docker containers and a work in progress. It's somewhat stable, but not completely secure just yet.

Service to connect to an ssh server via a simple web interface with an xterm.js tty. Generalized to support connecting to any Docker container (with standard user + pass. A modified version of [huashengdun/webssh](https://github.com/huashengdun/webssh) - uses standard connection details (username and pass) for simplicity.

The idea:

```
+---------+     http     +--------+    ssh    +-------------------------+
| browser | <==========> | webssh | <=======> | ssh server in container |
+---------+   websocket  +--------+    ssh    +-------------------------+
```

## Usage

Build and run with standardized username + password (for development purposes):

```sh
$ docker build -t virtuoso-web-ssh .
$ docker run -it --rm --name virtuoso-web-ssh \
    -p 8888:8888 \
    -e "STANDARD_CONTAINER_USERNAME=<username>" \
    -e "STANDARD_CONTAINER_PASSWORD=<password>" \
    -v /var/run/docker.sock:/var/run/docker.sock \
    virtuoso-web-ssh
```

Then, open `http://localhost:8888?hostname=<docker_container_id>` in your web browser.

## TODO

- [ ] user authentication
