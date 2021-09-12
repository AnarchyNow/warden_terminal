#!/bin/bash
# Command to build on multi platdorm
docker buildx build --platform linux/arm64,linux/amd64 --tag anarchynow/node_warden:latest --output "type=registry" .
