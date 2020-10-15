### What is this?

This is a simple example showing how to share a binary
between container using docker volumes.


### Build

```
> cd img1
> docker build -t img1 .

> cd img2
> docker build -t img2 .
```

### Run

```
> docker run -v bin:/home/foo/bin --name img2-run img2
> docker run -v bin:/home/foo/bin --name img1-run img1

Hello World!
Cool!
```

### Clean up

```
> docker rm img1-run img2-run
> docker volume rm bin
```
