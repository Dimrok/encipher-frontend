# A simple enciphering app based on dOpenssl

## Build

`make build`

By default, the image built is `encipher-frontend:$(git describe --always)` and can be overwrite via the `IMAGE` environment variable.

## Run

`docker run -v /var/run/docker.sock:/var/run/docker.sock --rm -it encipher:latest`

## Options

Optional options:

- `--version`: The version of `infinit/dopenssl` image to use.

## Tests

`make check`
