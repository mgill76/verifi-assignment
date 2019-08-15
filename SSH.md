# SSH access for entire company
This is a somewhat generic question, but I'll assume we don't want to use some Active Directory or Kerberos solution.

# SSH using singed certificates
In this model, users will ssh using a signed ssh certificate which is generated from their own public key and signed by an internal central Certificate Authority.

* SSH servers are configured to trust a central CA by distributing the public key to all servers and adding the below line
`TrustedUserCAKeys /etc/ssh/ca.pub`
* SSH servers are configured to 
* Users will create their own private/public keypair using ssh-keygen
* Some method is needed here to get public key to the CA server and sign, which generates a user certificate. An internally-developed CLI is best for this due to security and ease of use. If it's easy, the certs can be signed for short periods of time providing further security.
* User now can ssh using their own certificate and will ssh in as root
* User certificate will be logged in /var/log/auth.log which should be forwarded to a central log store for analysis

# Secure SSH using bastion host
The basic idea here is to configure you SSH servers to allow access only from a bastion host. 
