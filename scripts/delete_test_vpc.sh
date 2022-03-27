#!/usr/bin/env bash
aws cloudformation delete-stack --stack-name "test-arole-docker"

echo "Waiting for delete-stack to finish"
aws cloudformation wait stack-delete-complete --stack-name "test-arole-docker"

echo "Stack deleted: test-arole-docker"