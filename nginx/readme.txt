To use:

1. Replace your.domain.com with the host that has nginx_status
2. Replace 0000 with the listening port for statsd
3. Replacee x.x.x.x with the host running statsd



This script expects to see an nginx_status of the following format:

Active connections: 2200 
server accepts handled requests
 88372093 88364544 189981064 
Reading: 54 Writing: 30 Waiting: 2116 