# get rid of old stuff
docker rmi -f $(docker images | grep "^<none>" | awk "{print $3}")
docker rm $(docker ps -q -f status=exited)

docker build --platform linux/amd64 -f Dockerfile -t lachmann12/latex:0.1 .

#docker push lachmann12/latex:0.1
#docker run -v /Users/maayanlab/Documents/GitHub/latexapi/store:/latex/example -it lachmann12/latex:0.1