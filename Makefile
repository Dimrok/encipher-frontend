TAG ?= $(shell git describe --always)
IMAGE ?= encipher-frontend:$(TAG)
TEST_IMAGE ?= encipher-frontend-tests:$(TAG)

build:
	docker build --tag $(IMAGE) .

check: build
	docker build --tag $(TEST_IMAGE) tests
	docker run -v /var/run/docker.sock:/var/run/docker.sock --rm $(TEST_IMAGE) $(IMAGE)
