#!/bin/bash

RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
NC="\033[0m"

echo -e "${YELLOW}Checking system requirements...${NC}"

export PYTHONPATH="${PYTHONPATH}:$(dirname "$(cd "$(dirname "$0")"; pwd -P)")"

if ! command -v docker &> /dev/null; then
    echo -e "${RED}Docker is not installed. Please install Docker and try again.${NC}"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo -e "${RED}Docker Compose is not installed. Please install Docker Compose and try again.${NC}"
    exit 1
fi

NETWORK_NAME="sublate"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
DOCKER_COMPOSE_FILE="$SCRIPT_DIR/../docker-compose.yml"

echo -e "${YELLOW}Setting up the environment...${NC}"

if [ ! -f "$DOCKER_COMPOSE_FILE" ]; then
    echo -e "${RED}The file $DOCKER_COMPOSE_FILE was not found in the current directory.${NC}"
    exit 1
fi

if docker network inspect "$NETWORK_NAME" &> /dev/null; then
    echo -e "${GREEN}The Docker network $NETWORK_NAME already exists.${NC}"
else
    echo -e "${YELLOW}Creating Docker network $NETWORK_NAME...${NC}"
    docker network create --driver bridge "$NETWORK_NAME"
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}The Docker network $NETWORK_NAME was successfully created.${NC}"
    else
        echo -e "${RED}An error occurred while creating the Docker network $NETWORK_NAME.${NC}"
        exit 1
    fi
fi

echo -e "${YELLOW}Starting up the services...${NC}"
docker-compose -f "$DOCKER_COMPOSE_FILE" up -d --build --remove-orphans
if [ $? -ne 0 ]; then
  echo -e "${RED}An error occurred while running the docker-compose command.${NC}"
  exit 1
fi

echo -ne "${YELLOW}Waiting for the Django server to start. "
i=1
sp="/-\|"
echo -ne ' '
while [ $i -le 40 ]
do
    printf "\b${sp:i++%${#sp}:1}"
    sleep 0.10
done

echo -e "\n${YELLOW}All done! Your environment is all set up and running.${NC}"
echo -e "${GREEN}Access the application at${NC} http://localhost:9999"
