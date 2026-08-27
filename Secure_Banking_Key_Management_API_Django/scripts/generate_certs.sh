#!/usr/bin/env bash
set -e
mkdir -p certs
openssl req -x509 -nodes -newkey rsa:2048 -days 30 -keyout certs/server.key -out certs/server.crt -subj "/C=IN/ST=Maharashtra/L=Pune/O=Bank Demo/CN=localhost"
echo "Demo TLS certificate generated."
echo "Production certificates must come from an approved enterprise PKI."
