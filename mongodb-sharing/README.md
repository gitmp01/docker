## mongodb-sharing

Show how to share a database between containers, using docker-compose.
The instance is divided into three services:

 - mongo: the database
 - service1: a python script that inserts a document inside the database
 - service2: a python script that gets the document inserted by service1

### Run

```docker-compose up --build```

### Interesting facts

1. The volume is still there after different builds and runs:

```bash
docker-compose up --build
ctrl+c
docker-compose up --build mongo service2
```

The second run will show the document inserted on the first run.


2. If you do the same as 1. but with the `-V` flag, everything is **LOST**.

```bash
docker-compose up --build
ctrl+c
docker-compose up --build -V mongo service2
```

**Note:** the `-V` flag is supposed to remove any created docker volumes, so use it 
with extreme care.

3. To make a backup run

```bash
docker exec mongodb-sharing_mongo_1 sh -c 'exec mongodump -d archive --archive' > db-backup.archive
```

**Notes:** 

 - only mongorestore can read the archive and restore the appropriate data
 - `--archive` option without any value will print the archive to stdout
