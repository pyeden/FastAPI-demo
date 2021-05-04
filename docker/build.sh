set -e
image="sampleImage/demo"
timestamp=$(date +%Y%m%d%H%M%S)
#tag=$image:$timestamp
tag=$image:latest
docker build -t $tag .

